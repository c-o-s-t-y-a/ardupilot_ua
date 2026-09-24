#!/usr/bin/env python3
"""Замінює посилання «ще не перекладено» на локальні для сторінок, що вже є в translation-status.md.

Використання: scripts/relink.py [файл.md ...]   (без аргументів — усі docs/**/*.md)
«[текст](https://ardupilot.org/copter/docs/<файл>.html#якір) *(ще не перекладено)*»
→ «[текст](<відносний шлях>.md#якір)». Якір лишається як є — перевірте його вручну,
якщо заголовок у перекладі має інший slug.
"""
import os
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
ROOT = Path(__file__).resolve().parent.parent
LINK = re.compile(r"\]\(https://ardupilot\.org/copter/docs/([\w.-]+)\.html(#[\w-]+)?\)\s*\*\(ще не перекладено\)\*")


def translated():
    out = {}
    for line in (ROOT / "translation-status.md").read_text(encoding="utf-8").splitlines():
        m = re.match(r"\| \S+ \| \[[^]]*\]\(([^)]+)\) \| `([^`]+)`", line)
        if m:
            out[Path(m.group(2)).stem] = ROOT / m.group(1)
    return out


def main():
    done = translated()
    files = [Path(f) for f in sys.argv[1:]] or sorted((ROOT / "docs").rglob("*.md"))
    for f in files:
        text = f.read_text(encoding="utf-8")

        def repl(m):
            target = done.get(m.group(1))
            if not target:
                return m.group(0)
            rel = os.path.relpath(target, f.resolve().parent)
            if m.group(2):
                print(f"  ⚠ {f.name}: якір {m.group(2)} → {rel} — замініть на slug українського заголовка")
            return f"]({rel}{m.group(2) or ''})"

        new = LINK.sub(repl, text)
        if new != text:
            f.write_text(new, encoding="utf-8")
            print(f"{f}: {len(LINK.findall(text)) - len(LINK.findall(new))} посилань")


if __name__ == "__main__":
    main()
