---
titolo: Ecosistema npm dopo Shai-Hulud
stato: attivo
creato: 2026-10-15
aggiornato: 2026-10-16
tag: [sicurezza-web, supply-chain]
prossima_revisione: 2027-01-15
owasp: [A03:2025, A08:2025]
---

# Ecosistema npm dopo Shai-Hulud

> **In sintesi.** Shai-Hulud ha dimostrato che `npm install` va trattato come esecuzione di codice remoto. Le contromisure sono di due tipi: quelle che applichi tu come **consumatore** di pacchetti, e quelle che applichi come **pubblicatore**.

## Cosa è successo

| Data | Evento |
|---|---|
| Fine agosto 2025 | Compromissione di **Nx**, attribuita allo stesso attore |
| 14–16 settembre 2025 | **Shai-Hulud**: worm auto-replicante, phishing ai maintainer tramite domini che imitano npm; colpiti pacchetti come `@ctrl/tinycolor`, `ngx-bootstrap`, `ng2-file-upload`. Oltre 477 pacchetti compromessi secondo le stime successive |
| 24 novembre 2025 | **SHA1-Hulud / Shai-Hulud 2.0**: seconda ondata, ancora attiva a dicembre 2025 |

Meccanismo: script di lifecycle (`postinstall`) che rubano token GitHub/npm e chiavi cloud, li pubblicano in repository chiamati "Shai-Hulud" negli account delle vittime, aggiungono un workflow GitHub Actions malevolo e ripubblicano automaticamente gli altri pacchetti del maintainer.

## Come consumatore

### 🔴 Obbligatorio

- `npm ci` in CI e nei deploy, mai `npm install`.
- Lockfile versionato e revisionato nelle pull request (attenzione alla *lockfile injection*: URL `resolved` che puntano fuori dal registro).
- Disattiva gli script di lifecycle di default e abilitali solo per i pacchetti che ne hanno bisogno:

  ```ini
  # .npmrc
  ignore-scripts=true
  ```

  Con **pnpm 10+** gli script di lifecycle delle dipendenze **non vengono eseguiti per default**: si approvano esplicitamente con `onlyBuiltDependencies` (o `pnpm approve-builds`). Usa **pnpm ≥ 10.26.0**: le versioni precedenti avevano una falla (CVE-2025-69264, gravità alta) che permetteva di eseguire script tramite dipendenze installate da repository git.
- Verifica firme e attestazioni del registro: `npm audit signatures`.

### 🟠 Raccomandato

- **Età minima delle versioni** prima dell'installazione (pnpm `minimumReleaseAge`, Renovate `minimumReleaseAge`, Dependabot `cooldown` — quest'ultimo vale solo per gli aggiornamenti di versione, non per quelli di sicurezza, che restano immediati).
- Evita le dipendenze installate direttamente da URL git: sfuggono a molti controlli del registro.
- Sviluppo in container o devcontainer isolati: il malware trova meno segreti.
- Nessun token di lunga durata sulle macchine di sviluppo; `gh auth` con scope minimi.

## Come pubblicatore

GitHub ha annunciato a settembre 2025 un irrigidimento del registro npm:

- **2FA obbligatoria** per la pubblicazione locale, senza eccezioni di bypass;
- token granulari con **durata massima di 7 giorni** e revoca dei token classici;
- pubblicazione via token **disabilitata di default**, a favore di trusted publishing o 2FA.

Pratiche:

- 🔴 Usa **Trusted Publishing** (OIDC da GitHub Actions o GitLab CI): nessun token da rubare, e npm genera automaticamente le **provenance attestation**. Richiede npm CLI ≥ 11.5.1 e va configurato per ciascun pacchetto.

  ```yaml
  permissions:
    contents: read
    id-token: write
  steps:
    - run: npm install -g npm@latest
    - run: npm publish
  ```

- 🔴 2FA con chiave di sicurezza / passkey sull'account npm e GitHub.
- 🟠 Diffida di email "npm" che chiedono di aggiornare la 2FA: era il vettore iniziale.

## Se sospetti una compromissione

1. Rimuovi le versioni compromesse, pulisci cache (`npm cache clean --force`) e `node_modules`.
2. **Ruota tutti i segreti** esposti: token GitHub e npm, chiavi cloud, chiavi API.
3. Cerca repository chiamati `Shai-Hulud`, branch `shai-hulud` e file `.github/workflows/shai-hulud-workflow.yml`.
4. Verifica i workflow CI e i pacchetti pubblicati di recente dai tuoi account.

## Fonti

- [OSV-PNPM], [GH-DEPENDABOT], [CSN-SHAI], [SNYK-NPM], [SOCRADAR-SHAI], [LEADDEV-SHAI], [BLACKPOINT-SHAI], [DEEPWATCH-BRIEF], [THN-GITHUB], [RHC-GITHUB], [PHILNA-TP] — vedi [fonti.md](../fonti.md)
