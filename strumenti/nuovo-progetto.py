#!/usr/bin/env python3
"""Prepara una repo di progetto nuova (vuota) con la struttura standard di Volta la carta.

    python3 strumenti/nuovo-progetto.py ../nome-repo --nome "Nome del progetto" --descrizione "Una riga."

Copia nella cartella: il modello _modelli/repo-progetto/ (con i segnaposto compilati), gli
strumenti (indici, controlli, nuova decisione), le GitHub Actions e le configurazioni.
La repo entra da sola nel grafo del second brain. Poi: git add, commit, push.
"""

from __future__ import annotations

import argparse
import shutil
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from doclib import RADICE, oggi  # noqa: E402

MODELLO = RADICE / "_modelli" / "repo-progetto"
STRUMENTI = ["doclib.py", "indici.py", "controlla.py", "nuova-decisione.py"]
WORKFLOW = ["controlli.yml", "indici.yml"]
CONFIG = [".markdownlint-cli2.jsonc", ".editorconfig", ".gitignore"]


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("cartella", help="cartella della repo appena clonata (vuota)")
    ap.add_argument("--nome", required=True)
    ap.add_argument("--descrizione", required=True)
    ap.add_argument("--proprietario", default="voltalacarta")
    ap.add_argument("--forza", action="store_true", help="scrivi anche se la cartella contiene già file")
    a = ap.parse_args()

    dest = Path(a.cartella).resolve()
    dest.mkdir(parents=True, exist_ok=True)
    gia = [p for p in dest.iterdir() if p.name != ".git"]
    if gia and not a.forza:
        print(f"La cartella non è vuota ({', '.join(p.name for p in gia[:5])}…): usa --forza per scrivere comunque.")
        return 1

    valori = {"{{NOME}}": a.nome, "{{DESCRIZIONE}}": a.descrizione, "{{DATA}}": oggi(), "{{PROPRIETARIO}}": a.proprietario}
    scritti = []
    for src in sorted(MODELLO.rglob("*")):
        if src.is_dir():
            continue
        rel = src.relative_to(MODELLO)
        out = dest / rel
        out.parent.mkdir(parents=True, exist_ok=True)
        testo = src.read_text(encoding="utf-8")
        for k, v in valori.items():
            testo = testo.replace(k, v)
        out.write_text(testo, encoding="utf-8")
        scritti.append(rel.as_posix())
    for nome in STRUMENTI:
        (dest / "strumenti").mkdir(exist_ok=True)
        shutil.copy2(RADICE / "strumenti" / nome, dest / "strumenti" / nome)
        scritti.append(f"strumenti/{nome}")
    for nome in WORKFLOW:
        (dest / ".github" / "workflows").mkdir(parents=True, exist_ok=True)
        shutil.copy2(RADICE / ".github" / "workflows" / nome, dest / ".github" / "workflows" / nome)
        scritti.append(f".github/workflows/{nome}")
    for nome in CONFIG:
        if (RADICE / nome).is_file():
            shutil.copy2(RADICE / nome, dest / nome)
            scritti.append(nome)

    subprocess.run([sys.executable, str(dest / "strumenti" / "indici.py")], check=True, capture_output=True)
    print(f"Pronta: {dest} ({len(scritti)} file + INDICE.md)")
    print("Ora: git add -A && git commit -m 'struttura: impianto iniziale' && git push")
    return 0


if __name__ == "__main__":
    sys.exit(main())
