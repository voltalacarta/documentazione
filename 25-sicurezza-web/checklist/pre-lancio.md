---
titolo: Checklist pre-lancio
stato: attivo
creato: 2026-10-15
aggiornato: 2026-10-16
tag: [sicurezza-web, checklist]
prossima_revisione: 2027-04-15
---

# Checklist pre-lancio

Da completare prima di mettere online un sito o una nuova versione importante. Ogni voce rimanda al file di approfondimento. Le voci 🔴 sono bloccanti.

## Autenticazione e sessioni

- [ ] 🔴 MFA su tutti gli account amministrativi (app, CMS, hosting, DNS, registrar, repository, CI) → [mfa](../01-autenticazione/mfa-e-recupero-account.md)
- [ ] 🟠 Passkey disponibili per gli utenti → [passkey](../01-autenticazione/passkey-webauthn.md)
- [ ] 🔴 Password: min. 15 caratteri (8 con MFA), blocklist, nessuna scadenza forzata, Argon2id/bcrypt → [password](../01-autenticazione/password-nist.md)
- [ ] 🔴 Rate limiting su login, reset e OTP → [waf](../09-infrastruttura/waf-rate-limiting-bot.md)
- [ ] 🔴 Cookie `Secure; HttpOnly; SameSite`, ID rigenerato al login, logout lato server → [sessioni](../01-autenticazione/sessioni-e-cookie.md)

## Autorizzazione

- [ ] 🔴 Nega per default; ogni endpoint verifica utente e proprietà dell'oggetto → [controllo-accessi](../02-autorizzazione/controllo-accessi.md)
- [ ] 🔴 Testato con due account che provano ad accedere uno ai dati dell'altro
- [ ] 🔴 Fetch di URL lato server protetti da SSRF → [ssrf](../02-autorizzazione/ssrf.md)

## Input e output

- [ ] 🔴 Query parametrizzate ovunque → [injection](../03-input-e-output/injection.md)
- [ ] 🔴 Validazione con schema di form e API → [api](../07-api/owasp-api-top10.md)
- [ ] 🔴 Escape automatico attivo, nessun `innerHTML`/`v-html` con dati utente → [xss](../03-input-e-output/xss.md)
- [ ] 🔴 Protezione CSRF attiva → [csrf](../03-input-e-output/csrf.md)
- [ ] 🔴 Upload: allowlist, rinomina, fuori dalla web root → [upload](../03-input-e-output/upload-file.md)

## Browser e trasporto

- [ ] 🔴 HTTPS ovunque, TLS 1.2+ (1.3 preferito), certificati automatici → [tls](../05-crittografia/tls-e-hsts.md)
- [ ] 🔴 HSTS ≥ 1 anno → [header](../04-browser/header-di-sicurezza.md)
- [ ] 🔴 `nosniff`, `Referrer-Policy`, `frame-ancestors` configurati
- [ ] 🟠 CSP strict (almeno in report-only) → [csp](../04-browser/content-security-policy.md)
- [ ] 🔴 CORS assente o con allowlist esatta → [cors](../04-browser/cors.md)
- [ ] 🟠 Key exchange post-quantum abilitato → [post-quantum](../05-crittografia/post-quantum.md)

## Configurazione e infrastruttura

- [ ] 🔴 Debug off, nessun `.git`/`.env`/backup raggiungibile, nessuna console admin esposta → [hardening](../09-infrastruttura/hardening-configurazione.md)
- [ ] 🔴 Database e servizi interni non esposti su Internet
- [ ] 🔴 Header `Server`/`X-Powered-By` rimossi
- [ ] 🔴 CMS, plugin e temi aggiornati; inutilizzati rimossi → [cms](../09-infrastruttura/cms-e-hosting.md)
- [ ] 🟠 WAF/CDN davanti all'origine, IP origine non pubblico
- [ ] 🟠 SPF, DKIM, DMARC sul dominio

## Supply chain

- [ ] 🔴 Lockfile versionato, installazioni con `npm ci` o equivalente → [dipendenze](../06-supply-chain/dipendenze.md)
- [ ] 🔴 Nessuna vulnerabilità critica/alta nota nelle dipendenze
- [ ] 🔴 Nessun segreto nel repository (secret scanning eseguito) → [segreti](../05-crittografia/dati-e-segreti.md)
- [ ] 🟠 Script di lifecycle npm disattivati o controllati → [npm](../06-supply-chain/npm-dopo-shai-hulud.md)
- [ ] 🟠 SRI sugli script da CDN; azioni CI fissate per SHA → [ci-cd](../06-supply-chain/ci-cd.md)

## Operazioni

- [ ] 🔴 Errori generici all'utente, controlli fail-closed → [gestione-errori](../10-operazioni/gestione-errori.md)
- [ ] 🔴 Log degli eventi di sicurezza centralizzati, senza dati sensibili → [logging](../10-operazioni/logging-e-alert.md)
- [ ] 🟠 Almeno un alert attivo e testato
- [ ] 🔴 Backup automatici, off-site, **ripristino testato** → [backup](../10-operazioni/backup-e-continuita.md)
- [ ] 🟠 Piano di risposta agli incidenti con contatti e termini di notifica → [incident-response](../10-operazioni/incident-response.md)
- [ ] 🟠 `/.well-known/security.txt` pubblicato → [disclosure](../10-operazioni/vulnerability-disclosure.md)

## AI (se presente)

- [ ] 🔴 Output del modello trattato come non fidato; nessun segreto nel system prompt → [llm](../08-ai-llm/owasp-llm-top10.md)
- [ ] 🔴 Strumenti dell'agente con permessi minimi e conferma per azioni irreversibili → [agenti](../08-ai-llm/agenti-e-strumenti.md)
- [ ] 🔴 Limiti di consumo per utente

## Normativa

- [ ] 🔴 Informativa privacy, consenso cookie, registro trattamenti, DPA con i fornitori → [gdpr](../12-normativa-ue/gdpr.md)
- [ ] 🟠 Verificata l'eventuale applicabilità di NIS2 e CRA → [nis2](../12-normativa-ue/nis2-italia.md), [cra](../12-normativa-ue/cyber-resilience-act.md)

## Verifica finale

- [ ] 🟠 Scansione DAST (es. ZAP) su staging → [testing](../11-sdlc/testing-di-sicurezza.md)
- [ ] 🟠 SSL Labs ≥ A, Mozilla Observatory / securityheaders.com verificati
- [ ] 🟠 Penetration test se il sito ha login, pagamenti o dati personali
