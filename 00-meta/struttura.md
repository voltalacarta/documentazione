---
titolo: Struttura del repository
stato: attivo
creato: 2026-10-15
aggiornato: 2026-10-16
tag: [meta, struttura]
---

# Struttura del repository

## Principi

1. **Ogni cosa ha un solo posto.** Se un documento potrebbe stare in due sezioni, va in una e l'altra ci punta con un link.
2. **Le decisioni sono separate dalle descrizioni.** `10-decisioni/` dice *cosa* si è scelto e *perché*; le altre sezioni dicono *com'è* e *come si fa*.
3. **Si archivia, non si cancella.** Lo storico resta consultabile, anche grazie a Git.
4. **Ogni cartella si autodescrive** con il proprio `README.md`.

## Schema

```text
documentazione/
├── README.md              ← home e mappa
├── CLAUDE.md              ← istruzioni per l'assistente AI
├── 00-meta/               ← regole del repository
├── 10-decisioni/          ← registro decisioni (ADR)
├── 20-infrastruttura/     ← ambiente di lavoro e strumenti
├── 25-sicurezza-web/      ← sicurezza di siti e progetti digitali
├── 30-conoscenza/         ← second brain e gestione note
├── 40-procedure/          ← procedure operative
├── 50-progetti/           ← schede progetto
├── 90-archivio/           ← documenti superati
├── _modelli/              ← modelli da copiare
├── .github/               ← controlli automatici e modello di PR
├── .devcontainer/         ← ambiente Codespaces per modificare la documentazione
├── .markdownlint-cli2.jsonc ← regole di formato Markdown
├── .editorconfig          ← codifica e a capo uniformi
└── .gitignore             ← blocca segreti e file inutili
```

## Controlli automatici

A ogni push e pull request, GitHub Actions ([`controlli.yml`](../.github/workflows/controlli.yml)) verifica:

- **formato Markdown** con markdownlint;
- **link interni** con lychee: segnala file o titoli inesistenti.

Una volta al mese [`revisioni-sicurezza-web.yml`](../.github/workflows/revisioni-sicurezza-web.yml) controlla le date di revisione della sezione [Sicurezza web](../25-sicurezza-web/README.md) e apre una issue se qualcosa è scaduto.

## Numerazione a decine

I prefissi vanno di 10 in 10 per lasciare spazio a sezioni future senza rinumerare:

| Intervallo | Area | Liberi per esempio per… |
| --- | --- | --- |
| `00–09` | Meta | — |
| `10–19` | Decisioni e governance | `15-politiche/` |
| `20–29` | Infrastruttura e strumenti | `25-sicurezza-web/` (in uso), `26-servizi-esterni/` |
| `30–39` | Conoscenza | — |
| `40–49` | Operatività | `45-checklist/` |
| `50–59` | Progetti | `55-clienti/` |
| `60–89` | **Liberi** | es. `60-editoria/`, `70-amministrazione/` |
| `90–99` | Archivio | — |

## Aggiungere una nuova sezione

1. Scegli un prefisso libero nell'intervallo giusto.
2. Crea la cartella con un `README.md` (usa [`_modelli/indice-sezione.md`](../_modelli/indice-sezione.md)).
3. Aggiungi la riga nella mappa del [`README.md` principale](../README.md) e in questa tabella.
4. Se è una scelta di rilievo, registra una decisione in `10-decisioni/`.

## Sottocartelle

Dentro una sezione si creano sottocartelle quando ci sono **più di circa 7 documenti** sullo stesso tema. Anche le sottocartelle hanno il loro `README.md`.
