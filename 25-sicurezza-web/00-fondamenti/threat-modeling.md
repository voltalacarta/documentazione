---
titolo: Threat modeling
stato: attivo
creato: 2026-10-15
aggiornato: 2026-10-16
tag: [sicurezza-web, fondamenti]
prossima_revisione: 2027-10-15
owasp: [A06:2025]
---

# Threat modeling

> **In sintesi.** È il modo più economico di prevenire la categoria A06 *Insecure Design*: ragionare sugli attacchi prima di scrivere codice costa ore, correggere un difetto di progettazione in produzione costa settimane.

## Le quattro domande (approccio di Shostack)

1. **Cosa stiamo costruendo?** — diagramma dei flussi di dati con confini di fiducia.
2. **Cosa può andare storto?** — elenco delle minacce.
3. **Cosa facciamo al riguardo?** — contromisure, accettazioni, trasferimenti del rischio.
4. **Abbiamo fatto un buon lavoro?** — revisione e verifica.

## STRIDE come promemoria

| Minaccia | Proprietà violata | Esempio web | Contromisura tipica |
|---|---|---|---|
| **S**poofing | Autenticazione | Furto di sessione, phishing | [Passkey](../01-autenticazione/passkey-webauthn.md), cookie sicuri |
| **T**ampering | Integrità | Modifica del prezzo nel carrello | Validazione lato server, firme |
| **R**epudiation | Non ripudio | "Non ho fatto io quell'ordine" | [Log di audit](../10-operazioni/logging-e-alert.md) |
| **I**nformation disclosure | Riservatezza | IDOR, stack trace esposti | [Controllo accessi](../02-autorizzazione/controllo-accessi.md) |
| **D**enial of service | Disponibilità | Flood sul login | [Rate limiting](../09-infrastruttura/waf-rate-limiting-bot.md) |
| **E**levation of privilege | Autorizzazione | Utente che diventa admin | Controllo dei ruoli lato server |

## Pratiche

- 🔴 Fai una sessione di threat modeling all'avvio del progetto e a ogni nuova funzionalità sensibile (pagamenti, upload, ruoli, integrazioni AI).
- 🟠 Includi esplicitamente i **flussi di business abusabili** (coupon, registrazioni, prenotazioni): sono un rischio specifico dell'[OWASP API Top 10](../07-api/owasp-api-top10.md) (API6).
- 🟠 Considera la **supply chain** come attore: dipendenze, CDN, script di terze parti, fornitori SaaS.
- 🟠 Se integri un LLM, tratta ogni contenuto che il modello legge come potenzialmente ostile (vedi [owasp-llm-top10](../08-ai-llm/owasp-llm-top10.md)).
- 🟢 Mantieni il modello come file versionato accanto al codice e aggiornalo nelle code review.

## Strumenti

- OWASP Threat Dragon (gratuito), Microsoft Threat Modeling Tool, oppure un semplice diagramma + tabella in questo repository.

## Fonti

- [RADWARE-21BP] — vedi [fonti.md](../fonti.md)
