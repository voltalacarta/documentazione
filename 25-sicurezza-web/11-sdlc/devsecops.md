---
titolo: DevSecOps — sicurezza nel ciclo di sviluppo
stato: attivo
creato: 2026-10-15
aggiornato: 2026-10-16
tag: [sicurezza-web, sdlc]
prossima_revisione: 2027-04-15
owasp: [A06:2025]
---

# DevSecOps

> **In sintesi.** La sicurezza costa meno quanto prima entra nel processo ("shift left"), ma non finisce al rilascio: serve anche in esercizio ("shield right"). L'obiettivo è che i controlli siano **automatici** e i loro risultati arrivino a chi scrive il codice.

## Il ciclo

| Fase | Attività | Riferimento |
|---|---|---|
| Requisiti | Livello ASVS target, requisiti di privacy | [owasp-asvs-5](../00-fondamenti/owasp-asvs-5.md) |
| Design | Threat modeling | [threat-modeling](../00-fondamenti/threat-modeling.md) |
| Sviluppo | Linee guida di codice sicuro, IDE con linter di sicurezza, pre-commit hook per segreti | [dati-e-segreti](../05-crittografia/dati-e-segreti.md) |
| Code review | Checklist di sicurezza nelle PR | sotto |
| Build | SAST, SCA, secret scanning, scansione IaC e container, SBOM | [testing-di-sicurezza](testing-di-sicurezza.md) |
| Test | DAST, test di autorizzazione | [testing-di-sicurezza](testing-di-sicurezza.md) |
| Rilascio | Firma artefatti, approvazione per la produzione | [ci-cd](../06-supply-chain/ci-cd.md) |
| Esercizio | WAF, monitoraggio, alert, patching | [10-operazioni](../10-operazioni/logging-e-alert.md) |

## Checklist per la code review

- [ ] Nuove route: autenticazione e autorizzazione presenti?
- [ ] Accesso a oggetti: verifica di proprietà/tenant?
- [ ] Input esterni: validati con schema?
- [ ] Query e comandi: parametrizzati?
- [ ] Output HTML: niente vie di fuga dall'escape automatico?
- [ ] Nuove dipendenze: necessarie, mantenute, versione fissata?
- [ ] Segreti: nessuno nel diff?
- [ ] Errori: gestiti, fail-closed, senza dettagli all'utente?
- [ ] Log: eventi di sicurezza registrati, nessun dato sensibile?
- [ ] Codice generato da AI: revisionato con la stessa attenzione del resto?

## Codice scritto con assistenti AI

- 🔴 Il codice suggerito da un assistente va revisionato e testato come quello di un collaboratore esterno.
- 🟠 Verifica che i pacchetti suggeriti **esistano davvero** e siano quelli attesi: i nomi inventati dai modelli possono essere registrati da attaccanti (*slopsquatting*).
- 🟠 Non incollare segreti o dati personali nei prompt.

## Formazione

- 🟠 Formazione periodica per sviluppatori su OWASP Top 10 e sullo stack in uso (es. OWASP Juice Shop, PortSwigger Web Security Academy, gratuite).
- 🟠 Per i soggetti NIS2, la formazione è richiesta anche agli organi di amministrazione (vedi [nis2-italia](../12-normativa-ue/nis2-italia.md)).

## Fonti

- [PALTECH-BP], [A10-WEBSEC], [HDSUPPLY-7RULES] — vedi [fonti.md](../fonti.md)
