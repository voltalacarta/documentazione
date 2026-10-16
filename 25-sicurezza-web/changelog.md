---
titolo: Changelog
stato: attivo
creato: 2026-10-15
aggiornato: 2026-10-16
tag: [sicurezza-web]
---

# Changelog

Formato ispirato a [Keep a Changelog](https://keepachangelog.com/it/). Versionamento: `MAJOR.MINOR.PATCH`

- **MAJOR**: ristrutturazione dell'albero o cambio di standard di riferimento (es. nuova OWASP Top 10).
- **MINOR**: nuovo file o nuova sezione sostanziale.
- **PATCH**: correzioni, aggiornamento di date, versioni o link.

## [1.3.0] — 2026-10-16

### Aggiunto

- Integrazione nel repository `voltalacarta/documentazione` come sezione `25-sicurezza-web/`.
- Controllo mensile automatico (`.github/workflows/revisioni-sicurezza-web.yml`) che apre una issue quando ci sono revisioni scadute o in scadenza.
- Proposta di decisione [0006](../10-decisioni/0006-riferimento-sicurezza-web.md): la sezione come riferimento per tutti i progetti digitali.
- `README.md` di indice in ogni cartella, come richiesto dalle convenzioni del repository.

### Modificato

- Frontmatter convertito al formato del repository (`titolo`, `stato`, `creato`, `aggiornato`, `tag`), mantenendo `prossima_revisione`, `owasp` e `asvs`.
- Nomi di file adeguati alle convenzioni (minuscole e trattini): `caddyfile`, `netlify-headers`, `laravel-security-headers.php`, `changelog.md`, `contribuire.md`. Ogni file indica con quale nome va copiato.
- Il modello per nuove schede è ora in [`_modelli/scheda-sicurezza-web.md`](../_modelli/scheda-sicurezza-web.md).
- Questionario fornitori: domande con codici univoci per sezione (A1, B2…).
- `kb-revisioni.py`: si esegue dalla radice del repository con `--radice 25-sicurezza-web` e ignora gli indici delle cartelle.
- Formato Markdown corretto secondo `markdownlint` (righe vuote intorno a titoli, elenchi e blocchi).

## [1.2.0] — 2026-10-15

Revisione di accuratezza: chiusi tutti i 15 punti marcati "da verificare" confrontandoli con fonti primarie.

### Corretto

- **Go e post-quantum** (`post-quantum.md`): X25519MLKEM768 è abilitato **di default** da Go 1.24 (non disattivato, come riportava una fonte secondaria).
- **Next.js** (`13-ricettario/`): `nextjs-middleware.ts` sostituito da `nextjs-proxy.ts`, allineato alla guida ufficiale (convenzione `proxy.ts` da Next.js 16; nonce applicato automaticamente; rendering dinamico obbligatorio; alternativa SRI sperimentale).
- **Django** (`13-ricettario/`): CSP con le impostazioni native di Django 6.0 (`SECURE_CSP`, `SECURE_CSP_REPORT_ONLY`, costanti `django.utils.csp.CSP`).
- **Password** (`password-nist.md`): tabella completa dei parametri OWASP; bcrypt indicato come solo legacy (limite di 72 byte); PBKDF2 a 600.000 iterazioni.

### Aggiornato

- **Trusted Types**: Baseline da febbraio 2026 (Safari 26, Firefox); passa da "avanzato" a "raccomandato" per siti con dati sensibili.
- **Sanitizer API `setHTML`**: Firefox 148 e Chrome 146; non ancora Safari.
- **DBSC**: disponibile in Chrome solo su Windows.
- **Certificati TLS**: calendario SC-081 (200 giorni da marzo 2026 — già in vigore —, 100 da marzo 2027, 47 da marzo 2029).
- **OCSP**: Let's Encrypt ha spento i responder il 6/8/2025; sconsigliato Must-Staple.
- **pnpm**: script bloccati per default da v10; usare ≥ 10.26.0 (CVE-2025-69264).
- **Dependabot**: `cooldown` confermato (solo aggiornamenti di versione, non di sicurezza).
- **Cyber Resilience Act**: criteri RDPS delle linee guida della Commissione per i servizi online.
- **Checklist periodica**: aggiunta la scadenza dei certificati a 100 giorni (marzo 2027).

### Confermato senza modifiche

- Capitoli ASVS 5.0 (V1–V17), parametri Argon2id, sintassi OSV-Scanner v2, finestra annuale di registrazione ACN, URL di NIST SP 800-63B-4.

## [1.1.0] — 2026-10-15

### Aggiunto

- `13-ricettario/`: configurazioni di sicurezza per nginx, Apache, Caddy, Netlify, Vercel, Express, Next.js, Django, Laravel e WordPress, con tabella dello stato di verifica.
- `14-automazione/`: `check-headers.py` (header, cookie, TLS, redirect, file esposti; testato su server locali), `kb-revisioni.py` (scadenze e marcatori della base; testato), workflow GitHub Actions, Dependabot, Renovate, `.npmrc`, pre-commit, `.gitignore`.
- `15-modelli/`: security.txt, politica di divulgazione, piano di risposta agli incidenti, registro violazioni GDPR, registro asset e accessi, questionario fornitori, procedura accessi.
- `16-progetti/`: profili di progetto (A–D + moduli) e requisiti di sicurezza da inserire nei capitolati.
- `17-formazione/`: dieci regole per redattori e quiz di verifica (base e tecnico).

### Modificato

- README: percorsi d'uso, albero aggiornato, revisioni tramite `kb-revisioni.py`.

### Da verificare

- Ricette nginx, Caddy, Next.js, Apache e Netlify non validate automaticamente (strumenti non disponibili nell'ambiente di stesura).
- Workflow GitHub Actions validato solo come YAML: eseguire una prima volta e fissare le action per SHA.

## [1.0.0] — 2026-10-15

### Aggiunto

- Prima versione della knowledge base: 13 aree tematiche, 2 checklist, bibliografia centralizzata.
- Allineamento a OWASP Top 10:2025, OWASP ASVS 5.0.0, OWASP API Security Top 10:2023, OWASP Top 10 for LLM Applications 2025.
- Autenticazione allineata a NIST SP 800-63B-4 (password, passkey sincronizzate AAL2).
- Supply chain: lezioni di Shai-Hulud (set. 2025) e SHA1-Hulud (nov. 2025), trusted publishing npm.
- Crittografia: stato del TLS post-quantum (X25519MLKEM768, RFC 10024 di agosto 2026).
- Normativa: GDPR, NIS2 (D.Lgs. 138/2024, scadenza misure di base 31/10/2026), Cyber Resilience Act (segnalazioni dall'11/09/2026).

### Da monitorare

- Ballot CA/Browser Forum sui certificati ML-DSA (non ancora approvato a ottobre 2026).
- Supporto di DBSC e `setHTML` in Safari.
- Linee guida settoriali ACN per le misure NIS2 a lungo termine.
- Eventuale aggiornamento dell'OWASP API Security Top 10 (ultima edizione: 2023).
- Piena applicazione del CRA: 11/12/2027.
