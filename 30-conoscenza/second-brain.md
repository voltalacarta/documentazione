---
titolo: Second brain
stato: attivo
creato: 2026-10-15
aggiornato: 2026-10-19
tag: [conoscenza, second-brain, obsidian, foam]
sintesi: "Struttura, strumenti e regole del second brain"
collegati: [0004, 0005, 0007]
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
├── .devcontainer/   ← Codespace con Foam; apre da solo il grafo interattivo
├── _config/         ← grafo.yml (impostazioni) e vocabolario.yml (concetti)
├── .github/kg/      ← il motore del grafo (Python, con i suoi test)
├── _grafo/          ← GENERATO: pagine di repo e concetti, note-ponte, indici, index.html
├── grafo.md         ← GENERATO: panoramica con diagramma
└── CLAUDE.md        ← istruzioni brevi per Claude
```

## Il grafo della conoscenza

Decisione di riferimento: [0007 · Grafo della conoscenza automatico](../10-decisioni/0007-grafo-della-conoscenza-automatico-su-tutte-le-repo.md).

Il second brain è l'**hub** che collega tutte le repo di voltalacarta. Una GitHub Action (*Aggiorna il grafo*) gira ogni 3 ore, a ogni push e su avviso delle altre repo. Non usa modelli AI.

| Nodo | Da dove viene |
| --- | --- |
| 📦 Repo | Scoperta automatica di tutte le repo del proprietario |
| Documento | Ogni file `.md` delle altre repo (con una nota-ponte in `_grafo/documenti/`) |
| Nota | Le note del second brain |
| Concetto | Tag e campi del frontmatter, vocabolario, glossari, `[[wikilink]]` a note non ancora create |

| Collegamento | Quando |
| --- | --- |
| contiene | Una repo contiene un file |
| link | Un file rimanda a un altro, anche in un'altra repo |
| collegato | Una decisione cita un'altra nel campo `collegati` |
| tag | Un file ha quel tag o concetto nel frontmatter |
| menziona | Il nome di un concetto compare nel testo (al massimo 6 per file, i più frequenti) |

Prodotti, tutti rigenerati a ogni giro (solo i file cambiati):

- [`grafo.md`](https://github.com/voltalacarta/second-brain/blob/main/grafo.md): panoramica Mermaid, leggibile su github.com;
- `_grafo/repo/`, `_grafo/concetti/`: una pagina per repo e per concetto, con mini-grafo ed elenchi;
- `_grafo/documenti/`: note-ponte che fanno vedere i documenti delle altre repo nei grafi di Foam e Obsidian;
- `_grafo/index.html`: grafo interattivo con ricerca e filtri, aperto in automatico nel Codespace;
- `_grafo/indice.jsonl` e `_grafo/indice.md`: mappa compatta per le ricerche (e per Claude);
- `_grafo/revisione.md`: manutenzione (inbox da smistare, note da creare, revisioni in scadenza, link rotti);
- `_grafo/suggerimenti.md`: termini frequenti che possono diventare concetti.

Come far entrare le repo private e altre regolazioni: [collegare le repo al grafo](../40-procedure/collegare-le-repo-al-grafo.md).

## Strumenti

| Dove | Strumento | Funzioni |
| --- | --- | --- |
| Ovunque, senza installare nulla | File **`grafo.md`** su github.com | Panoramica di repo e concetti, con una pagina per ciascuno |
| Browser (completo) | Codespaces + **Foam** | Wikilink, backlink, grafo di Foam e grafo interattivo del second brain, note giornaliere, modelli |
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
