---
titolo: Quiz di verifica
stato: attivo
creato: 2026-10-15
aggiornato: 2026-10-16
tag: [sicurezza-web, formazione]
prossima_revisione: 2027-10-15
---

# Quiz di verifica

Due set: **base** per tutti, **tecnico** per chi sviluppa o gestisce i siti. Le soluzioni sono in fondo.

## Set base (tutti)

**1.** Ricevi un'email da "npm" o dal tuo hosting che ti chiede di riconfigurare l'autenticazione a due fattori entro 24 ore. Cosa fai?
a) Clicco e seguo le istruzioni, è urgente
b) Apro il sito digitando l'indirizzo e controllo da lì, oppure chiedo al referente
c) Rispondo all'email chiedendo se è vera

**2.** Quale di queste password è la più robusta?
a) `P@ssw0rd2026!`
b) `Tr0ub4dor&3`
c) `gatto lampada autunno ferrovia`

**3.** Le passkey sono più sicure delle password perché…
a) sono più lunghe
b) non esiste un segreto che si possa consegnare a un sito falso
c) scadono ogni 90 giorni

**4.** Un collaboratore esterno ha finito il lavoro sul sito. Cosa va fatto?
a) Nulla, magari torna
b) Cambiargli la password
c) Disattivare i suoi account, revocare token e ruotare le credenziali condivise che conosceva

**5.** Scopri che un file con indirizzi di clienti era pubblicamente raggiungibile. Entro quanto può essere necessario notificarlo al Garante?
a) 72 ore dalla scoperta
b) 30 giorni
c) Solo se qualcuno se ne lamenta

**6.** Ogni quanto conviene cambiare una password robusta e mai compromessa, secondo NIST?
a) Ogni 90 giorni
b) Ogni anno
c) Solo se c'è il sospetto che sia stata compromessa

## Set tecnico

**7.** Qual è il rischio n.1 della OWASP Top 10:2025?
a) Injection
b) Broken Access Control
c) Software Supply Chain Failures

**8.** `GET /api/ordini/1043` restituisce l'ordine di un altro cliente. Come si chiama il difetto e qual è la correzione?
a) XSS — escape dell'output
b) IDOR/BOLA — verifica lato server che l'oggetto appartenga all'utente
c) CSRF — token anti-CSRF

**9.** Quale CSP protegge davvero dalle XSS?
a) `script-src 'self' 'unsafe-inline' https://cdn.jsdelivr.net`
b) `script-src 'nonce-<casuale>' 'strict-dynamic'; object-src 'none'; base-uri 'none'`
c) `default-src *`

**10.** Dopo Shai-Hulud, quale misura riduce di più il rischio di eseguire codice malevolo installando dipendenze npm?
a) Usare sempre l'ultima versione appena uscita
b) `npm ci` dal lockfile con gli script di installazione disattivati e un'età minima delle versioni
c) Eseguire `npm audit` una volta all'anno

**11.** Il server scarica un URL fornito dall'utente per generare un'anteprima. Quale attacco va prevenuto?
a) SSRF
b) Clickjacking
c) Session fixation

**12.** Un controllo di autorizzazione va in eccezione. Cosa deve succedere?
a) Lasciare passare per non bloccare l'utente
b) Negare l'accesso e registrare l'errore
c) Riprovare all'infinito

**13.** Hai fatto commit per errore di una chiave API su un repository. Qual è la prima azione?
a) Riscrivere la storia di git
b) Ruotare (revocare e sostituire) la chiave
c) Rendere privato il repository

**14.** Un chatbot del sito riassume pagine web per gli utenti. Una pagina contiene un testo nascosto che istruisce il modello a inviare dati altrove. Come si chiama il rischio?
a) Prompt injection indiretta (LLM01)
b) Model poisoning
c) Overfitting

**15.** Cosa protegge lo scambio di chiavi ibrido X25519MLKEM768?
a) La firma dei certificati
b) Il traffico registrato oggi da decifrazioni future con computer quantistici
c) Gli attacchi DDoS

---

<details>
<summary><b>Soluzioni</b></summary>

1-b · 2-c (la lunghezza conta più della complessità) · 3-b · 4-c · 5-a (art. 33 GDPR, se c'è rischio per le persone) · 6-c (NIST SP 800-63B-4) · 7-b · 8-b · 9-b · 10-b · 11-a · 12-b (fail-closed, OWASP A10:2025) · 13-b · 14-a · 15-b

Approfondimenti: [password-nist](../01-autenticazione/password-nist.md), [passkey-webauthn](../01-autenticazione/passkey-webauthn.md), [controllo-accessi](../02-autorizzazione/controllo-accessi.md), [content-security-policy](../04-browser/content-security-policy.md), [npm-dopo-shai-hulud](../06-supply-chain/npm-dopo-shai-hulud.md), [ssrf](../02-autorizzazione/ssrf.md), [gestione-errori](../10-operazioni/gestione-errori.md), [dati-e-segreti](../05-crittografia/dati-e-segreti.md), [owasp-llm-top10](../08-ai-llm/owasp-llm-top10.md), [post-quantum](../05-crittografia/post-quantum.md).
</details>
