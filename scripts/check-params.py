#!/usr/bin/env python3
"""Перевіряє, що всі UPPER_CASE-ідентифікатори з RST-джерела є в перекладі.

Використання: scripts/check-params.py <переклад.md> <джерело.rst>
Ідентифікатор = великі літери/цифри з принаймні одним «_» (FRAME_CLASS, AHRS_ORIENTATION).
Блоки [site wiki="..."] не для copter ігноруються.
"""
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from rstutil import filter_site_blocks  # noqa: E402

IDENT_RE = re.compile(r"(?<![\w/.-])[A-Z][A-Z0-9]*(?:_[A-Z0-9]+)+(?![\w-])")


def main():
    if len(sys.argv) != 3:
        sys.exit(__doc__)
    md = Path(sys.argv[1]).read_text(encoding="utf-8")
    rst = filter_site_blocks(Path(sys.argv[2]).read_text(encoding="utf-8"))
    # мітки ".. _target:" і цілі :ref:`...<target>` — не параметри в тексті
    rst = re.sub(r"^\.\. _[^:]+:\s*$", "", rst, flags=re.M)
    rst = re.sub(r"<([^>]+)>`", "`", rst)
    missing = sorted(set(IDENT_RE.findall(rst)) - set(IDENT_RE.findall(md)))
    for ident in missing:
        print(f"{sys.argv[1]}: відсутній ідентифікатор {ident}")
    sys.exit(1 if missing else 0)


if __name__ == "__main__":
    main()
