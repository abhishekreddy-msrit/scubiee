"""Operator docs must not pin a scubiee== version."""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "web-info"
PIN = re.compile(r"scubiee==")


def test_operator_docs_do_not_pin_scubiee_version() -> None:
    hits: list[str] = []
    for path in sorted(DOCS.rglob("*.md")):
        text = path.read_text(encoding="utf-8")
        for lineno, line in enumerate(text.splitlines(), 1):
            if PIN.search(line):
                rel = path.relative_to(ROOT).as_posix()
                hits.append(f"{rel}:{lineno}: {line.strip()}")
    assert not hits, "docs/web-info must not pin scubiee==:\n" + "\n".join(hits)
