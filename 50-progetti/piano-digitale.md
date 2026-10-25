---
titolo: Piano digitale di Volta la carta
stato: bozza
creato: 2026-10-24
aggiornato: 2026-10-25
tag: [progetti, piano, vendite, crm, email, gestionale]
sintesi: "Proposta degli strumenti oltre al sito (pagamenti, ordini, CRM, email, pannello prodotti, fatture, numeri) ordinati per impatto sulle vendite."
collegati: [0009]
---

# Piano digitale di Volta la carta

Proposta da discutere. Obiettivo, dalla decisione [0009](../10-decisioni/0009-rifare-i-siti-rilegaretesi-it-e-voltalacarta-it-per-vendere.md): vendere di più nei prossimi 5 anni, partendo subito. Ogni voce è giudicata su tre domande: fa vendere di più? fa risparmiare tempo? fa lavorare meglio?

Le risposte del titolare al questionario del 25/10/2026 sono in [Volta la carta, conoscenza dell'attività](../30-conoscenza/volta-la-carta/README.md): partire da lì.

Principio guida: **pochi strumenti, collegati tra loro**. Il Registro VLC (Google Sheets) resta il centro: prodotti, prezzi, ordini e clienti stanno lì o si vedono da lì. Si aggiunge un servizio esterno solo quando il foglio non basta.

## Il flusso di un ordine, da come sarà

1. Il cliente configura la tesi e **carica il PDF**: il sito conta da solo le facciate e mostra in anteprima il suo vero frontespizio sulla copertina.
2. Paga con carta, Apple Pay, Google Pay o PayPal.
3. L'ordine compare nella scheda *Ordini* del Registro; il PDF finisce in `ProduzioneVLC/Rilegaretesi/Ordini/AAAA-MM/` con il numero d'ordine.
4. In bottega si stampa la **scheda di lavorazione** del giorno: copertina, colore della scritta, facciate, scadenza, codice QR che apre il PDF.
5. Cambiando lo stato nel foglio (*In stampa*, *Spedito*…) il cliente riceve l'email giusta, con il codice di tracciamento.
6. Dopo la consegna parte la richiesta di recensione; il giorno della laurea, gli auguri.
7. La fattura elettronica parte da sola verso lo SdI.

## Le aree

### 1. Vendita online (sito rilegaretesi.it)

| Cosa | Perché | Fase |
| --- | --- | --- |
| Pagamento online (es. Stripe: carte, Apple/Google Pay; PayPal) | Senza non si vende | 1 |
| Caricamento PDF con conteggio automatico delle facciate | Niente errori sul prezzo, meno email di chiarimento | 1 |
| Anteprima con il vero frontespizio del cliente | Fa decidere più in fretta: si vede la propria tesi | 1 |
| Calcolo della data di consegna ("ti arriva entro giovedì 13") con festivi | Il cliente ha una scadenza: dirgli che ce la fa vende | 1 |
| **Ordine entro le 12, spedizione in giornata** in evidenza (oggi gratis; un sovrapprezzo si valuta col titolare) | Chi è in ritardo cerca proprio questo | 1 |
| Limite di ordini al giorno, con la prima data di spedizione libera | Le tesi le fa una persona sola: 20-25 al giorno | 1 |
| Dati per la fattura elettronica (P.IVA, codice destinatario) | Clienti con partita IVA ed enti pubblici sono frequenti | 1 |
| Ritiro in bottega a Ferrara (già possibile, da dire sul sito) | Risparmio per gli studenti di Unife; li porta in negozio | 1 |
| Extra all'ordine: copia in più per genitori o relatore, carta più pesante, confezione regalo, biglietto | Aumenta lo scontrino medio | 1 |
| Recensioni vere, chieste dopo la consegna, mostrate sul sito e su Google | Fiducia: oggi il sito non ne ha | 1 |
| Pagine per città e ateneo ("rilegatura tesi Bologna") e guide (frontespizio, impaginazione) | Visite da Google senza pagare pubblicità | 2 |
| Modelli di frontespizio scaricabili per ateneo, in cambio dell'email | Contatti da ricontattare prima della laurea | 2 |
| Codici sconto per associazioni studentesche, copisterie, "porta un amico" | Passaparola misurabile | 2 |
| Buono regalo "regala la rilegatura" (per genitori e nonni) | Nuovo pubblico | 3 |

### 2. Pannello prodotti

Proposta: **il Registro VLC è il pannello**. Si aggiunge una copertina con una riga, si cambia un prezzo in una cella, si toglie la spunta *Disponibile* quando un colore finisce. Il sito si aggiorna da solo (sincronizzazione automatica ogni ora, o con un pulsante).

- Foto: si caricano in una cartella Drive con il nome del codice (`CP-030.jpg`) e il sito le prende da lì.
- Un controllo automatico avvisa se una riga ha errori (prezzo mancante, finitura sconosciuta) prima che vada online.
- Più avanti, se serve, un modulo semplice da telefono per chi aggiorna stando in bottega.

Alternativa scartata per ora: un CMS o un pannello su misura. Costa tempo da mantenere e il foglio fa già tutto.

### 3. Clienti (CRM) ed email

Proposta: un servizio europeo per email e contatti (es. **Brevo**: conforme al GDPR, piano gratuito per iniziare, email automatiche e newsletter nello stesso posto).

Email automatiche:

| Momento | Email |
| --- | --- |
| Ordine pagato | Conferma con riepilogo e data di consegna prevista |
| In lavorazione | "La tua tesi è sul banco" (con una foto della bottega) |
| Spedito | Codice di tracciamento |
| Consegnato + 2 giorni | Richiesta di recensione |
| Giorno della laurea (se lo indica) | Auguri da Volta la carta |
| Laurea triennale + circa 2 anni | Promemoria per la magistrale, con sconto da cliente |
| Carrello abbandonato | Promemoria entro 24 ore |

Scheda cliente: nome, email, ateneo, corso, data di laurea, ordini, recensione lasciata. Con il consenso giusto per il marketing, separato da quello per l'ordine.

Email del dominio: configurare SPF, DKIM e DMARC su rilegaretesi.it e voltalacarta.it, altrimenti le email automatiche finiscono nello spam.

Assistenza: una casella condivisa per info@ con risposte pronte per le domande frequenti. **WhatsApp no**: il titolare preferisce l'email.

### 4. Bottega e spedizioni

- **Scheda di lavorazione** ed **elenco del giorno stampabili**, ordinati per data di laurea: l'elenco resta su carta, uno schermo in laboratorio non serve.
- **Etichette di spedizione** generate dall'ordine per **GLS** (oggi si fanno a mano sul sito del corriere), con tracciamento inviato in automatico.
- **Scorte dei materiali**: quante copertine per colore sono rimaste; sotto la soglia arriva un avviso e, a zero, il colore sparisce dal sito.

### 5. Fatture e conti

- Fatturazione elettronica collegata ai pagamenti: oggi si usa **Konga Lite** (circa 20 ore al mese tra fatture e conti). Prima strada: un'esportazione degli ordini pronta da importare; se non basta, valutare un programma collegabile.
- Riconciliazione dei pagamenti in un foglio mensile.

### 6. Numeri

Un cruscotto con poche cifre, aggiornato da solo:

- ordini e incasso per settimana, confrontati con l'anno prima;
- scontrino medio e quanti aggiungono extra;
- copertine più vendute e margine per finitura (prezzo meno costo del materiale);
- da dove arrivano i clienti e quanti, tra chi apre il configuratore, ordinano;
- andamento attorno alle sessioni di laurea, per preparare materiali e personale.

Statistiche del sito con uno strumento senza cookie (es. Plausible o Umami): niente banner, dati affidabili.

### 7. Apprezzare il proprio lavoro

- **Galleria delle tesi rilegate** (con il permesso dei clienti): portfolio sul sito e materiale per i social, senza fatica.
- **Riepilogo della settimana** per chi lavora in bottega: tesi consegnate, recensioni ricevute, frasi dei clienti.
- Le mani e le lavorazioni sul sito (scritta in oro, incollaggio), su copertine di prova e con la musica del titolare: nessuno vuole mostrare il volto, ma il lavoro a mano si vede lo stesso.

### 8. Volta la carta

Restyling di voltalacarta.it con lo stesso sistema grafico: catalogo della casa editrice, modulo d'ordine per le librerie, rimando a rilegaretesi per le tesi. In fase 3, dopo che rilegaretesi vende.

### 9. Sicurezza e continuità

Applicare le regole in [25-sicurezza-web](../25-sicurezza-web/) e [backup e continuità](../25-sicurezza-web/10-operazioni/backup-e-continuita.md): accessi personali per ognuno, verifica in due passaggi ovunque, backup del Registro e degli ordini, privacy policy aggiornata.

## Fasi

| Fase | Contenuto | Obiettivo |
| --- | --- | --- |
| 1 · Lancio | Pagamento, caricamento PDF con conteggio facciate e controllo del file, ordini nel Registro e su Drive, email di stato, spedizione in giornata, limite giornaliero, ritiro in bottega, extra, recensioni, dati per la fattura, statistiche | **Online entro metà gennaio 2027**, prima del picco di febbraio e marzo |
| 2 · Crescita | CRM e automazioni (auguri, magistrale, carrello), pagine per ateneo e guide, codici sconto, scheda di lavorazione, etichette, cruscotto | Più clienti da Google e dal passaparola, meno lavoro manuale |
| 3 · Consolidamento | Buono regalo, scorte, galleria, restyling di voltalacarta.it, ordini delle librerie | Il sistema regge anche la casa editrice |

## Risposte del titolare (25/10/2026)

| Domanda | Risposta |
| --- | --- |
| Chi gestisce gli ordini ogni giorno, e da dove? | Il titolare, dal computer del negozio; per il sito il referente è Piex |
| Quale corriere? | GLS, etichette fatte sul sito del corriere |
| Con cosa si fanno le fatture? | Konga Lite |
| Dove sono le caselle email? | Gmail e Libero |
| Prossimo picco di lauree | Febbraio-marzo, poi ottobre-dicembre |
| Budget mensile | Non indicato. Vincolo: non fare debiti e non spendere troppo |

## Domande aperte

Vedi l'elenco in [Volta la carta, conoscenza dell'attività](../30-conoscenza/volta-la-carta/README.md#domande-ancora-aperte).
