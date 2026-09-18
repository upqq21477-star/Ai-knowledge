#!/usr/bin/env python3
"""
掃描 repo 內所有 .md 檔，讀取簡易 frontmatter（id / status），
自動產生「現況-自動產生.md」，並檢查版本一致性。

不需要任何外部套件（不用 pip install），只用 Python 標準函式庫，
可以直接在 GitHub Actions 的 ubuntu-latest 上執行。

使用方式：
    在要標記的檔案最上方加入類似這樣的區塊：

    ---
    id: 交接資料
    status: current
    ---

    同一個 id 的舊版本檔案，把 status 改成 superseded（或直接不寫，
    腳本會當作歷史版本處理，只是不會警告「找不到 current」）。
"""

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# 這些資料夾本來就是歷史封存區，不必納入一致性檢查
SKIP_DIR_NAMES = {"廢棄", "舊資料"}

FRONTMATTER_RE = re.compile(r"^---\n(.*?)\n---\n", re.DOTALL)
KV_RE = re.compile(r"^(\w+):\s*(.+)$")
VERSION_RE = re.compile(r"-v(\d+(?:\.\d+)*)(?:\.md)?$")


def parse_frontmatter(text: str) -> dict:
    m = FRONTMATTER_RE.match(text)
    if not m:
        return {}
    data = {}
    for line in m.group(1).splitlines():
        kv = KV_RE.match(line.strip())
        if kv:
            data[kv.group(1)] = kv.group(2).strip()
    return data


def version_key(v: str):
    return [int(n) for n in v.split(".")]


def main() -> int:
    entries: dict[str, list[tuple[Path, dict]]] = {}

    for path in ROOT.rglob("*.md"):
        if any(part in SKIP_DIR_NAMES for part in path.parts):
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except Exception:
            continue
        fm = parse_frontmatter(text)
        doc_id = fm.get("id")
        if doc_id:
            entries.setdefault(doc_id, []).append((path, fm))

    lines = ["# 現況（自動產生，請勿手動編輯，改由腳本重新產生）", ""]
    warnings: list[str] = []

    for doc_id, items in sorted(entries.items()):
        currents = [p for p, fm in items if fm.get("status") == "current"]

        if len(currents) == 0:
            warnings.append(f"[{doc_id}] 沒有任何檔案標記 status: current")
        elif len(currents) > 1:
            names = ", ".join(str(p.relative_to(ROOT)) for p in currents)
            warnings.append(f"[{doc_id}] 有 {len(currents)} 個檔案同時標記 current：{names}")

        versioned = []
        for p, _ in items:
            vm = VERSION_RE.search(p.stem)
            if vm:
                versioned.append((p, vm.group(1)))

        if versioned:
            versioned.sort(key=lambda x: version_key(x[1]))
            latest_path = versioned[-1][0]
            if currents and latest_path not in currents:
                warnings.append(
                    f"[{doc_id}] 檔名版本最新的是 {latest_path.name}，"
                    f"但標記 current 的卻是 {currents[0].name}（可能是漏改，或刻意保留舊版為現行）"
                )

        lines.append(f"## {doc_id}")
        for p, fm in sorted(items, key=lambda x: x[0].name):
            tag = "→ 現行" if fm.get("status") == "current" else "  歷史"
            lines.append(f"- {tag}：`{p.relative_to(ROOT)}`")
        lines.append("")

    if warnings:
        lines.append("## ⚠️ 一致性警告")
        lines.extend(f"- {w}" for w in warnings)
        lines.append("")

    if not entries:
        lines.append("_（目前沒有任何檔案帶有 id frontmatter，尚未開始標記）_")

    out_path = ROOT / "現況-自動產生.md"
    out_path.write_text("\n".join(lines), encoding="utf-8")

    if warnings:
        print("發現一致性問題：", file=sys.stderr)
        for w in warnings:
            print(" -", w, file=sys.stderr)
        return 1

    print(f"OK：共 {len(entries)} 個 id，未發現一致性問題。")
    return 0


if __name__ == "__main__":
    sys.exit(main())
