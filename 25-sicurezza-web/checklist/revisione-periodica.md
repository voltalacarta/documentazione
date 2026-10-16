---
titolo: Checklist di revisione periodica
stato: attivo
creato: 2026-10-15
aggiornato: 2026-10-16
tag: [sicurezza-web, checklist]
prossima_revisione: 2027-04-15
---

# Checklist di revisione periodica

La sicurezza di un sito decade nel tempo anche senza toccare il codice: escono nuove vulnerabilità, scadono certificati, restano account di persone che non lavorano più con te.

## Ogni settimana

- [ ] Applicati gli aggiornamenti di sicurezza di CMS, plugin, dipendenze (o verificato che gli auto-update siano andati a buon fine)
- [ ] Letti gli alert di sicurezza della settimana

## Ogni mese

- [ ] Controllati i report di Dependabot/Renovate e gli advisory dello stack
- [ ] Verificato il catalogo **CISA KEV** per i componenti in uso
- [ ] Rivisti i report CSP e i picchi negli accessi negati
- [ ] Verificato che i backup siano stati eseguiti

## Ogni trimestre

- [ ] **Test di ripristino** da backup → [backup](../10-operazioni/backup-e-continuita.md)
- [ ] Revisione degli account: utenti admin, accessi a hosting/DNS/CI, chiavi API, membri del repository; rimuovi chi non serve più
- [ ] Rotazione dei segreti in scadenza → [segreti](../05-crittografia/dati-e-segreti.md)
- [ ] Scansione DAST completa
- [ ] Ricontrollo header e TLS (SSL Labs, Observatory)
- [ ] Verifica dei record DNS (sottodomini orfani)
- [ ] Revisione dei file di questa base con `prossima_revisione` scaduta → [CONTRIBUIRE](../contribuire.md)

## Ogni anno

- [ ] Penetration test
- [ ] Aggiornamento del threat model → [threat-modeling](../00-fondamenti/threat-modeling.md)
- [ ] Esercitazione di risposta agli incidenti → [incident-response](../10-operazioni/incident-response.md)
- [ ] Aggiornamento di `Expires` in `security.txt`
- [ ] Formazione di sviluppatori e, per i soggetti NIS2, degli organi di amministrazione
- [ ] Verifica delle nuove edizioni di OWASP Top 10, ASVS, API Top 10, LLM Top 10, NIST
- [ ] Revisione di contratti e DPA con i fornitori

## Scadenze normative da tenere d'occhio (aggiornato al 2026-10-15)

- [ ] **31/10/2026** — NIS2: misure di sicurezza di base operative (soggetti in elenco dal 2025)
- [ ] **1/1 – 28/2/2027** — NIS2: finestra annuale di registrazione/aggiornamento ACN (ricorre ogni anno secondo il vademecum ACN di settembre 2026)
- [ ] **marzo 2027** — certificati TLS pubblici: validità massima ridotta a 100 giorni → verificare che il rinnovo sia automatico
- [ ] **11/12/2027** — CRA: applicazione completa
