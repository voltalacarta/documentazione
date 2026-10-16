---
titolo: Sicurezza di CI/CD e integrità del software
stato: attivo
creato: 2026-10-15
aggiornato: 2026-10-16
tag: [sicurezza-web, supply-chain]
prossima_revisione: 2027-01-15
owasp: [A03:2025, A08:2025]
---

# Sicurezza di CI/CD e integrità del software

> **In sintesi.** La pipeline ha accesso a codice, segreti e produzione: è il bersaglio più redditizio. Va protetta come un sistema di produzione, con credenziali effimere e permessi minimi.

## Repository

- 🔴 MFA obbligatoria per tutti i membri dell'organizzazione (GitHub/GitLab/Bitbucket).
- 🔴 **Branch protection** sul ramo principale: pull request obbligatoria, almeno una review, check verdi, niente force push.
- 🟠 `CODEOWNERS` per i file sensibili (workflow, configurazioni di deploy, gestione permessi).
- 🟠 Commit firmati (SSH/GPG/Sigstore gitsign) per i repository critici.

## Pipeline (esempio GitHub Actions)

- 🔴 Permessi del `GITHUB_TOKEN` al minimo, dichiarati in ogni workflow:

  ```yaml
  permissions:
    contents: read
  ```

- 🔴 **OIDC** verso il cloud (AWS/GCP/Azure) invece di chiavi statiche nei secret.
- 🔴 Azioni di terze parti **fissate per SHA del commit**, non per tag (`uses: org/action@<sha40>`). Dependabot può aggiornarle.
- 🔴 Attenzione a `pull_request_target` e `workflow_run`: eseguono con privilegi sul codice di fork non fidati.
- 🔴 Non interpolare input non fidati (titoli di PR, nomi di branch) direttamente negli script `run:` → script injection. Passali come variabili d'ambiente.
- 🟠 Ambienti protetti (`environment:`) con approvazione manuale per la produzione.
- 🟠 Runner self-hosted: effimeri, isolati, mai usati per repository pubblici.
- 🟢 Strumenti di analisi dei workflow: `zizmor`, `actionlint`, OpenSSF Scorecard.

## Integrità degli artefatti

- 🟠 **Provenance** degli artefatti secondo **SLSA** (livello 2–3): build riproducibili su runner gestiti, attestazioni firmate.
- 🟠 Firma di immagini container e pacchetti con **Sigstore/cosign**; verifica della firma al deploy (admission controller).
- 🟠 Immagini base minimali (distroless, Wolfi, Alpine) aggiornate e scansionate.
- 🔴 Aggiornamenti automatici del software (auto-update, plugin) solo da canali firmati e verificati: è il cuore di A08.

## Fonti

- [SNYK-NPM], [THN-GITHUB], [DEEPWATCH-BRIEF] — vedi [fonti.md](../fonti.md)
