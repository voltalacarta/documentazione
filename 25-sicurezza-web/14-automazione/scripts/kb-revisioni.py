#!/usr/bin/env python3
"""
kb-revisioni.py — elenca i file della knowledge base con revisione scaduta
o in scadenza, e i marcatori "da verificare" ancora aperti.

Uso (dalla radice del repository):
    python3 25-sicurezza-web/14-automazione/scripts/kb-revisioni.py --radice 25-sicurezza-web
    python3 25-sicurezza-web/14-automazione/scripts/kb-revisioni.py --radice 25-sicurezza-web --giorni 30     # anche quelli in scadenza entro 30 giorni
    python3 25-sicurezza-web/14-automazione/scripts/kb-revisioni.py --radice 25-sicurezza-web --markdown > report.md

Codice di uscita: 1 se ci sono revisioni scadute (utile in un job programmato).
Rev. 2026-10-15
"""
from __future__ import annotations

import argparse
import datetime as dt
import pathlib
import re
import sys

RE_FRONT = re.compile(r"^---\n(.*?)\n---", re.S)
RE_CAMPO = re.compile(r"^(\w+):\s*(.+)$", re.M)


def leggi_frontmatter(testo: str) -> dict[str, str]:
    m = RE_FRONT.match(testo)
    return dict(RE_CAMPO.findall(m.group(1))) if m else {}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--radice", default=".", help="cartella della knowledge base")
    ap.add_argument("--giorni", type=int, default=0, help="includi anche i file in scadenza entro N giorni")
    ap.add_argument("--oggi", help="data di riferimento AAAA-MM-GG (default: oggi)")
    ap.add_argument("--markdown", action="store_true", help="output in Markdown")
    a = ap.parse_args()

    oggi = dt.date.fromisoformat(a.oggi) if a.oggi else dt.date.today()
    limite = oggi + dt.timedelta(days=a.giorni)
    radice = pathlib.Path(a.radice)

    scaduti, in_scadenza, senza_data, aperti = [], [], [], []
    for f in sorted(radice.rglob("*.md")):
        if f.name in {"changelog.md", "fonti.md", "contribuire.md"}:
            continue
        # I modelli da compilare non hanno frontmatter: si rivede solo il loro README
        if "15-modelli" in f.parts and f.name != "README.md":
            continue
        testo = f.read_text(encoding="utf-8")
        fm = leggi_frontmatter(testo)
        rel = f.relative_to(radice).as_posix()
        data = fm.get("prossima_revisione")
        # Gli indici delle cartelle non hanno una scadenza propria
        if f.name == "README.md" and not data:
            continue
        if not data:
            senza_data.append(rel)
        else:
            try:
                d = dt.date.fromisoformat(data.strip())
            except ValueError:
                senza_data.append(f"{rel} (data non valida: {data})")
            else:
                if d < oggi:
                    scaduti.append((rel, d))
                elif d <= limite:
                    in_scadenza.append((rel, d))
        for n, riga in enumerate(testo.splitlines(), 1):
            if "⚠️ da verificare" in riga and "`⚠️ da verificare`" not in riga:
                aperti.append(f"{rel}:{n}")

    if a.markdown:
        print(f"# Revisioni della knowledge base — {oggi}\n")
        print(f"## Scaduti ({len(scaduti)})\n")
        print("\n".join(f"- [ ] `{p}` — dal {d}" for p, d in scaduti) or "_nessuno_")
        if a.giorni:
            print(f"\n## In scadenza entro {a.giorni} giorni ({len(in_scadenza)})\n")
            print("\n".join(f"- [ ] `{p}` — {d}" for p, d in in_scadenza) or "_nessuno_")
        print(f"\n## Marcatori 'da verificare' ({len(aperti)})\n")
        print("\n".join(f"- `{x}`" for x in aperti) or "_nessuno_")
        if senza_data:
            print(f"\n## Senza data di revisione ({len(senza_data)})\n")
            print("\n".join(f"- `{x}`" for x in senza_data))
    else:
        print(f"Data di riferimento: {oggi}")
        print(f"Scaduti: {len(scaduti)}")
        for p, d in scaduti:
            print(f"  ❌ {p}  (dal {d})")
        if a.giorni:
            print(f"In scadenza entro {a.giorni} giorni: {len(in_scadenza)}")
            for p, d in in_scadenza:
                print(f"  ⚠️  {p}  ({d})")
        print(f"Marcatori 'da verificare': {len(aperti)}")
        for x in aperti:
            print(f"  · {x}")
        if senza_data:
            print(f"Senza data: {len(senza_data)}")
            for x in senza_data:
                print(f"  ? {x}")
    return 1 if scaduti else 0


if __name__ == "__main__":
    sys.exit(main())
