---
titolo: Hardening e configurazione sicura
stato: attivo
creato: 2026-10-15
aggiornato: 2026-10-16
tag: [sicurezza-web, infrastruttura]
prossima_revisione: 2027-04-15
owasp: [A02:2025]
asvs: [V13]
---

# Hardening e configurazione sicura

> **In sintesi.** Le configurazioni errate sono salite al secondo posto della OWASP Top 10:2025 e sono state trovate in tutte le applicazioni testate. La difesa è rendere la configurazione **codice**: versionata, revisionata, ripetibile e verificata automaticamente.

## Applicazione

- 🔴 Modalità debug **disattivata** in produzione (`DEBUG=False`, `APP_ENV=production`, `NODE_ENV=production`).
- 🔴 Nessuna pagina di default, console di amministrazione esposta (phpMyAdmin, Adminer, `/actuator`, `/_profiler`), file di esempio o installer rimasti online.
- 🔴 Nessun file sensibile servibile: `.git/`, `.env`, backup (`*.bak`, `*.sql`, `*.zip`), `composer.json`, source map pubbliche con codice interno.
- 🔴 Credenziali di default cambiate ovunque.
- 🟠 Listing delle directory disattivato.
- 🟠 Configurazioni identiche (salvo segreti) tra staging e produzione, così i test sono significativi.

## Server e rete

- 🔴 Solo le porte necessarie esposte (tipicamente 443, e 80 per il redirect). Database, Redis, Elasticsearch **mai** su IP pubblico.
- 🔴 Accesso amministrativo (SSH, pannelli) tramite VPN, bastion o accesso zero trust; SSH solo con chiavi, root login disattivato.
- 🔴 Aggiornamenti di sicurezza del sistema operativo automatici o pianificati.
- 🟠 Segmentazione: il server web non raggiunge reti che non gli servono.
- 🟠 Processi applicativi con utente non privilegiato; container non-root, filesystem in sola lettura dove possibile.

## Cloud

- 🔴 Bucket di storage **privati per default**; blocco dell'accesso pubblico a livello di account.
- 🔴 MFA e nessun uso quotidiano dell'account root/owner.
- 🟠 IAM con ruoli minimi; niente chiavi di accesso statiche dove si può usare l'identità del workload.
- 🟠 Strumenti di postura (CSPM): AWS Security Hub, Google Security Command Center, Microsoft Defender for Cloud, Prowler (open source).

## Infrastructure as Code

- 🟠 Terraform/OpenTofu, Pulumi, Ansible versionati e revisionati.
- 🟠 Scansione IaC in CI: Checkov, tfsec/Trivy, KICS.
- 🟢 Rilevamento del *drift* tra configurazione dichiarata e reale.

## DNS ed email del dominio

- 🔴 Account del registrar e del DNS con MFA e blocco del trasferimento (*registrar lock*).
- 🟠 Elimina i record DNS che puntano a risorse dismesse (rischio *subdomain takeover*).
- 🟠 SPF, DKIM e DMARC (fino a `p=reject`) per impedire email false a nome del dominio.

## Fonti

- [OWASP-T10], [RADWARE-T10], [RADWARE-15BP] — vedi [fonti.md](../fonti.md)
