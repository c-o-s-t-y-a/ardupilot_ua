#!/usr/bin/env python3
"""Додає або оновлює рядок сторінки в translation-status.md.

Використання: scripts/update-status.py <переклад.md> <джерело.rst у .upstream>
Записує hash останнього коміту upstream, що змінював джерело, і сьогоднішню дату.
"""
import datetime
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
STATUS = ROOT / "translation-status.md"
HEADER = """# Стан перекладу

Hash — останній коміт [ardupilot_wiki](https://github.com/ArduPilot/ardupilot_wiki), що змінював
файл-джерело на момент перекладу. `scripts/check-stale.sh` показує сторінки, джерело яких відтоді змінилося.

| Сторінка | Переклад | Джерело | Commit | Дата |
|---|---|---|---|---|
"""


def main():
    if len(sys.argv) != 3:
        sys.exit(__doc__)
    md = Path(sys.argv[1]).resolve().relative_to(ROOT).as_posix()
    src = Path(sys.argv[2]).resolve().relative_to(ROOT / ".upstream").as_posix()
    commit = subprocess.check_output(
        ["git", "-C", str(ROOT / ".upstream"), "log", "-1", "--format=%H", "--", src], text=True).strip()
    if not commit:
        sys.exit(f"немає історії для {src}")
    title = re.search(r"^# (.+)$", (ROOT / md).read_text(encoding="utf-8"), re.M).group(1)
    page = Path(src).stem
    row = f"| {page} | [{title}]({md}) | `{src}` | `{commit[:12]}` | {datetime.date.today()} |"

    rows = []
    if STATUS.exists():
        rows = [l for l in STATUS.read_text(encoding="utf-8").splitlines()
                if l.startswith("| ") and not l.startswith("| Сторінка")]
    rows = [r for r in rows if r.split("|")[1].strip() != page] + [row]
    STATUS.write_text(HEADER + "\n".join(rows) + "\n", encoding="utf-8")
    print(row)


if __name__ == "__main__":
    main()
