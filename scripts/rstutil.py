"""Спільні утиліти для роботи з RST-джерелами ardupilot_wiki."""
import re

SITE_RE = re.compile(r'\[site\s+wiki="([^"]*)"\](.*?)\[/site\]', re.S)


def filter_site_blocks(text, wiki="copter"):
    """Лишає лише [site]-блоки для заданої вікі, решту видаляє."""
    def repl(m):
        wikis = [w.strip() for w in m.group(1).split(",")]
        return m.group(2) if wiki in wikis else ""
    return SITE_RE.sub(repl, text)
