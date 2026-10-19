---
titolo: GitHub
stato: attivo
creato: 2026-10-15
aggiornato: 2026-10-19
tag: [infrastruttura, github]
sintesi: "Account, repository, convenzioni"
collegati: [0002]
---

# GitHub

Decisione di riferimento: [0002 · GitHub come base unica di lavoro](../10-decisioni/0002-github-come-base-di-lavoro.md).

## Account

- Account/organizzazione: [`voltalacarta`](https://github.com/voltalacarta)

## Repository

| Repository | Scopo | Visibilità | Stato |
| --- | --- | --- | --- |
| [`documentazione`](https://github.com/voltalacarta/documentazione) | Documentazione generale e decisioni | **pubblico** (da valutare) | attivo |
| [`second-brain`](https://github.com/voltalacarta/second-brain) | Note personali (vedi [0004](../10-decisioni/0004-second-brain-markdown-su-github.md)) | **privato** | attivo |
| `rt2` | Da definire (trovata dalla scoperta automatica, ancora vuota) | pubblico | vuota |
| `dotfiles` | Configurazioni personali per Codespaces | pubblico o privato | da creare |

L'elenco sempre aggiornato, con i contenuti di ogni repo, è nel [grafo del second brain](https://github.com/voltalacarta/second-brain/blob/main/grafo.md): ogni repo nuova vi compare da sola.

## Convenzioni per i repository

- Nomi in minuscolo con trattini: `nome-progetto`.
- Ogni repository ha un `README.md` che spiega scopo e uso.
- Ramo principale: `main`.
- Repository di codice: protezione di `main`, modifiche tramite pull request, Dependabot attivo.
- Repository di codice: `.devcontainer/devcontainer.json` per Codespaces (vedi [ambiente cloud](ambiente-cloud.md)).
- **Ogni progetto nuovo nasce dal modello** (indici automatici, decisioni, controlli, collegamento al grafo): vedi [nuovo progetto](../40-procedure/nuovo-progetto.md).

## Segreti delle Actions

| Segreto | Dove | A cosa serve |
| --- | --- | --- |
| `KG_TOKEN` | `second-brain` | Sola lettura su tutte le repo: fa entrare nel grafo anche le **private** |
| `KG_AVVISO` | Facoltativo, nelle altre repo | Scrittura solo su `second-brain`: dopo un push il grafo si aggiorna subito invece che entro 3 ore |

Come crearli: [collegare le repo al grafo](../40-procedure/collegare-le-repo-al-grafo.md).

## Integrazione con Claude

Claude accede ai repository autorizzati dalla sessione su claude.ai. L'accesso a GitHub si gestisce da **claude.ai → Impostazioni → Connettori**.
Nei repository dove Claude lavora conviene un file `CLAUDE.md` con le convenzioni del progetto (come quello di questo repository).
