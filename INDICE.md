# Indice compatto

<!-- Generato da strumenti/indici.py: le modifiche qui dentro vengono sovrascritte. -->

108 documenti. Una riga per file: `percorso · titolo · stato · sintesi`.
Per cercare: `grep -i "parola" INDICE.md`, poi apri solo i file trovati.

## 00-meta

- 00-meta/README.md · Meta — regole del repository · attivo · Le regole che tengono in ordine questo repository.
- 00-meta/convenzioni.md · Convenzioni di scrittura · attivo · Nomi dei file, intestazioni, stati, link, commit
- 00-meta/glossario.md · Glossario · attivo · Termini usati nella documentazione
- 00-meta/struttura.md · Struttura del repository · attivo · Perché le cartelle sono fatte così e come aggiungerne di nuove

## 10-decisioni

- 10-decisioni/0001-registrare-le-decisioni.md · Registrare le decisioni in questo repository · accettato · Le scelte su strumenti, metodi e organizzazione vengono prese in conversazioni sparse e rischiano di perdersi.
- 10-decisioni/0002-github-come-base-di-lavoro.md · GitHub come base unica di lavoro · accettato · Si vuole un'unica base per codice, documentazione e note, accessibile da qualsiasi dispositivo e su cui anche l'assistente AI (Claude) possa lavorare
- 10-decisioni/0003-ambiente-di-sviluppo-solo-cloud.md · Ambiente di sviluppo solo cloud con GitHub Codespaces · accettato · Non si vuole usare il computer locale per lo sviluppo: tutto deve funzionare nel cloud, dal browser, da qualsiasi dispositivo.
- 10-decisioni/0004-second-brain-markdown-su-github.md · Second brain in Markdown su GitHub · accettato · Si vuole un second brain stile Obsidian, ma interamente remoto.
- 10-decisioni/0005-strumenti-online-gratuiti.md · Strumenti online gratuiti per editor e second brain · accettato · Le decisioni 0003 e 0004 fissano dove si lavora.
- 10-decisioni/0006-riferimento-sicurezza-web.md · Knowledge base di sicurezza web come riferimento per i progetti digitali · proposto · Sono previsti progetti digitali (siti, applicazioni), non ancora definiti.
- 10-decisioni/0007-grafo-della-conoscenza-automatico-su-tutte-le-repo.md · Grafo della conoscenza automatico su tutte le repo · accettato · Un motore deterministico nel second brain collega tutte le repo, i documenti e i concetti, e mantiene indici compatti per spendere pochi token.
- 10-decisioni/0008-app-web-del-second-brain-su-github-pages.md · App web del second brain su GitHub Pages · accettato · Un'app statica in una repo pubblica legge e scrive il second brain privato con l'API di GitHub e un token personale; zero dipendenze, CSP rigida.
- 10-decisioni/0009-rifare-i-siti-rilegaretesi-it-e-voltalacarta-it-per-vendere.md · Rifare i siti rilegaretesi.it e voltalacarta.it per vendere di più · accettato · Rilegaretesi.it si rifà da zero, voltalacarta.it riceve un restyling pesante; obiettivo: vendere di più nei prossimi 5 anni, partendo subito.
- 10-decisioni/README.md · Registro delle decisioni · attivo · Qui finisce tutto ciò che viene sancito.

## 20-infrastruttura

- 20-infrastruttura/README.md · Infrastruttura · attivo · Com'è fatto l'ambiente di lavoro: piattaforme, strumenti, configurazioni.
- 20-infrastruttura/ambiente-cloud.md · Ambiente di sviluppo cloud · attivo · Codespaces, github.dev, Cloud Shell, costi
- 20-infrastruttura/github.md · GitHub · attivo · Account, repository, convenzioni
- 20-infrastruttura/sicurezza.md · Sicurezza · attivo · Accessi, segreti, backup

## 25-sicurezza-web

- 25-sicurezza-web/00-fondamenti/README.md · Fondamenti · attivo · -
- 25-sicurezza-web/00-fondamenti/owasp-asvs-5.md · OWASP ASVS 5.0 — Standard di verifica · attivo · Se la Top 10 dice quali rischi esistono, l'Application Security Verification Standard dice cosa verificare, con requisiti testabili.
- 25-sicurezza-web/00-fondamenti/owasp-top10-2025.md · OWASP Top 10:2025 · attivo · È il documento di consapevolezza di riferimento sui rischi delle applicazioni web, aggiornato circa ogni 3-4 anni su dati reali.
- 25-sicurezza-web/00-fondamenti/principi.md · Principi di progettazione sicura · attivo · Le tecniche cambiano ogni anno; questi principi no.
- 25-sicurezza-web/00-fondamenti/threat-modeling.md · Threat modeling · attivo · È il modo più economico di prevenire la categoria A06 Insecure Design: ragionare sugli attacchi prima di scrivere codice costa ore, correggere un dife
- 25-sicurezza-web/01-autenticazione/README.md · Autenticazione · attivo · -
- 25-sicurezza-web/01-autenticazione/mfa-e-recupero-account.md · MFA, SSO e recupero account · attivo · Non tutti i secondi fattori si equivalgono.
- 25-sicurezza-web/01-autenticazione/passkey-webauthn.md · Passkey e WebAuthn · attivo · Nel 2026 le passkey sono il metodo di login da offrire per primo: sono resistenti al phishing per costruzione e NIST le riconosce nelle sue linee guid
- 25-sicurezza-web/01-autenticazione/password-nist.md · Politica delle password (NIST SP 800-63B-4) · attivo · Lunghezza conta più della complessità, niente scadenze forzate, controllo contro le password compromesse, pieno supporto ai password manager.
- 25-sicurezza-web/01-autenticazione/sessioni-e-cookie.md · Sessioni, cookie e token · attivo · Una sessione rubata vale quanto una password rubata, e aggira anche la MFA.
- 25-sicurezza-web/02-autorizzazione/README.md · Autorizzazione · attivo · -
- 25-sicurezza-web/02-autorizzazione/controllo-accessi.md · Controllo degli accessi · attivo · È il rischio n.1 della OWASP Top 10:2025 ed è stato trovato in tutte le applicazioni testate.
- 25-sicurezza-web/02-autorizzazione/ssrf.md · Server-Side Request Forgery (SSRF) · attivo · Quando il server scarica un URL fornito dall'utente (anteprime link, webhook, import da URL, generazione PDF, agenti AI che navigano), un attaccante p
- 25-sicurezza-web/03-input-e-output/README.md · Input e output · attivo · -
- 25-sicurezza-web/03-input-e-output/csrf.md · Cross-Site Request Forgery (CSRF) · attivo · Un sito esterno fa inviare al browser della vittima una richiesta autenticata al tuo sito.
- 25-sicurezza-web/03-input-e-output/injection.md · Injection (SQL, NoSQL, comandi, template) · attivo · Succede quando dati non fidati diventano parte di un comando o di una query.
- 25-sicurezza-web/03-input-e-output/upload-file.md · Upload e gestione dei file · attivo · Un file caricato può essere codice eseguibile, una XSS travestita da immagine, una bomba di decompressione o un path traversal.
- 25-sicurezza-web/03-input-e-output/xss.md · Cross-Site Scripting (XSS) · attivo · Tre livelli di difesa che si sommano: encoding contestuale dell'output, CSP strict che impedisce l'esecuzione di script non autorizzati, Trusted Types
- 25-sicurezza-web/04-browser/README.md · Browser · attivo · -
- 25-sicurezza-web/04-browser/content-security-policy.md · Content Security Policy (CSP) · attivo · Usa una CSP strict basata su nonce (siti renderizzati dal server) o su hash (SPA e siti statici).
- 25-sicurezza-web/04-browser/cors.md · CORS (Cross-Origin Resource Sharing) · attivo · CORS non è una protezione: è un allentamento controllato della Same-Origin Policy.
- 25-sicurezza-web/04-browser/header-di-sicurezza.md · Header HTTP di sicurezza · attivo · Gli header attivano protezioni del browser indipendenti dal codice applicativo.
- 25-sicurezza-web/04-browser/trusted-types.md · Trusted Types · attivo · Trusted Types rende il codice JavaScript sicuro per default contro la DOM XSS: i sink pericolosi (innerHTML, eval, script.src…) smettono di accettare
- 25-sicurezza-web/05-crittografia/README.md · Crittografia · attivo · -
- 25-sicurezza-web/05-crittografia/dati-e-segreti.md · Cifratura dei dati e gestione dei segreti · attivo · Non inventare crittografia, usa librerie di alto livello.
- 25-sicurezza-web/05-crittografia/post-quantum.md · Crittografia post-quantum per il web · attivo · Nel 2026 lo scambio di chiavi ibrido post-quantum è già lo standard di fatto del web lato browser.
- 25-sicurezza-web/05-crittografia/tls-e-hsts.md · TLS, certificati e HSTS · attivo · HTTPS ovunque, TLS 1.3 come preferenza, TLS 1.2 solo con cifrari moderni, nulla di più vecchio.
- 25-sicurezza-web/06-supply-chain/README.md · Supply chain · attivo · -
- 25-sicurezza-web/06-supply-chain/ci-cd.md · Sicurezza di CI/CD e integrità del software · attivo · La pipeline ha accesso a codice, segreti e produzione: è il bersaglio più redditizio.
- 25-sicurezza-web/06-supply-chain/dipendenze.md · Gestione delle dipendenze (SCA, SBOM, aggiornamenti) · attivo · Dal 2025 la supply chain ha una categoria propria nella OWASP Top 10 (A03), che allarga i vecchi "componenti vulnerabili" a registri, build e distribu
- 25-sicurezza-web/06-supply-chain/npm-dopo-shai-hulud.md · Ecosistema npm dopo Shai-Hulud · attivo · Shai-Hulud ha dimostrato che npm install va trattato come esecuzione di codice remoto.
- 25-sicurezza-web/07-api/README.md · Api · attivo · -
- 25-sicurezza-web/07-api/owasp-api-top10.md · Sicurezza delle API (OWASP API Security Top 10:2023) · attivo · Le API espongono direttamente la logica di business e i dati, senza l'interfaccia che "nasconde" i campi.
- 25-sicurezza-web/08-ai-llm/README.md · Ai llm · attivo · -
- 25-sicurezza-web/08-ai-llm/agenti-e-strumenti.md · Agenti AI, strumenti e MCP · bozza · Un agente che può navigare, leggere email o chiamare API è un utente privilegiato manovrabile da chiunque riesca a fargli leggere un testo.
- 25-sicurezza-web/08-ai-llm/owasp-llm-top10.md · OWASP Top 10 for LLM Applications 2025 · attivo · Se il sito integra un chatbot, una ricerca semantica, un assistente o un agente, ai rischi web classici si aggiungono quelli specifici dei modelli lin
- 25-sicurezza-web/09-infrastruttura/README.md · Infrastruttura · attivo · -
- 25-sicurezza-web/09-infrastruttura/cms-e-hosting.md · CMS, plugin e hosting · attivo · Per la maggior parte dei siti (WordPress, Joomla, Drupal, PrestaShop, Shopify con app) il rischio principale non è il codice scritto in casa, ma plugi
- 25-sicurezza-web/09-infrastruttura/hardening-configurazione.md · Hardening e configurazione sicura · attivo · Le configurazioni errate sono salite al secondo posto della OWASP Top 10:2025 e sono state trovate in tutte le applicazioni testate.
- 25-sicurezza-web/09-infrastruttura/waf-rate-limiting-bot.md · WAF, rate limiting, bot e DDoS · attivo · Sono controlli perimetrali che riducono il rumore e comprano tempo.
- 25-sicurezza-web/10-operazioni/README.md · Operazioni · attivo · -
- 25-sicurezza-web/10-operazioni/backup-e-continuita.md · Backup e continuità operativa · attivo · Un backup non testato è un'ipotesi. Contro il ransomware serve almeno una copia che l'attaccante non possa cancellare né cifrare.
- 25-sicurezza-web/10-operazioni/gestione-errori.md · Gestione degli errori e delle condizioni eccezionali · attivo · Nuova categoria della OWASP Top 10:2025 (A10).
- 25-sicurezza-web/10-operazioni/incident-response.md · Risposta agli incidenti · attivo · Il piano si scrive prima dell'incidente.
- 25-sicurezza-web/10-operazioni/logging-e-alert.md · Logging, monitoraggio e alert · attivo · Il nome della categoria OWASP 2025 è cambiato in Logging and Alerting Failures: un log che nessuno guarda non serve.
- 25-sicurezza-web/10-operazioni/vulnerability-disclosure.md · Divulgazione delle vulnerabilità (security.txt, VDP) · attivo · Chi trova un problema nel tuo sito deve sapere a chi dirlo e sentirsi al sicuro nel farlo.
- 25-sicurezza-web/11-sdlc/README.md · Sdlc · attivo · -
- 25-sicurezza-web/11-sdlc/devsecops.md · DevSecOps — sicurezza nel ciclo di sviluppo · attivo · La sicurezza costa meno quanto prima entra nel processo ("shift left"), ma non finisce al rilascio: serve anche in esercizio ("shield right").
- 25-sicurezza-web/11-sdlc/testing-di-sicurezza.md · Testing di sicurezza · attivo · Nessuno strumento trova tutto. SAST e SCA trovano problemi nel codice e nelle dipendenze, DAST trova problemi nell'applicazione in esecuzione, il pene
- 25-sicurezza-web/12-normativa-ue/README.md · Normativa ue · attivo · -
- 25-sicurezza-web/12-normativa-ue/cyber-resilience-act.md · Cyber Resilience Act (Reg. UE 2024/2847) · attivo · ⚠️ Sintesi orientativa, non consulenza legale.
- 25-sicurezza-web/12-normativa-ue/gdpr.md · GDPR — obblighi di sicurezza per i siti web · attivo · ⚠️ Sintesi orientativa, non consulenza legale.
- 25-sicurezza-web/12-normativa-ue/nis2-italia.md · NIS2 in Italia (D.Lgs. 138/2024) · attivo · ⚠️ Sintesi orientativa, non consulenza legale.
- 25-sicurezza-web/13-ricettario/README.md · Ricettario di configurazioni · attivo · Configurazioni di partenza, pronte da copiare, per gli stack più comuni.
- 25-sicurezza-web/13-ricettario/wordpress-hardening.md · Hardening di WordPress · attivo · La grande maggioranza delle compromissioni WordPress passa da plugin e temi non aggiornati o da credenziali admin deboli.
- 25-sicurezza-web/14-automazione/README.md · Automazione dei controlli · attivo · Strumenti pronti da copiare in qualunque progetto futuro, indipendenti dal linguaggio.
- 25-sicurezza-web/14-automazione/config/README.md · File di configurazione · attivo · -
- 25-sicurezza-web/14-automazione/github/README.md · File per GitHub · attivo · -
- 25-sicurezza-web/14-automazione/github/workflows/README.md · Workflow GitHub Actions · attivo · Workflow GitHub Actions
- 25-sicurezza-web/14-automazione/scripts/README.md · Script · attivo · -
- 25-sicurezza-web/15-modelli/README.md · Modelli di documenti · attivo · Documenti pronti da compilare, validi per qualunque progetto digitale.
- 25-sicurezza-web/15-modelli/piano-risposta-incidenti.md · Piano di risposta agli incidenti di sicurezza · attivo · Riferimenti: incident-response, gdpr, nis2-italia, cyber-resilience-act.
- 25-sicurezza-web/15-modelli/politica-divulgazione.md · Segnalazione responsabile delle vulnerabilità · attivo · Teniamo alla sicurezza dei nostri siti e servizi e a quella delle persone che li usano.
- 25-sicurezza-web/15-modelli/procedura-accessi.md · Procedura di gestione degli accessi · attivo · Si applica a dipendenti, collaboratori, agenzie e fornitori che accedono a domini, hosting, CMS, repository, caselle email, social e strumenti SaaS.
- 25-sicurezza-web/15-modelli/questionario-fornitori.md · Questionario di sicurezza per fornitori · attivo · Le domande hanno un codice (A1, B2…) da citare nelle risposte.
- 25-sicurezza-web/16-progetti/README.md · Progetti · attivo · -
- 25-sicurezza-web/16-progetti/profili-di-progetto.md · Profili di progetto — requisiti in base al tipo · attivo · Quando nasce un nuovo progetto digitale, rispondi alle domande di classificazione: il profilo che ne esce dice quale livello ASVS adottare, quali cont
- 25-sicurezza-web/16-progetti/requisiti-capitolato.md · Requisiti di sicurezza per capitolati e contratti · attivo · ⚠️ Testo tecnico di partenza: le clausole contrattuali (responsabilità, penali, garanzie) vanno validate da un legale.
- 25-sicurezza-web/17-formazione/README.md · Formazione · attivo · -
- 25-sicurezza-web/17-formazione/quiz.md · Quiz di verifica · attivo · Due set: base per tutti, tecnico per chi sviluppa o gestisce i siti.
- 25-sicurezza-web/17-formazione/regole-per-redattori.md · Dieci regole per chi lavora sul sito · attivo · -
- 25-sicurezza-web/README.md · Sicurezza web · attivo · Knowledge base di best practice (aggiornata al 2026) per progettare, sviluppare e gestire siti e applicazioni web sicuri.
- 25-sicurezza-web/changelog.md · Changelog · attivo · Formato ispirato a Keep a Changelog. Versionamento: MAJOR.MINOR.PATCH
- 25-sicurezza-web/checklist/README.md · Checklist · attivo · -
- 25-sicurezza-web/checklist/pre-lancio.md · Checklist pre-lancio · attivo · Da completare prima di mettere online un sito o una nuova versione importante.
- 25-sicurezza-web/checklist/revisione-periodica.md · Checklist di revisione periodica · attivo · La sicurezza di un sito decade nel tempo anche senza toccare il codice: escono nuove vulnerabilità, scadono certificati, restano account di persone ch
- 25-sicurezza-web/contribuire.md · Come aggiornare questa knowledge base · attivo · -
- 25-sicurezza-web/fonti.md · Fonti · attivo · Nota sull'affidabilità. Durante la revisione 1.2.0 una fonte secondaria ([UNVEIL-PQ]) è risultata in contrasto con il sorgente ufficiale di Go.

## 30-conoscenza

- 30-conoscenza/README.md · Conoscenza · attivo · Come si raccolgono, organizzano e ritrovano note e appunti.
- 30-conoscenza/second-brain.md · Second brain · attivo · Struttura, strumenti e regole del second brain

## 40-procedure

- 40-procedure/README.md · Procedure · attivo · Istruzioni passo-passo per le attività ricorrenti.
- 40-procedure/aggiornare-la-documentazione.md · Aggiornare la documentazione · attivo · Aggiungere o modificare un documento in questo repository
- 40-procedure/collegare-le-repo-al-grafo.md · Collegare le repo al grafo · attivo · Come una repo entra nel grafo del second brain, e i due token facoltativi per le repo private e per l'aggiornamento immediato.
- 40-procedure/lavorare-online.md · Lavorare online · attivo · Usare github.dev, Codespaces e Cloud Shell
- 40-procedure/nuovo-progetto.md · Nuovo progetto · attivo · Creare la repo di un progetto nuovo con la struttura standard: decisioni, indici automatici, controlli e collegamento al grafo.
- 40-procedure/usare-il-second-brain.md · Usare il second brain · attivo · App web (consigliata), Foam nel browser, Obsidian sul telefono, routine

## 50-progetti

- 50-progetti/README.md · Progetti · attivo · Una scheda per ogni progetto: obiettivo, stato, responsabili, link al repository di codice.
- 50-progetti/ambiente-di-lavoro-cloud.md · Ambiente di lavoro cloud · attivo · Mettere in opera GitHub, Codespaces e second brain

## 90-archivio

- 90-archivio/README.md · Archivio · attivo · Documenti superati o chiusi. Non si cancella nulla: si archivia.

## (radice)

- README.md · Documentazione — Volta la carta · - · Questa è la fonte unica di verità della documentazione generale.
