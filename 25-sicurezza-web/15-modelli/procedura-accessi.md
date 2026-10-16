---
titolo: Procedura di gestione degli accessi
stato: attivo
creato: 2026-10-15
aggiornato: 2026-10-16
tag: [sicurezza-web, modelli, modello]
---

# Procedura di gestione degli accessi

*[NOME ORGANIZZAZIONE] — versione [1.0] — [DATA]*

Si applica a dipendenti, collaboratori, agenzie e fornitori che accedono a domini, hosting, CMS, repository, caselle email, social e strumenti SaaS. Il registro di riferimento è [registro-asset-e-accessi.csv](registro-asset-e-accessi.csv).

## Regole generali

1. **Un account per persona.** Nessuna credenziale condivisa. Dove un servizio non lo consente, la credenziale sta in un password manager condiviso con accesso tracciato.
2. **MFA obbligatoria** su ogni account che lo consente; passkey o chiave di sicurezza per gli amministratori.
3. **Minimo privilegio.** Il ruolo assegnato è il più basso sufficiente per il lavoro.
4. **Proprietà in capo all'organizzazione.** Domini, hosting, account di analytics, social e repository sono intestati all'organizzazione, non a persone o agenzie. Le agenzie ricevono accessi delegati.
5. **Email di recupero aziendali**, non personali.
6. **Password manager** aziendale per tutti.

## Ingresso (onboarding)

- [ ] Richiesta approvata da [RESPONSABILE] con elenco dei sistemi e ruoli necessari
- [ ] Account creati con ruolo minimo
- [ ] MFA attivata al primo accesso (verificata)
- [ ] Accesso al password manager
- [ ] Lettura delle [regole per chi lavora sul sito](../17-formazione/regole-per-redattori.md)
- [ ] Registro accessi aggiornato

## Cambio di ruolo

- [ ] Rimozione degli accessi non più necessari prima di aggiungere i nuovi
- [ ] Registro aggiornato

## Uscita (offboarding) — entro il giorno di cessazione

- [ ] Disattivazione degli account (non solo cambio password)
- [ ] Chiusura delle sessioni attive e revoca dei token/chiavi API personali
- [ ] Rimozione da repository, hosting, CMS, social, gruppi email
- [ ] Rotazione delle credenziali condivise che conosceva
- [ ] Trasferimento della proprietà di file e risorse
- [ ] Rimozione delle passkey/dispositivi registrati sugli account aziendali
- [ ] Registro aggiornato con data e chi ha eseguito

## Revisione periodica

Ogni **trimestre** [RESPONSABILE] verifica il registro e rimuove gli accessi non più giustificati (vedi [revisione-periodica](../checklist/revisione-periodica.md)).
