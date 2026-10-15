---
titolo: Ambiente di sviluppo solo cloud con GitHub Codespaces
stato: accettato
creato: 2026-10-15
aggiornato: 2026-10-15
tag: [decisioni, codespaces, cloud, sviluppo]
collegati: [0002]
---

# 0003 · Ambiente di sviluppo solo cloud con GitHub Codespaces

## Contesto

Non si vuole usare il computer locale per lo sviluppo: tutto deve funzionare nel cloud, dal browser, da qualsiasi dispositivo.

## Decisione

| Ruolo | Strumento |
| --- | --- |
| Ambiente principale | **GitHub Codespaces** (VS Code completo nel browser, con terminale) |
| Modifiche rapide | **github.dev** (tasto `.` su un repository) |
| Lavoro delegato | **Claude** nel cloud, fino alla pull request |
| Test e rilascio | **GitHub Actions** |

- Ogni repository di codice contiene un `.devcontainer/devcontainer.json` che rende l'ambiente riproducibile.
- Le preferenze personali stanno in un repository `dotfiles`, applicato automaticamente a ogni Codespace.

## Alternative considerate

| Alternativa | Perché scartata |
| --- | --- |
| Sviluppo locale | Esplicitamente escluso |
| Gitpod / altri IDE cloud | Validi, ma Codespaces è integrato in GitHub, già scelto come base |
| Server virtuale personale | Più manutenzione, nessun vantaggio per l'uso attuale |

## Conseguenze

- ✅ Nessuna dipendenza dal computer locale.
- ✅ Ambiente identico ogni volta, ricreabile in pochi minuti.
- ⚠️ Quota gratuita limitata: va impostato un limite di spesa (vedi [ambiente cloud](../20-infrastruttura/ambiente-cloud.md#controllo-dei-costi)).
- ⚠️ Serve connessione internet.

## Dettagli

- [Ambiente cloud](../20-infrastruttura/ambiente-cloud.md)
