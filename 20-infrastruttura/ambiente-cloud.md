---
titolo: Ambiente di sviluppo cloud
stato: attivo
creato: 2026-10-15
aggiornato: 2026-10-15
tag: [infrastruttura, codespaces, cloud-shell, cloud]
sintesi: "Codespaces, github.dev, Cloud Shell, costi"
collegati: [0003, 0005]
---

# Ambiente di sviluppo cloud

Decisioni di riferimento: [0003 · Sviluppo solo cloud](../10-decisioni/0003-ambiente-di-sviluppo-solo-cloud.md) e [0005 · Strumenti online gratuiti](../10-decisioni/0005-strumenti-online-gratuiti.md).

## Principio

**I dati vivono solo su GitHub.** Ogni editor è sostituibile. A fine sessione: commit e push.

## Componenti

| Componente | A cosa serve | Terminale | Come si apre |
| --- | --- | --- | --- |
| **GitHub Codespaces** | Lavoro completo: editor, terminale, estensioni | ✅ | Repository → *Code* → *Codespaces* → *Create codespace on main* |
| **github.dev** | Modifiche veloci | ❌ | Tasto `.` su un repository |
| **Google Cloud Shell** | Riserva gratuita con terminale | ✅ | [shell.cloud.google.com](https://shell.cloud.google.com) |
| **Claude** | Compiti delegati, fino a commit o PR | — | claude.ai |
| **GitHub Actions** | Controlli automatici | — | File in `.github/workflows/` |

Procedura d'uso: [Lavorare online](../40-procedure/lavorare-online.md).

## Dev container

Ogni repository ha `.devcontainer/devcontainer.json`, che descrive l'ambiente di Codespaces: immagine, strumenti, estensioni. Così ogni Codespace nasce identico.

| Repository | Ambiente |
| --- | --- |
| `documentazione` | Node 20 + markdownlint |
| `second-brain` | Ubuntu base + Foam |

I repository di codice avranno il loro quando sarà definito lo stack.

## Dotfiles

Un repository `dotfiles` (alias, terminale, Git) applicato automaticamente a ogni Codespace. Si attiva da **GitHub → Settings → Codespaces → Dotfiles**. Da creare.

## Controllo dei costi

### Limiti gratuiti (verificati il 2026-10-15)

| Servizio | Quota gratuita |
| --- | --- |
| Codespaces (piano Free) | 120 ore di calcolo e 15 GB-mese al mese. Le macchine più grandi consumano in proporzione ai core: su 2 core ≈ 60 ore reali |
| Codespaces (piano Pro) | 180 ore di calcolo e 20 GB-mese al mese |
| Cloud Shell | 50 ore a settimana, 5 GB in `$HOME`, sessioni fino a 12 ore |

### Impostazioni consigliate

In **GitHub → Settings → Codespaces** e **Settings → Billing**:

| Impostazione | Valore | Perché |
| --- | --- | --- |
| Metodo di pagamento | **nessuno** | Finita la quota l'uso si blocca, senza addebiti |
| Timeout di inattività | **30 minuti** | Non consuma ore quando non si usa |
| Conservazione Codespace inattivi | **7 giorni** | Libera spazio di archiviazione |
| Tipo di macchina | **2 core** | Il minimo, consuma meno quota |

### Attenzione

- Un Codespace cancellato perde le modifiche non inviate con push.
- Cloud Shell cancella `$HOME` dopo 120 giorni senza accessi (con avviso via email).

## Da completare

- [ ] Applicare le impostazioni di costo
- [ ] Creare il repository `dotfiles`
- [ ] Definire lo stack dei progetti di codice
