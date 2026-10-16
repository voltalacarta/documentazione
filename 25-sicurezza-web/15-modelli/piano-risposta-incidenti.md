---
titolo: Piano di risposta agli incidenti di sicurezza
stato: attivo
creato: 2026-10-15
aggiornato: 2026-10-16
tag: [sicurezza-web, modelli, modello]
---

# Piano di risposta agli incidenti di sicurezza

*[NOME ORGANIZZAZIONE] — versione [1.0] — approvato da [CHI] il [DATA] — prossima revisione [DATA + 12 mesi]*

Riferimenti: [incident-response](../10-operazioni/incident-response.md), [gdpr](../12-normativa-ue/gdpr.md), [nis2-italia](../12-normativa-ue/nis2-italia.md), [cyber-resilience-act](../12-normativa-ue/cyber-resilience-act.md).

## 1. Ruoli e contatti

| Ruolo | Nome | Telefono | Email | Sostituto |
|---|---|---|---|---|
| Responsabile dell'incidente | | | | |
| Referente tecnico (sviluppo) | | | | |
| Hosting / sistemista | | | | |
| DPO / referente privacy | | | | |
| Legale | | | | |
| Comunicazione | | | | |
| Direzione (decisioni e notifiche) | | | | |

## 2. Contatti esterni

| Soggetto | Contatto | Note |
|---|---|---|
| Supporto hosting | | numero d'emergenza, numero contratto |
| CDN / WAF | | |
| Registrar del dominio | | |
| Agenzia/sviluppatore esterno | | |
| Assicurazione cyber | | numero polizza, obbligo di preavviso |
| Garante Privacy | servizi online del Garante (notifica data breach) | entro 72 h |
| CSIRT Italia | portale ACN / csirt.gov.it | solo se soggetto NIS2 |
| Polizia Postale | commissariatodips.it | in caso di reato (es. estorsione) |

## 3. Classificazione

| Gravità | Esempi | Chi attivare | Tempo di risposta |
|---|---|---|---|
| **Critica** | Furto di dati personali, ransomware, sito usato per diffondere malware, account admin compromesso | Tutti i ruoli | Immediato |
| **Alta** | Defacement, segreto esposto pubblicamente, dipendenza malevola installata | Responsabile, tecnico, hosting | Entro 2 h |
| **Media** | Vulnerabilità segnalata non sfruttata, DDoS mitigato | Tecnico | Entro 1 giorno lavorativo |
| **Bassa** | Scansioni, tentativi di login falliti senza esito | Tecnico (monitoraggio) | Ordinario |

## 4. Decisione sulle notifiche (avviare il conteggio subito)

| Domanda | Se sì |
|---|---|
| Sono coinvolti dati personali con rischio per le persone? | Notifica al Garante **entro 72 h** (art. 33 GDPR) |
| Il rischio per le persone è elevato? | Comunicazione agli interessati (art. 34) |
| Siamo soggetti NIS2 ed è un incidente significativo? | Preallarme CSIRT Italia **entro 24 h**, notifica entro 72 h |
| Siamo fabbricanti di un prodotto digitale e la vulnerabilità è sfruttata? | Preallarme ENISA/CSIRT **entro 24 h** (CRA art. 14) |
| La polizza assicurativa richiede preavviso? | Avvisare la compagnia nei termini |

Ora di scoperta: `[AAAA-MM-GG hh:mm]` — Scadenza 24 h: `[...]` — Scadenza 72 h: `[...]`

## 5. Procedura

1. **Apri il registro**: canale dedicato (non quello eventualmente compromesso) e diario con orario di ogni azione.
2. **Valuta** gravità e perimetro; decidi sulle notifiche (sezione 4).
3. **Preserva le prove**: copia dei log, snapshot dei server, prima di modificare.
4. **Contieni**:
   - revoca sessioni e token, cambia password e chiavi coinvolte;
   - disattiva account compromessi;
   - metti il sito in manutenzione se necessario;
   - blocca IP/percorsi d'attacco sul WAF.
5. **Elimina la causa**: correggi la vulnerabilità, rimuovi malware/backdoor, aggiorna componenti.
6. **Ripristina** da backup verificati come puliti; monitoraggio rafforzato per [30] giorni.
7. **Comunica** secondo la sezione 4 e, se opportuno, pubblicamente.
8. **Analisi post-incidente** entro [10] giorni: cosa è successo, perché, cosa cambiamo. Aggiorna questo piano.

## 6. Runbook rapidi

### Segreto esposto (chiave API, password nel repository)

1. Ruota il segreto **subito** (cancellarlo dal repository non basta).
2. Controlla nei log del servizio se è stato usato.
3. Cerca altri segreti con Gitleaks su tutta la storia.

### Account amministratore compromesso

1. Disattiva l'account e chiudi tutte le sessioni.
2. Controlla utenti creati, plugin installati, file modificati di recente.
3. Ripristina l'accesso solo con MFA attiva.

### Sito modificato / malware

1. Manutenzione, snapshot per le prove.
2. Ripristino da backup antecedente alla compromissione; aggiornamento di tutto.
3. Cambio di tutte le credenziali (pannello, database, FTP/SSH, hosting).
4. Richiesta di revisione a Google Search Console se segnalato come pericoloso.

### Dipendenza malevola installata

Vedi [npm-dopo-shai-hulud](../06-supply-chain/npm-dopo-shai-hulud.md), sezione "Se sospetti una compromissione".

## 7. Esercitazioni

| Data | Scenario | Partecipanti | Esito e azioni |
|---|---|---|---|
| | | | |
