---
titolo: Come aggiornare questa knowledge base
stato: attivo
creato: 2026-10-15
aggiornato: 2026-10-16
tag: [sicurezza-web]
---

# Come aggiornare questa knowledge base

## Regole

1. **Un argomento, un file.** Se una sezione supera ~200 righe o tocca un tema diverso, separala in un nuovo file e collegala.
2. **Parti dal modello.** Copia [`scheda-sicurezza-web.md`](../_modelli/scheda-sicurezza-web.md) per ogni nuovo file.
3. **Frontmatter sempre aggiornato.** A ogni modifica aggiorna `aggiornato` (come in tutto il repository); imposta `prossima_revisione` in base alla volatilità:
   - normativa, versioni software, attacchi in corso → **3 mesi**
   - standard (OWASP, NIST) → **6 mesi**
   - principi e concetti → **12 mesi**
4. **Fonti nel file e in [`fonti.md`](fonti.md).** Ogni affermazione datata o numerica deve avere una fonte. Usa ID brevi (es. `[OWASP-T10]`) definiti in `fonti.md`.
5. **Nessuna citazione lunga.** Riassumi con parole tue; i testi originali restano alle fonti.
6. **Registra in [`changelog.md`](changelog.md)** cosa è cambiato e perché.
7. **Segna l'incertezza.** Usa il marcatore `⚠️ da verificare` quando un'informazione non è confermata da una fonte primaria.

## Ciclo di revisione consigliato

| Frequenza | Cosa controllare |
|---|---|
| Mensile | Advisory sulle dipendenze, CVE critiche dello stack, catalogo CISA KEV |
| Trimestrale | File con `prossima_revisione` scaduta, scadenze normative |
| Annuale | Nuove edizioni OWASP/NIST, ristrutturazione dell'albero |

## Comandi utili

Dalla radice del repository:

```bash
# Revisioni scadute o in scadenza entro 30 giorni e marcatori aperti
python3 25-sicurezza-web/14-automazione/scripts/kb-revisioni.py --radice 25-sicurezza-web --giorni 30

# Gli stessi controlli della pipeline del repository
npx markdownlint-cli2 "**/*.md"
lychee --offline --include-fragments "**/*.md"
```

Il controllo delle revisioni gira anche da solo una volta al mese e apre una issue se trova file scaduti.
