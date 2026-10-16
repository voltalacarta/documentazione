---
titolo: Cyber Resilience Act (Reg. UE 2024/2847)
stato: attivo
creato: 2026-10-15
aggiornato: 2026-10-16
tag: [sicurezza-web, normativa-ue]
prossima_revisione: 2027-01-15
---

# Cyber Resilience Act (CRA)

> ⚠️ Sintesi orientativa, non consulenza legale. L'ambito di applicazione a software e servizi va valutato caso per caso con le linee guida della Commissione.
>
> **In sintesi.** Il CRA è il primo regolamento UE orizzontale con requisiti di sicurezza obbligatori per i **prodotti con elementi digitali** (hardware e software) immessi sul mercato UE. In vigore dal 10 dicembre 2024; il primo obbligo operativo — la **segnalazione** — è scattato l'**11 settembre 2026**.

## Riguarda un sito web?

- **Sito o servizio SaaS puro**: il CRA riguarda i *prodotti*. Un servizio online rientra solo come **soluzione di elaborazione dati remota (RDPS)** di un prodotto. Le linee guida della Commissione (bozza di marzo 2026, poi Comunicazione C(2026) 5252 del 27 luglio 2026) valutano tre criteri:
  1. la funzione remota è **parte integrante** del prodotto?
  2. il prodotto **dipende** da quella funzione per funzionare?
  3. il software remoto è sviluppato **dal fabbricante** o sotto la sua responsabilità?

  Se le risposte sono sì, la parte remota segue gli obblighi del prodotto (es. il cloud di un'app o di un dispositivo connesso). Un sito editoriale o un e-commerce non legato a un prodotto distribuito, di norma, no. Le linee guida non sono vincolanti: nei casi dubbi serve una valutazione legale.
- **Software distribuito** (plugin, temi, app, librerie commerciali, app mobile, firmware, agent installabili): rientra.
- **Open source**: obblighi ridotti per gli *steward*, ma con un perimetro analogo per le segnalazioni quando sono coinvolti nello sviluppo dei prodotti.

Chi sviluppa siti per clienti e distribuisce anche plugin o componenti software deve verificare la propria posizione come **fabbricante**.

## Calendario

| Data | Fase |
|---|---|
| 10 dic 2024 | Entrata in vigore |
| 11 giu 2026 | Disposizioni sugli organismi notificati |
| **11 set 2026** | **Art. 14 — obblighi di segnalazione** dei fabbricanti; avvio della Single Reporting Platform di ENISA |
| 11 dic 2027 | Applicazione completa: requisiti essenziali (Allegato I), gestione delle vulnerabilità, marcatura CE |

## Obblighi di segnalazione (art. 14)

Il fabbricante deve segnalare, tramite la **Single Reporting Platform** gestita da ENISA, a ENISA e al CSIRT nazionale designato:

- le **vulnerabilità attivamente sfruttate** presenti nei suoi prodotti;
- gli **incidenti gravi** che incidono sulla sicurezza del prodotto.

| Fase | Termine |
|---|---|
| Preallarme | **24 ore** dalla conoscenza |
| Notifica | 72 ore |
| Rapporto finale | 14 giorni dalla disponibilità della misura correttiva (vulnerabilità) / 1 mese (incidenti gravi) |

Vale anche per i prodotti **già sul mercato**. Le sanzioni previste dal regolamento arrivano fino a 15 milioni di euro (o percentuale del fatturato, secondo la violazione).

Osservazione critica ricorrente: tra settembre 2026 e dicembre 2027 la norma richiede il risultato (notificare in 24 ore) prima di imporre formalmente i mezzi (processi di gestione delle vulnerabilità dell'Allegato I, Parte II). In pratica, conviene costruire quei processi subito.

## Cosa preparare ora

- 🔴 Processo interno definito: chi riceve una segnalazione, chi decide che va notificata, chi compila e invia sulla piattaforma.
- 🔴 Canale di ricezione delle vulnerabilità ([vulnerability-disclosure](../10-operazioni/vulnerability-disclosure.md)).
- 🟠 Monitoraggio delle vulnerabilità e **SBOM** dei prodotti ([dipendenze](../06-supply-chain/dipendenze.md)).
- 🟠 Supporto di sicurezza con durata dichiarata e aggiornamenti distribuiti in modo sicuro ([ci-cd](../06-supply-chain/ci-cd.md)).
- 🟢 Roadmap verso i requisiti essenziali del 2027 (secure by default, protezione dei dati, minimizzazione della superficie d'attacco).

## Fonti

- [DLAPIPER-CRA], [PILLITTERI-CRA], [AGENDADIG-CRA], [AGENDADIG-CRA2], [CS360-CRA], [NAMIRIAL-CRA], [ICTSEC-CRA], [ICTSEC-CRA-RISCHIO], [CERTIFICO-CRA], [PRESENCIS-CRA] — vedi [fonti.md](../fonti.md)
