---
titolo: Requisiti di sicurezza per capitolati e contratti
stato: attivo
creato: 2026-10-15
aggiornato: 2026-10-16
tag: [sicurezza-web, progetti]
prossima_revisione: 2027-04-15
---

# Requisiti di sicurezza per capitolati e contratti

> ⚠️ Testo tecnico di partenza: le clausole contrattuali (responsabilità, penali, garanzie) vanno validate da un legale.
>
> **In sintesi.** Se commissioni un sito o un'app a un'agenzia, ciò che non è scritto nel contratto non è dovuto. Questo testo si incolla in un capitolato o in un'offerta e rende i requisiti di sicurezza verificabili alla consegna. Adatta il livello al [profilo del progetto](profili-di-progetto.md).

---

## Testo da incollare

### Art. [X] — Sicurezza

**X.1 Standard di riferimento.** Il Fornitore progetta, sviluppa e configura la soluzione in conformità allo standard **OWASP ASVS 5.0, livello [1/2]**, e tiene conto dei rischi descritti in **OWASP Top 10:2025** [e, se applicabile, OWASP API Security Top 10:2023 / OWASP Top 10 for LLM Applications 2025]. Le eventuali deroghe sono documentate e approvate per iscritto dal Committente.

**X.2 Requisiti minimi.** Alla consegna la soluzione garantisce almeno:
a) HTTPS su tutte le risorse, TLS 1.2 o superiore (1.3 abilitato), HSTS di almeno un anno;
b) header di sicurezza: `Content-Security-Policy` (almeno `frame-ancestors`, `object-src 'none'`, `base-uri`), `X-Content-Type-Options: nosniff`, `Referrer-Policy`, `Cross-Origin-Opener-Policy`, `Permissions-Policy`;
c) cookie di sessione con attributi `Secure`, `HttpOnly`, `SameSite`;
d) autenticazione amministrativa con MFA; per gli utenti, password conformi a NIST SP 800-63B-4 [e passkey];
e) controllo degli accessi lato server su ogni funzione e oggetto;
f) query parametrizzate, validazione degli input, escape dell'output;
g) nessuna credenziale o segreto nel codice sorgente o nel repository;
h) modalità di debug disattivata e nessun file di configurazione, backup o repository accessibile pubblicamente;
i) componenti di terze parti in versioni supportate e prive di vulnerabilità note di gravità alta o critica alla data di consegna;
j) registrazione degli eventi di sicurezza (accessi, errori di autenticazione, azioni amministrative) senza dati sensibili in chiaro.

**X.3 Verifica.** Prima del collaudo il Fornitore consegna:
a) l'elenco delle componenti software (SBOM in formato CycloneDX o SPDX);
b) il report di una scansione automatica delle dipendenze e di una scansione dinamica (es. OWASP ZAP);
c) [per profili B–D] il report di un penetration test eseguito da soggetto indipendente, con le vulnerabilità alte e critiche risolte e ri-verificate.
Il Committente può eseguire o far eseguire verifiche proprie; le non conformità ai requisiti X.2 sono trattate come difetti.

**X.4 Proprietà e accessi.** Domini, hosting, account di servizio, repository del codice e chiavi sono intestati al Committente o trasferiti a esso alla consegna. Il Fornitore accede con account nominativi e MFA, e restituisce o revoca ogni accesso a fine contratto, dandone conferma scritta.

**X.5 Codice e documentazione.** Il Fornitore consegna il codice sorgente completo in un repository del Committente, con istruzioni di build e deploy, e la documentazione delle configurazioni di sicurezza.

**X.6 Manutenzione di sicurezza.** Per [12/24/36] mesi dalla consegna il Fornitore:
a) applica le patch di sicurezza di gravità critica entro [72 ore] e alta entro [7 giorni] dalla disponibilità;
b) monitora le vulnerabilità delle componenti utilizzate;
c) mantiene aggiornati core, plugin e dipendenze.

**X.7 Incidenti.** Il Fornitore notifica al Committente qualunque incidente o vulnerabilità sfruttata che riguardi la soluzione **senza ingiustificato ritardo e comunque entro [12] ore** dalla conoscenza, per consentire al Committente il rispetto dei propri obblighi (GDPR art. 33, e ove applicabili D.Lgs. 138/2024 e Reg. UE 2024/2847), e collabora alla gestione.

**X.8 Dati personali.** Il trattamento di dati personali per conto del Committente è regolato da un accordo ai sensi dell'art. 28 GDPR, parte integrante del contratto.

**X.9 Sub-fornitori.** L'uso di sub-fornitori, servizi SaaS e componenti che trattano dati del Committente è comunicato in anticipo e soggetto agli stessi requisiti.

---

## Checklist di collaudo (uso interno)

- [ ] [check-headers.py](../14-automazione/scripts/check-headers.py) senza errori
- [ ] SSL Labs ≥ A
- [ ] SBOM ricevuta, nessuna vulnerabilità alta/critica aperta
- [ ] Report ZAP ricevuto e analizzato
- [ ] Report pen test ricevuto, rilievi alti/critici chiusi (profili B–D)
- [ ] Repository, domini e account trasferiti; credenziali dell'agenzia revocate o nominative
- [ ] Backup configurati e un ripristino provato
- [ ] DPA firmato
