---
titolo: NIS2 in Italia (D.Lgs. 138/2024)
stato: attivo
creato: 2026-10-15
aggiornato: 2026-10-16
tag: [sicurezza-web, normativa-ue]
prossima_revisione: 2026-12-15
---

# NIS2 in Italia

> ⚠️ Sintesi orientativa, non consulenza legale. Le scadenze dipendono dalla data di comunicazione dell'inserimento nell'elenco NIS: verificare sul portale ACN.
>
> **In sintesi.** La Direttiva (UE) 2022/2555 è recepita con il **D.Lgs. 138/2024** e attuata dall'**ACN** (Agenzia per la Cybersicurezza Nazionale). Il 2026 è l'anno in cui si passa dalla registrazione alla **dimostrazione** delle misure. Per chi è nell'elenco dal 2025, la scadenza delle misure di base è il **31 ottobre 2026** — tra pochi giorni rispetto alla data di questo documento.

## Si applica a me?

Riguarda i soggetti **essenziali** e **importanti** dei settori elencati dal decreto (energia, trasporti, sanità, digitale, servizi ICT gestiti, fornitori di servizi digitali come marketplace e motori di ricerca, manifattura di alcuni settori, ecc.), in genere sopra le soglie di media impresa, con eccezioni. Un sito web aziendale non rende di per sé soggetti NIS2, ma **se l'organizzazione lo è, il sito rientra nel perimetro** delle misure.

Anche chi non è soggetto NIS2 può esserne toccato come **fornitore**: i soggetti NIS2 devono gestire la sicurezza della propria catena di approvvigionamento e lo chiederanno ai fornitori.

## Calendario 2026

| Data | Adempimento |
|---|---|
| 1 gen – 28 feb 2026 | Finestra annuale di registrazione/aggiornamento sul portale ACN |
| dal 15 gen 2026 | Pienamente operativo l'obbligo di **notifica degli incidenti significativi** al CSIRT Italia (Determinazione ACN 379907/2025) |
| entro 30 giu 2026 | **Categorizzazione** di attività e servizi (Determinazione ACN 155238/2026): 10 macro-aree, 4 livelli di rilevanza |
| entro **31 ott 2026** | **Misure di sicurezza di base** implementate e documentate (18 mesi dalla comunicazione, per chi è in elenco dalla primavera 2025) |
| da ottobre 2026 | ACN può avviare le **attività ispettive** |

## Le misure di base

La Determinazione ACN 379907/2025 ha quattro allegati:

- **Allegato 1** — soggetti importanti: 37 misure, 87 requisiti;
- **Allegato 2** — soggetti essenziali: 43 misure, 116 requisiti;
- **Allegati 3 e 4** — criteri degli incidenti significativi per le due categorie.

Le misure coprono governance, gestione del rischio, gestione degli asset, controllo accessi, sicurezza della supply chain, gestione delle vulnerabilità, continuità operativa, gestione e notifica degli incidenti, formazione.

## Ricadute pratiche per il sito web

| Misura NIS2 | Dove in questa base |
|---|---|
| Inventario degli asset | [dipendenze](../06-supply-chain/dipendenze.md) (SBOM), [owasp-api-top10](../07-api/owasp-api-top10.md) (API9) |
| Controllo accessi e MFA | [01-autenticazione](../01-autenticazione/mfa-e-recupero-account.md), [controllo-accessi](../02-autorizzazione/controllo-accessi.md) |
| Gestione vulnerabilità | [dipendenze](../06-supply-chain/dipendenze.md), [testing-di-sicurezza](../11-sdlc/testing-di-sicurezza.md) |
| Supply chain | [06-supply-chain](../06-supply-chain/ci-cd.md), [cms-e-hosting](../09-infrastruttura/cms-e-hosting.md) |
| Crittografia | [05-crittografia](../05-crittografia/tls-e-hsts.md) |
| Logging e incidenti | [logging-e-alert](../10-operazioni/logging-e-alert.md), [incident-response](../10-operazioni/incident-response.md) |
| Continuità | [backup-e-continuita](../10-operazioni/backup-e-continuita.md) |

## Governance

- Gli **organi di amministrazione** approvano le misure, ne sorvegliano l'attuazione, rispondono delle violazioni e devono seguire formazione in materia di sicurezza.
- Servono **evidenze documentali**: delibere con data e verbale, politiche, registri, report di test.

## Notifica degli incidenti

Preallarme al CSIRT Italia entro **24 ore**, notifica entro **72 ore**, relazione finale entro un mese. Vedi [incident-response](../10-operazioni/incident-response.md).

## Fonti

- [ECNEWS-NIS2], [PILLITTERI-NIS2], [ICTSEC-NIS2], [ICTSEC-NIS2-MAPPA], [TOMSHW-NIS2], [NOZE-NIS2], [CERTIFICO-VADEMECUM] — vedi [fonti.md](../fonti.md)
