---
titolo: Second brain
stato: bozza
creato: 2026-10-15
aggiornato: 2026-10-15
tag: [conoscenza, second-brain, obsidian, foam]
collegati: [0004]
---

# Second brain

Decisione di riferimento: [0004 · Second brain in Markdown su GitHub](../10-decisioni/0004-second-brain-markdown-su-github.md).

> **Stato:** bozza. Il metodo è deciso, il repository `second-brain` non è ancora stato creato.

## Differenza con questo repository

| | `documentazione` | `second-brain` |
| --- | --- | --- |
| Contenuto | Ciò che è **deciso e ufficiale** | Appunti, idee, letture, bozze |
| Tono | Formale, stabile | Libero, in evoluzione |
| Visibilità | da definire | **privato** |

Quando un'idea del second brain diventa una scelta, si scrive una decisione qui.

## Struttura proposta

Ispirata al metodo PARA, con cartelle per l'ingresso e le note giornaliere:

```text
second-brain/
├── 00-inbox/        ← tutto ciò che entra, da smistare
├── 01-giornaliere/  ← una nota al giorno (AAAA-MM-GG.md)
├── 10-progetti/     ← iniziative con un obiettivo e una scadenza
├── 20-aree/         ← responsabilità continue (es. catalogo, amministrazione)
├── 30-risorse/      ← argomenti di interesse, letture, riferimenti
├── 40-archivio/     ← ciò che non è più attivo
├── _modelli/        ← modelli di nota
├── _allegati/       ← immagini compresse
├── .foam/           ← configurazione Foam
└── CLAUDE.md        ← istruzioni per Claude
```

## Strumenti

| Dove | Strumento | Funzioni |
| --- | --- | --- |
| Browser | Codespaces o github.dev + estensione **Foam** | Wikilink, backlink, grafo, note giornaliere |
| Telefono | App **Obsidian** + plugin Git (facoltativo) | Esperienza Obsidian completa |
| Assistente | **Claude** | Smistare l'inbox, collegare note, riassumere |

## Regole

- Link tra note con `[[nome-nota]]`.
- Immagini compresse in `_allegati/`; PDF e file grandi fuori dal repository, solo il link.
- Nessun dato sensibile (vedi [sicurezza](../20-infrastruttura/sicurezza.md#dati-sensibili)).

## Automazioni possibili

Da valutare e, se adottate, registrare come decisione:

- nota giornaliera creata ogni mattina;
- revisione settimanale: smistamento dell'inbox, collegamenti, progetti fermi;
- riepilogo mensile di quanto scritto.

## Da completare

- [ ] Creare il repository privato `second-brain`
- [ ] Configurare Foam e i modelli di nota
- [ ] Scrivere il `CLAUDE.md` del second brain
- [ ] Decidere le automazioni
