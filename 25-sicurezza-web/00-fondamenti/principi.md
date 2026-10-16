---
titolo: Principi di progettazione sicura
stato: attivo
creato: 2026-10-15
aggiornato: 2026-10-16
tag: [sicurezza-web, fondamenti]
prossima_revisione: 2027-10-15
owasp: [A06:2025]
---

# Principi di progettazione sicura

> **In sintesi.** Le tecniche cambiano ogni anno; questi principi no. Ogni decisione tecnica degli altri file ne è un'applicazione.

## I principi

| Principio | Significato pratico |
|---|---|
| **Difesa in profondità** | Nessun controllo è l'unico: validazione input + query parametrizzate + CSP + WAF. Se uno cede, gli altri reggono. |
| **Minimo privilegio** | Utenti, servizi, token CI, account database hanno solo i permessi indispensabili, per il tempo indispensabile. |
| **Nega per default** | Ogni route, risorsa o azione è vietata finché non viene esplicitamente permessa. |
| **Secure by default** | La configurazione di fabbrica è quella sicura; l'insicurezza richiede un'azione deliberata e documentata. |
| **Fallire in modo sicuro** | Se un controllo va in errore, l'esito è "accesso negato", non "accesso consentito". Vedi [gestione-errori](../10-operazioni/gestione-errori.md). |
| **Riduzione della superficie d'attacco** | Ciò che non esiste non si può attaccare: disattiva endpoint, plugin, porte e funzioni inutilizzate. |
| **Zero trust** | Nessuna richiesta è fidata per la sua provenienza (rete interna, altro microservizio): si autentica e autorizza sempre. |
| **Non fidarsi del client** | Tutto ciò che arriva dal browser (campi nascosti, prezzi, ruoli, ID) è manipolabile. I controlli stanno sul server. |
| **Separazione dei compiti** | Chi scrive il codice non è l'unico ad approvarlo; chi deploya non gestisce da solo i segreti. |
| **Semplicità** | Un'architettura complessa ha più punti ciechi. Preferisci componenti standard e collaudati a soluzioni artigianali, soprattutto in crittografia e autenticazione. |
| **Privacy by design** | Raccogli solo i dati necessari, conservali il minimo indispensabile (vedi [GDPR](../12-normativa-ue/gdpr.md)). |

## Applicarli concretamente

- 🔴 Documenta per ogni progetto: dati trattati, attori, confini di fiducia. È l'input del [threat modeling](threat-modeling.md).
- 🔴 Usa framework maturi che applicano già molti principi (escape automatico, protezione CSRF, ORM).
- 🟠 Registra le **decisioni di sicurezza** (es. "accettiamo X perché Y"): ASVS 5.0 lo richiede esplicitamente. Vedi [owasp-asvs-5](owasp-asvs-5.md).
- 🟠 Riesamina i principi a ogni cambio architetturale importante (nuova API pubblica, integrazione AI, nuovo fornitore).

## Vedi anche

- [owasp-top10-2025](owasp-top10-2025.md)
- [threat-modeling](threat-modeling.md)
