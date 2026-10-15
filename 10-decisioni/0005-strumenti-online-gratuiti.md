---
titolo: Strumenti online gratuiti per editor e second brain
stato: accettato
creato: 2026-10-15
aggiornato: 2026-10-15
tag: [decisioni, codespaces, cloud-shell, foam, obsidian, costi]
collegati: [0003, 0004]
---

# 0005 · Strumenti online gratuiti per editor e second brain

## Contesto

Le decisioni [0003](0003-ambiente-di-sviluppo-solo-cloud.md) e [0004](0004-second-brain-markdown-su-github.md) fissano *dove* si lavora. Resta da stabilire *con quali strumenti*, con tre vincoli: **tutto online**, **tutto gratuito**, **durevole** (nessun dato perso se uno strumento cambia).

## Decisione

### Principio di durabilità

**GitHub è l'unico posto dove i dati vivono.** Editor e ambienti sono usa-e-getta: si possono cancellare e ricreare in qualsiasi momento senza perdere nulla, purché si faccia commit e push a fine sessione.

### Editor

| Ruolo | Strumento | Terminale | Limite gratuito |
| --- | --- | --- | --- |
| **Principale** | GitHub Codespaces, macchina 2 core | ✅ | 120 ore di calcolo e 15 GB-mese al mese (piano Free); su 2 core equivalgono a circa 60 ore reali |
| **Rapido** | github.dev (tasto `.`) | ❌ | Nessuno |
| **Riserva** | Google Cloud Shell (editor + terminale) | ✅ | 50 ore a settimana, 5 GB persistenti |

**Nessun metodo di pagamento** collegato a GitHub per Codespaces: finita la quota, l'uso si blocca invece di generare addebiti.

### "Obsidian online"

| Dove | Strumento |
| --- | --- |
| Browser | Repository `second-brain` + estensione **Foam** in Codespaces (completo) o github.dev |
| Telefono | App **Obsidian** + plugin comunitario **Git** (gratuiti) |

Il vault è configurato per entrambi: stesse cartelle, stessi modelli, stesse note giornaliere.

## Alternative considerate

| Alternativa | Perché scartata |
| --- | --- |
| Obsidian Sync / Publish | A pagamento |
| Gitpod | Offerta cambiata più volte, futuro gratuito incerto |
| Server personale con code-server (es. VM gratuita) | Più manutenzione e sicurezza a carico nostro |
| Pubblicare il vault come sito (Quartz su GitHub Pages) | Pages su repository privati richiede un piano a pagamento: le note diventerebbero pubbliche |

## Conseguenze

- ✅ Costo zero.
- ✅ Nessun lock-in: se uno strumento sparisce, si apre lo stesso repository con un altro.
- ✅ Due ambienti con terminale indipendenti (GitHub e Google).
- ⚠️ Le modifiche non pubblicate con push si perdono quando un Codespace viene cancellato.
- ⚠️ Cloud Shell cancella la cartella personale dopo 120 giorni di inutilizzo: i dati vanno sempre su GitHub.
- ⚠️ I limiti gratuiti possono cambiare: ricontrollarli ogni anno.

## Dettagli

- [Ambiente cloud](../20-infrastruttura/ambiente-cloud.md)
- [Lavorare online](../40-procedure/lavorare-online.md)
- [Usare il second brain](../40-procedure/usare-il-second-brain.md)
