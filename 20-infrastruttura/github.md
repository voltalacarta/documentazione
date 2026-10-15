---
titolo: GitHub
stato: attivo
creato: 2026-10-15
aggiornato: 2026-10-15
tag: [infrastruttura, github]
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
| `dotfiles` | Configurazioni personali per Codespaces | pubblico o privato | da creare |

Aggiorna questa tabella ogni volta che si crea, rinomina o archivia un repository.

## Convenzioni per i repository

- Nomi in minuscolo con trattini: `nome-progetto`.
- Ogni repository ha un `README.md` che spiega scopo e uso.
- Ramo principale: `main`.
- Repository di codice: protezione di `main`, modifiche tramite pull request, Dependabot attivo.
- Repository di codice: `.devcontainer/devcontainer.json` per Codespaces (vedi [ambiente cloud](ambiente-cloud.md)).

## Integrazione con Claude

Claude accede ai repository autorizzati dalla sessione su claude.ai. L'accesso a GitHub si gestisce da **claude.ai → Impostazioni → Connettori**.
Nei repository dove Claude lavora conviene un file `CLAUDE.md` con le convenzioni del progetto (come quello di questo repository).
