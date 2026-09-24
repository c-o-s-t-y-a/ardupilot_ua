#!/usr/bin/env python3
"""Додає переклад у дужках після першої появи терміна, якщо його там немає.

Використання: scripts/gloss-first.py <файл.md> [...]
Логіка пошуку та сама, що в check-terms.py (заголовки, код, URL, UI-назви
пропускаються). Перевірте результат очима: іноді природніше переформулювати речення.
"""
import importlib.util
import re
import sys
from pathlib import Path

spec = importlib.util.spec_from_file_location("ct", Path(__file__).with_name("check-terms.py"))
ct = importlib.util.module_from_spec(spec)
spec.loader.exec_module(ct)


def fix(path):
    raw = Path(path).read_text(encoding="utf-8")
    added = []
    for en, ua in ct.load_glossary():
        text = ct.mask(ct.prepare(raw), r"(?m)^#.*$")
        m = next(iter(ct.en_pattern(en).finditer(text)), None)
        if not m:
            continue
        after = text[m.end():]
        glossed = re.match(r"\s*\(([^()\n]*)\)", after)
        if glossed and glossed.group(1) == ua:
            continue
        raw = raw[:m.end()] + f" ({ua})" + raw[m.end():]
        added.append(f"{m.group(0)} ({ua})")
    Path(path).write_text(raw, encoding="utf-8")
    for a in added:
        print(f"{path}: + {a}")


if __name__ == "__main__":
    for f in sys.argv[1:]:
        fix(f)
