---
titolo: GDPR — obblighi di sicurezza per i siti web
stato: attivo
creato: 2026-10-15
aggiornato: 2026-10-16
tag: [sicurezza-web, normativa-ue]
prossima_revisione: 2027-01-15
---

# GDPR — obblighi di sicurezza per i siti web

> ⚠️ Sintesi orientativa, non consulenza legale. Verificare con il proprio DPO o legale.
>
> **In sintesi.** Il Regolamento (UE) 2016/679 si applica a quasi tutti i siti (form di contatto, account, analytics, newsletter). Non impone tecnologie specifiche, ma misure "adeguate al rischio" e la capacità di dimostrarle.

## Articoli rilevanti per la sicurezza

| Articolo | Contenuto | Ricaduta tecnica |
|---|---|---|
| Art. 5 | Principi: minimizzazione, limitazione della conservazione, integrità e riservatezza | Raccogli il minimo, cancella quando non serve |
| Art. 25 | Protezione dei dati fin dalla progettazione e per impostazione predefinita | Privacy by design nei requisiti |
| Art. 28 | Responsabili del trattamento | Contratti (DPA) con hosting, CDN, SaaS, fornitori AI |
| Art. 30 | Registro dei trattamenti | Inventario di dati, finalità, fornitori |
| Art. 32 | Sicurezza del trattamento | Pseudonimizzazione, cifratura, riservatezza, integrità, disponibilità, resilienza, ripristino, test periodici |
| Art. 33 | Notifica al Garante | **Entro 72 ore** dalla scoperta della violazione |
| Art. 34 | Comunicazione agli interessati | Se il rischio è elevato |
| Art. 35 | Valutazione d'impatto (DPIA) | Per trattamenti ad alto rischio |
| Art. 44 e ss. | Trasferimenti extra UE | Attenzione a CDN, analytics, servizi AI con server fuori UE |

## Pratiche per il sito

- 🔴 HTTPS ovunque, cifratura dei backup, controllo degli accessi: sono l'attuazione minima dell'art. 32.
- 🔴 **Registro delle violazioni** (anche di quelle non notificate) e procedura per le 72 ore: vedi [incident-response](../10-operazioni/incident-response.md).
- 🔴 Banner e gestione del **consenso** per cookie e tracker non tecnici (disciplina ePrivacy e linee guida del Garante): nessun tracker caricato prima del consenso.
- 🟠 Conservazione dei log e dei dati con termini definiti e cancellazione automatica.
- 🟠 Pseudonimizzazione degli IP nei log e negli analytics dove possibile.
- 🟠 Inventario degli script di terze parti: ognuno è potenzialmente un trasferimento di dati.
- 🟠 Integrazioni AI: verifica dove vengono trattati i dati inviati ai modelli e se vengono usati per l'addestramento.

## Fonti

- Testo del Regolamento (UE) 2016/679; Garante per la protezione dei dati personali — vedi [fonti.md](../fonti.md)
