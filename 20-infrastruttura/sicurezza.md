---
titolo: Sicurezza
stato: attivo
creato: 2026-10-15
aggiornato: 2026-10-16
tag: [infrastruttura, sicurezza, backup]
sintesi: "Accessi, segreti, backup"
collegati: [0002, 0003, 0004]
---

# Sicurezza

Questo documento riguarda l'**ambiente di lavoro** (account, segreti, backup). Per la sicurezza dei **siti e progetti digitali** vedi la sezione [Sicurezza web](../25-sicurezza-web/README.md).

## Accesso a GitHub

L'account GitHub dà accesso a tutto: va protetto per primo.

- [ ] Accesso con **passkey** o **autenticazione a due fattori (2FA)**
- [ ] Codici di recupero salvati nel password manager
- [ ] Revisione periodica delle app e dei token autorizzati (**Settings → Applications**)

## Segreti (token, chiavi API, password)

| Dove | Ammesso? |
| --- | --- |
| Codice o documentazione nel repository | ❌ Mai |
| File `.env` committato | ❌ Mai (bloccato dal `.gitignore`) |
| **Codespaces Secrets** (Settings → Codespaces → Secrets) | ✅ Per l'ambiente di sviluppo |
| **Actions Secrets** (repository → Settings → Secrets) | ✅ Per le automazioni |
| Password manager (es. Bitwarden, 1Password) | ✅ Per tutto ciò che è personale |

Se un segreto finisce per errore in un commit: **revocarlo subito** e generarne uno nuovo. Cancellarlo dal file non basta, resta nello storico di Git.

## Dati sensibili

Nessun dato personale sensibile (IBAN, documenti d'identità, dati sanitari, password) né in questo repository né nel second brain.

## Repository privati

- `second-brain`: sempre **privato**.
- Gli altri: valutare caso per caso e annotare la visibilità in [GitHub](github.md#repository).

## Backup

GitHub non è un backup: un errore o un problema di account può far perdere tutto.

- [ ] Copia automatica periodica (es. settimanale) dei repository importanti fuori da GitHub
- [ ] Verifica almeno trimestrale che il ripristino funzioni

Il metodo di backup è da decidere: quando sarà scelto, va registrato in `10-decisioni/` e descritto in `40-procedure/`.
