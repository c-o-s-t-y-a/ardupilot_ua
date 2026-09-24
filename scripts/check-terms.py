#!/usr/bin/env python3
"""Перевіряє вживання термінів глосарію в перекладених сторінках.

Використання: scripts/check-terms.py <файл.md> [...]

Правила (для кожного терміна з docs/glossary.md):
  1. перша поява в тексті — «term (переклад)», переклад дослівно як у глосарії;
  2. наступні появи — без перекладу в дужках;
  3. немає української форми терміна поза дужками («акселерометр»);
  4. немає транслітерацій («фейлсейф», «армінг», ...).
Не перевіряються: заголовки (для правил 1–2), код `...`, жирні латинські
назви UI (**Calibrate Level**), URL-и посилань і картинок, рядок «> Оригінал:».
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
GLOSSARY = ROOT / "docs" / "glossary.md"

TRANSLIT = [r"фейлсейф\w*", r"фейл-сейф\w*", r"арм(?:ін|ит|л|ув)\w*", r"заарм\w*",
            r"дезарм\w*", r"розарм\w*", r"тюнінг\w*", r"тюн\b", r"лог(?:и|ів|ах|ом|у|а)?",
            r"логуванн\w*", r"есц\w*", r"акселерометр\w*(?=-)"]
UA_ENDINGS = "аеєиіїоуюяйь"


def load_glossary():
    terms = []
    for line in GLOSSARY.read_text(encoding="utf-8").splitlines():
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) < 2 or cells[0] in ("EN", "") or set(cells[0]) <= set("-"):
            continue
        terms.append((cells[0], cells[1]))
    return terms


def en_pattern(term):
    words = r"\s+".join(re.escape(w) for w in term.split())
    # term, terms, term-<будь-що>; без продовження латиницею (arm ≠ armed)
    return re.compile(rf"(?<![\w-]){words}(?:s|-[а-яіїєґ]+)?(?![\w])", re.I)


ALLOWED_SUFFIXES = {"-и", "-ах"}


def ua_pattern(ua):
    parts = []
    for w in ua.split():
        stem = w.rstrip(UA_ENDINGS) if len(w) > 4 else w
        parts.append(re.escape(stem) + r"[а-яіїєґʼ']{0,4}")
    joined = r"\s+".join(parts)
    return re.compile(rf"(?<![\w]){joined}(?![\w])", re.I)


def mask(text, pattern):
    return re.sub(pattern, lambda m: re.sub(r"[^\n]", " ", m.group(0)), text)


def prepare(md):
    """Заміняє пробілами все, що не перевіряється, зберігаючи позиції."""
    md = mask(md, r"(?m)^> Оригінал:.*$")
    md = mask(md, r"`[^`\n]*`")
    md = mask(md, r"\]\([^)\s]*\)")                      # URL-и посилань/картинок
    md = mask(md, r"\*\*[^*\nа-яіїєґА-ЯІЇЄҐ]+\*\*")       # **UI-назви латиницею**
    md = mask(md, r"https?://\S+")
    return md


def check(path, terms):
    raw = Path(path).read_text(encoding="utf-8")
    text = prepare(raw)
    body = mask(text, r"(?m)^#.*$")                     # заголовки — окремо
    out = []

    def lineno(pos):
        return raw.count("\n", 0, pos) + 1

    # дужкові фрагменти, де українська форма дозволена
    brackets = [(m.start(), m.end()) for m in re.finditer(r"\([^()\n]*\)", text)]

    def in_brackets(pos):
        return any(s <= pos < e for s, e in brackets)

    for en, ua in terms:
        gloss = f"({ua})"
        first = True
        for m in en_pattern(en).finditer(text):
            suffix = re.search(r"-[а-яіїєґ]+$", m.group(0))
            if suffix and suffix.group(0) not in ALLOWED_SUFFIXES:
                out.append(f"{lineno(m.start())}: суфікс «{m.group(0)}» — дозволено лише -и/-ах")
        for m in en_pattern(en).finditer(body):
            after = body[m.end():]
            glossed = re.match(r"\s*\(([^()\n]*)\)", after)
            if first:
                if not glossed or glossed.group(1) != ua:
                    got = f"({glossed.group(1)})" if glossed else "без дужок"
                    out.append(f"{lineno(m.start())}: перша поява «{m.group(0)}» має бути з {gloss}, а не {got}")
                first = False
            elif glossed and glossed.group(1) == ua:
                out.append(f"{lineno(m.start())}: повторний переклад «{m.group(0)} {gloss}» — лише при першій появі")
        for m in ua_pattern(ua).finditer(text):
            if not in_brackets(m.start()):
                out.append(f"{lineno(m.start())}: українська форма «{m.group(0)}» без EN (має бути «{en}»)")

    for pat in TRANSLIT:
        for m in re.finditer(rf"(?<![\w]){pat}", text, re.I):
            out.append(f"{lineno(m.start())}: транслітерація «{m.group(0)}»")

    for m in re.finditer(r":ref:|^\.\. |\[/?site|\[copywiki", raw, re.M):
        out.append(f"{lineno(m.start())}: залишок RST-синтаксису «{m.group(0).strip()}»")

    return [f"{path}:{line}" for line in sorted(set(out), key=lambda s: int(s.split(':')[0]))]


def main():
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    terms = load_glossary()
    problems = [p for f in sys.argv[1:] for p in check(f, terms)]
    print("\n".join(problems) if problems else "OK")
    sys.exit(1 if problems else 0)


if __name__ == "__main__":
    main()
