#!/usr/bin/env python3
"""Перетворює :ref:-мітки ardupilot_wiki на посилання для перекладу.

Використання: scripts/ref-url.py <сторінка.md> <мітка> [...]
  - мітку сторінки, вже перекладеної (є в translation-status.md), — на відносний шлях .md;
  - інакше — на https://ardupilot.org/<wiki>/docs/<файл>.html[#якір] + «(ще не перекладено)»;
  - параметри (FRAME_CLASS) — на `FRAME_CLASS`.
Мітки з префіксом (planner:home, copter:foo) шукаються у відповідній вікі.
"""
import os
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
UP = ROOT / ".upstream"
WIKIS = {"copter": ["copter", "common"], "planner": ["planner", "common"],
         "planner2": ["planner2", "common"], "plane": ["common"], "rover": ["common"]}


def make_id(label):
    """Як docutils.nodes.make_id: нижній регістр, усе крім [a-z0-9] → «-»."""
    return re.sub(r"[^a-z0-9]+", "-", label.lower()).strip("-")


def translated():
    """{файл-джерело без .rst: шлях до .md}"""
    out = {}
    status = ROOT / "translation-status.md"
    for line in status.read_text(encoding="utf-8").splitlines():
        m = re.match(r"\| \S+ \| \[[^]]*\]\(([^)]+)\) \| `([^`]+)`", line)
        if m:
            out[Path(m.group(2)).stem] = ROOT / m.group(1)
    return out


# мітки сторінок, які update.py генерує під час збірки вікі (їх немає в .rst)
GENERATED = {"binary-features": ("binary-features", None), "all-features": ("binary-features", "all-features")}


def find_label(label, wiki):
    if label in GENERATED:
        return GENERATED[label]
    pat = re.compile(rf"^\.\. _{re.escape(label)}:\s*$", re.M | re.I)
    for sub in WIKIS[wiki]:
        for f in sorted((UP / sub / "source" / "docs").glob("*.rst")):
            text = f.read_text(encoding="utf-8", errors="replace")
            m = pat.search(text)
            if m:
                # мітка на початку файлу (до першого заголовка) — це сама сторінка
                before = text[:m.start()]
                is_page = not re.search(r"^(=+|-+|\^+|~+)\s*$", before, re.M)
                return f.stem, (None if is_page else make_id(label))
    return None, None


def resolve(md_page, ref):
    wiki, _, label = ref.rpartition(":")
    wiki = wiki or "copter"
    if re.fullmatch(r"[A-Z][A-Z0-9_]*", label):
        return f"`{label}`"
    if wiki not in WIKIS:
        # джерел цієї вікі (dev, mavproxy…) немає в .upstream — не вгадуємо адресу
        return f"https://ardupilot.org/{wiki}/" if label == "home" else f"?? мітка {ref}: вікі {wiki} не клоновано"
    stem, anchor = find_label(label, wiki)
    if stem is None:
        return f"?? мітку {ref} не знайдено"
    done = translated()
    if wiki == "copter" and stem in done:
        rel = os.path.relpath(done[stem], Path(md_page).resolve().parent)
        # у перекладі якір — slug українського заголовка, а не мітка RST
        return rel + (f"#{anchor}  ⚠ якір перевірте: у перекладі slug заголовка інший" if anchor else "")
    site = wiki
    return f"https://ardupilot.org/{site}/docs/{stem}.html" + (f"#{anchor}" if anchor else "") + "  *(ще не перекладено)*"


if __name__ == "__main__":
    if len(sys.argv) < 3:
        sys.exit(__doc__)
    for ref in sys.argv[2:]:
        print(f"{ref} -> {resolve(sys.argv[1], ref)}")
