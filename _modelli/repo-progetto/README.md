---
titolo: "{{NOME}}"
stato: attivo
creato: {{DATA}}
aggiornato: {{DATA}}
tag: [progetto]
sintesi: "{{DESCRIZIONE}}"
---

# {{NOME}}

{{DESCRIZIONE}}

## Dove trovare cosa

| Cosa | Dove |
| --- | --- |
| Documentazione del progetto | [`docs/`](docs/README.md) |
| Decisioni del progetto | [`docs/decisioni/`](docs/decisioni/README.md) |
| Mappa compatta di tutti i file (anche per Claude) | `INDICE.md`, generato da solo |
| Regole generali di Volta la carta | [documentazione](https://github.com/{{PROPRIETARIO}}/documentazione) |

## Come si lavora

- Apri la repo in un Codespace: *Code* → *Codespaces* → *Create codespace on main*.
- Una decisione nuova: `python3 strumenti/nuova-decisione.py "Titolo"`, poi compila il file.
- Indici e mappa si aggiornano da soli dopo il push; il progetto compare nel grafo del second brain entro qualche ora.
