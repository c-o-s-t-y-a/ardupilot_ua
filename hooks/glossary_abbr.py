"""MkDocs hook: підказки для термінів з docs/glossary.md і кольорові примітки.

До кожної сторінки (крім самого глосарію) дописуються визначення abbr
(«*[term]: UA — пояснення»), тож при наведенні на термін видно переклад і пояснення.
"""
import re
from pathlib import Path

_abbr = ""


def _plain(text):
    text = re.sub(r"\*\*|\*|`", "", text)
    return text.replace('"', "'").strip()


def on_config(config):
    global _abbr
    lines = []
    glossary = Path(config["docs_dir"]) / "glossary.md"
    for row in glossary.read_text(encoding="utf-8").splitlines():
        cells = [c.strip() for c in row.strip().strip("|").split("|")]
        if len(cells) < 3 or cells[0] in ("EN", "") or set(cells[0]) <= set("-"):
            continue
        en, ua, note = cells[0], cells[1], _plain(cells[2])
        title = f"{ua} — {note}" if note else ua
        # лише написання як у глосарії: так **Calibrate Level** чи «Loading Firmware»
        # (назви UI й оригіналів) не отримують підказку
        lines.append(f"*[{en}]: {title}")
    _abbr = "\n\n" + "\n".join(lines) + "\n"
    return config


def on_page_markdown(markdown, page, **kwargs):
    markdown = _admonitions(markdown)
    if page.file.src_uri == "glossary.md":
        return markdown
    return markdown + _abbr


# «> **Примітка.** текст» → кольоровий блок Material (admonition).
# Вихідний Markdown не змінюється, тож на GitHub це лишається цитатою.
_ADMONITIONS = {"Примітка": "note", "Порада": "tip", "Попередження": "danger",
                "Важливо": "info", "Увага": "warning"}
_QUOTE_RE = re.compile(
    r"^> \*\*(" + "|".join(_ADMONITIONS) + r")\.\*\* ?(.*(?:\n>.*)*)", re.M)


def _to_admonition(m):
    body = re.sub(r"^> ?", "", m.group(2), flags=re.M)
    body = "\n".join("    " + line if line else "" for line in body.splitlines())
    return f'!!! {_ADMONITIONS[m.group(1)]} "{m.group(1)}"\n{body}'


def _admonitions(markdown):
    return _QUOTE_RE.sub(_to_admonition, markdown)
