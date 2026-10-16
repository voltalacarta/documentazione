---
titolo: Risposta agli incidenti
stato: attivo
creato: 2026-10-15
aggiornato: 2026-10-16
tag: [sicurezza-web, operazioni]
prossima_revisione: 2027-01-15
---

# Risposta agli incidenti

> **In sintesi.** Il piano si scrive prima dell'incidente. Con NIS2, GDPR e Cyber Resilience Act le scadenze di notifica sono nell'ordine delle **24–72 ore**: non c'è tempo di improvvisare chi fa cosa.

## Fasi (modello NIST SP 800-61)

1. **Preparazione** — ruoli, contatti, strumenti, accessi d'emergenza, log disponibili.
2. **Rilevamento e analisi** — conferma dell'incidente, perimetro, gravità.
3. **Contenimento** — isolare, revocare credenziali, bloccare il vettore.
4. **Eradicazione e ripristino** — rimozione della causa, ripristino da backup puliti, monitoraggio rafforzato.
5. **Lezioni apprese** — post-mortem senza colpe, azioni correttive tracciate.

## Contenuto minimo del piano

- 🔴 **Rubrica**: responsabile dell'incidente, tecnici, hosting/CDN, legale, DPO, comunicazione, assicurazione cyber.
- 🔴 **Matrice delle notifiche obbligatorie**:

  | Norma | A chi | Termine | Quando |
  |---|---|---|---|
  | GDPR art. 33 | Garante Privacy | **72 ore** | Violazione di dati personali con rischio per gli interessati |
  | GDPR art. 34 | Interessati | Senza ingiustificato ritardo | Rischio elevato |
  | NIS2 (D.Lgs. 138/2024) | CSIRT Italia | **Preallarme 24 h**, notifica 72 h, relazione finale entro 1 mese | Soggetti NIS, incidente significativo |
  | Cyber Resilience Act art. 14 | ENISA + CSIRT tramite Single Reporting Platform | **Preallarme 24 h** | Fabbricanti: vulnerabilità sfruttate e incidenti gravi |

  Dettagli: [gdpr](../12-normativa-ue/gdpr.md), [nis2-italia](../12-normativa-ue/nis2-italia.md), [cyber-resilience-act](../12-normativa-ue/cyber-resilience-act.md).
- 🔴 **Runbook** per gli scenari più probabili: sito defacciato, account admin compromesso, segreto esposto, dipendenza malevola, data breach, ransomware, DDoS.
- 🟠 Procedura di **conservazione delle prove** (log, snapshot) prima di ripulire.
- 🟠 Modelli di comunicazione per utenti e stampa.

## Primi 60 minuti (promemoria)

1. Apri un canale dedicato e un registro temporale degli eventi.
2. Valuta se far scattare le notifiche normative (avvia il conteggio).
3. Contieni: revoca sessioni e token, ruota i segreti coinvolti, metti in manutenzione se necessario.
4. Preserva le prove.
5. Informa i responsabili e, se previsto, l'assicurazione.

## Esercitazioni

- 🟠 Almeno una *tabletop exercise* all'anno su uno scenario realistico.

## Fonti

- [PILLITTERI-CRA], [AGENDADIG-CRA], [ECNEWS-NIS2] — vedi [fonti.md](../fonti.md)
