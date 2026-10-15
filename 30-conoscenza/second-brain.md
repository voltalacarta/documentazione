---
titolo: Second brain
stato: attivo
creato: 2026-10-15
aggiornato: 2026-10-16
tag: [conoscenza, second-brain, obsidian, foam]
collegati: [0004, 0005]
---

# Second brain

Decisioni di riferimento: [0004 · Second brain su GitHub](../10-decisioni/0004-second-brain-markdown-su-github.md) e [0005 · Strumenti online gratuiti](../10-decisioni/0005-strumenti-online-gratuiti.md).

Repository: [`voltalacarta/second-brain`](https://github.com/voltalacarta/second-brain) (**privato**). Uso quotidiano: [Usare il second brain](../40-procedure/usare-il-second-brain.md).

## Differenza con questo repository

| | `documentazione` | `second-brain` |
| --- | --- | --- |
| Contenuto | Ciò che è **deciso e ufficiale** | Appunti, idee, letture, bozze |
| Tono | Formale, stabile | Libero, in evoluzione |
| Visibilità | pubblico (da valutare) | **privato** |

Quando un'idea del second brain diventa una scelta, si scrive una decisione qui.

## Struttura (metodo PARA)

```text
second-brain/
├── 00-inbox/        ← tutto ciò che entra, da smistare
├── 01-giornaliere/  ← una nota al giorno (AAAA-MM-GG.md)
├── 10-progetti/     ← iniziative con un obiettivo e una fine
├── 20-aree/         ← responsabilità continue
├── 30-risorse/      ← argomenti, letture, riferimenti
├── 40-archivio/     ← ciò che non è più attivo
├── _modelli/        ← modelli per Obsidian
├── _allegati/       ← immagini compresse
├── .foam/templates/ ← modelli per Foam
├── .obsidian/       ← impostazioni condivise di Obsidian
├── .vscode/         ← impostazioni di Foam ed estensioni consigliate
├── .devcontainer/   ← ambiente Codespaces con Foam
├── .github/         ← Action e script che generano grafo.md
├── grafo.md         ← grafo delle note, generato in automatico
└── CLAUDE.md        ← istruzioni per Claude
```

## Strumenti

| Dove | Strumento | Funzioni |
| --- | --- | --- |
| Ovunque, senza installare nulla | File **`grafo.md`** su github.com | Grafo dei collegamenti disegnato da GitHub, rigenerato da una GitHub Action a ogni modifica |
| Browser (completo) | Codespaces + **Foam** | Wikilink, backlink, grafo interattivo, note giornaliere, modelli |
| Browser (rapido) | github.dev + Foam | Modifica e link; alcune funzioni possono essere ridotte |
| Telefono | **Obsidian** + plugin **Git** | Esperienza Obsidian completa |
| Assistente | **Claude** | Smistare l'inbox, collegare, riassumere |

Foam e Obsidian condividono la stessa struttura: note giornaliere in `01-giornaliere/`, nuove note in `00-inbox/`, allegati in `_allegati/`. I modelli sono duplicati perché le due app usano segnaposto diversi (`{{date}}` per Obsidian, `$FOAM_DATE_*` per Foam).

## Regole

- Link tra note con `[[nome-nota]]`.
- Nomi file in minuscolo con trattini.
- Immagini compresse in `_allegati/`; PDF e file grandi fuori dal repository, solo il link.
- Nessun dato sensibile (vedi [sicurezza](../20-infrastruttura/sicurezza.md#dati-sensibili)).
- Fine sessione: commit e push.

## Automazioni possibili

Da valutare e, se adottate, registrare come decisione:

- nota giornaliera creata ogni mattina;
- revisione settimanale: smistamento dell'inbox, collegamenti, progetti fermi;
- riepilogo mensile di quanto scritto.

## Da completare

- [x] Creare il repository privato `second-brain` su GitHub e caricare la struttura (2026-10-15)
- [ ] Configurare Obsidian mobile con il plugin Git (facoltativo)
- [ ] Decidere le automazioni
