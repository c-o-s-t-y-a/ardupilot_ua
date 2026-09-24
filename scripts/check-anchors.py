#!/usr/bin/env python3
"""Перевіряє якорі посилань (#...) у зібраному сайті. Запускати після `mkdocs build`.

MkDocs сам не перевіряє, чи існує якір на цільовій сторінці, тож битий
«[текст](page.md#якір)» чи «(#якір)» знаходимо тут.
"""
import re
import sys
import urllib.parse
from pathlib import Path

DOCS, SITE = Path("docs").resolve(), Path("site")


def ids(page):
    return set(re.findall(r'id="([^"]+)"', page.read_text(encoding="utf-8")))


def main():
    broken = []
    for md in sorted(DOCS.rglob("*.md")):
        rel = md.relative_to(DOCS).with_suffix("")
        own = SITE / (rel.parent if rel.name == "index" else rel) / "index.html"
        for target, anchor in re.findall(r"\]\(([\w./-]*\.md)?#([^)\s]+)\)", md.read_text(encoding="utf-8")):
            page = own
            if target:
                t = (md.parent / target).resolve().relative_to(DOCS).with_suffix("")
                page = SITE / (t.parent if t.name == "index" else t) / "index.html"
            if urllib.parse.unquote(anchor) not in ids(page):
                broken.append(f"{md.relative_to(DOCS.parent)}: {target or ''}#{anchor}")
    print("\n".join(broken) if broken else "Якорі OK")
    sys.exit(1 if broken else 0)


if __name__ == "__main__":
    main()
