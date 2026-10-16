---
titolo: Gestione delle dipendenze (SCA, SBOM, aggiornamenti)
stato: attivo
creato: 2026-10-15
aggiornato: 2026-10-16
tag: [sicurezza-web, supply-chain]
prossima_revisione: 2027-01-15
owasp: [A03:2025]
asvs: [V15]
---

# Gestione delle dipendenze

> **In sintesi.** Dal 2025 la supply chain ha una categoria propria nella OWASP Top 10 (A03), che allarga i vecchi "componenti vulnerabili" a registri, build e distribuzione. Due rischi diversi: dipendenze **vulnerabili** (bug noti) e dipendenze **malevole** (pacchetti compromessi). Servono difese per entrambi.

## Inventario

- 🔴 Sai quali componenti usi? Lockfile versionato per ogni ecosistema (`package-lock.json`, `pnpm-lock.yaml`, `poetry.lock`, `composer.lock`, `go.sum`).
- 🟠 Genera una **SBOM** (CycloneDX o SPDX) a ogni build: `syft`, `cdxgen`, plugin dei build tool. È anche un requisito ricorrente nel [Cyber Resilience Act](../12-normativa-ue/cyber-resilience-act.md).
- 🟠 Includi negli inventari anche gli **script di terze parti** caricati nel browser (analytics, chat, pagamenti, tag manager).

## Vulnerabilità note (SCA)

- 🔴 Scansione automatica: Dependabot, Renovate, `npm audit`, `pip-audit`, OSV-Scanner, Trivy, Snyk.
- 🔴 Politica di patch con tempi definiti (esempio):

  | Gravità | Tempo massimo |
  |---|---|
  | Critica / nel catalogo CISA KEV | 48–72 ore |
  | Alta | 7 giorni |
  | Media | 30 giorni |
  | Bassa | prossimo ciclo |

- 🟠 Prioritizza per **raggiungibilità** e sfruttamento reale (EPSS, KEV), non solo per CVSS.

## Pacchetti malevoli

- 🔴 Installazioni deterministiche dal lockfile (`npm ci`, `pip install --require-hashes`, `composer install`).
- 🔴 Disabilita o controlla gli **script di installazione** (vedi [npm-dopo-shai-hulud](npm-dopo-shai-hulud.md)).
- 🟠 **Cooldown**: non adottare versioni pubblicate da meno di qualche giorno (molte compromissioni vengono rilevate e rimosse entro ore o pochi giorni). Renovate `minimumReleaseAge`, pnpm `minimumReleaseAge`.
- 🟠 Attenzione a **typosquatting** e *dependency confusion*: registri privati con scope riservati, nomi verificati.
- 🟠 Valuta la salute del pacchetto prima di adottarlo: manutentori, frequenza di rilascio, OpenSSF Scorecard.
- 🟢 Proxy/registry interno con quarantena (Artifactory, Nexus, Verdaccio) e scanner di malware (Socket, Aikido, Phylum, ecc.).

## Script di terze parti nel browser

- 🔴 **Subresource Integrity** per script e CSS da CDN:

  ```html
  <script src="https://cdn.example.com/lib.min.js"
          integrity="sha384-..." crossorigin="anonymous"></script>
  ```

- 🟠 Ospita localmente le librerie quando possibile.
- 🟠 Riduci il numero di tag di terze parti; ognuno ha accesso completo alla pagina (rischio *Magecart* sui checkout).

## Fonti

- [HCL-T10], [OWASP-T10], [SNYK-NPM], [CHAINGUARD-NPM] — vedi [fonti.md](../fonti.md)
