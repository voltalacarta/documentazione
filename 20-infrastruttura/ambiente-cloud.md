---
titolo: Ambiente di sviluppo cloud
stato: bozza
creato: 2026-10-15
aggiornato: 2026-10-15
tag: [infrastruttura, codespaces, cloud]
collegati: [0003]
---

# Ambiente di sviluppo cloud

Decisione di riferimento: [0003 · Ambiente di sviluppo solo cloud](../10-decisioni/0003-ambiente-di-sviluppo-solo-cloud.md).

> **Stato:** bozza. L'ambiente è deciso ma non ancora configurato. Questo documento verrà completato durante la messa in opera.

## Componenti

| Componente | A cosa serve | Come si apre |
| --- | --- | --- |
| **GitHub Codespaces** | Sviluppo completo: editor, terminale, debugger, estensioni | Repository → *Code* → *Codespaces* → *Create* |
| **github.dev** | Modifiche veloci, senza terminale, gratuito | Tasto `.` su un repository |
| **Claude** | Compiti delegati portati avanti nel cloud fino alla PR | claude.ai |
| **GitHub Actions** | Test e rilascio automatici | File in `.github/workflows/` |

## Dev container

Ogni repository di codice contiene `.devcontainer/devcontainer.json`, che descrive linguaggi, strumenti ed estensioni. Così l'ambiente è uguale ogni volta.

Esempio di base (da adattare allo stack, ancora da definire):

```json
{
  "name": "progetto",
  "image": "mcr.microsoft.com/devcontainers/base:ubuntu",
  "features": {
    "ghcr.io/devcontainers/features/node:1": {},
    "ghcr.io/devcontainers/features/python:1": {}
  },
  "customizations": {
    "vscode": {
      "extensions": ["editorconfig.editorconfig", "davidanson.vscode-markdownlint"]
    }
  }
}
```

## Dotfiles

Un repository `dotfiles` con alias, configurazione del terminale e di Git. Si attiva da **GitHub → Settings → Codespaces → Dotfiles**, e viene applicato automaticamente a ogni nuovo Codespace.

## Controllo dei costi

Le impostazioni si trovano in **GitHub → Settings → Codespaces** e **Settings → Billing**.

| Impostazione | Valore consigliato | Perché |
| --- | --- | --- |
| Limite di spesa Codespaces | **0 €** | Finita la quota gratuita si ferma, senza addebiti |
| Timeout di inattività | **30 minuti** | Non consuma ore quando non si usa |
| Conservazione Codespace inattivi | **pochi giorni** (es. 7) | Libera spazio di archiviazione |
| Tipo di macchina | 2 core | Sufficiente per la maggior parte del lavoro |

La quota gratuita per gli account personali è indicata da GitHub nella pagina di billing; i valori possono cambiare, quindi vanno verificati lì.

## Da completare

- [ ] Definire lo stack (linguaggi e strumenti) dei progetti di codice
- [ ] Creare il repository `dotfiles`
- [ ] Applicare le impostazioni di costo
- [ ] Scrivere la procedura "Aprire e usare un Codespace" in `40-procedure/`
