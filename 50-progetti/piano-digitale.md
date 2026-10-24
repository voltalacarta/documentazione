---
titolo: Piano digitale di Volta la carta
stato: bozza
creato: 2026-10-24
aggiornato: 2026-10-24
tag: [progetti, piano, vendite, crm, email, gestionale]
sintesi: "Proposta degli strumenti oltre al sito (pagamenti, ordini, CRM, email, pannello prodotti, fatture, numeri) ordinati per impatto sulle vendite."
collegati: [0009]
---

# Piano digitale di Volta la carta

Proposta da discutere. Obiettivo, dalla decisione [0009](../10-decisioni/0009-rifare-i-siti-rilegaretesi-it-e-voltalacarta-it-per-vendere.md): vendere di più nei prossimi 5 anni, partendo subito. Ogni voce è giudicata su tre domande: fa vendere di più? fa risparmiare tempo? fa lavorare meglio?

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
| **Consegna urgente** a pagamento | Chi è in ritardo paga volentieri per la velocità | 1 |
| Ritiro in bottega a Ferrara | Risparmio per gli studenti di Unife; li porta in negozio | 1 |
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

Assistenza: WhatsApp Business con risposte pronte per le domande frequenti, e una casella condivisa per info@.

### 4. Bottega e spedizioni

- **Scheda di lavorazione** stampabile, una per ordine, ordinata per scadenza.
- **Etichette di spedizione** generate dall'ordine (servizi come Sendcloud o l'integrazione del corriere che usate), con tracciamento inviato in automatico.
- **Scorte dei materiali**: quante copertine per colore sono rimaste; sotto la soglia arriva un avviso e, a zero, il colore sparisce dal sito.

### 5. Fatture e conti

- Fatturazione elettronica collegata ai pagamenti (es. Fatture in Cloud o il programma che usate già): ogni ordine pagato genera fattura o corrispettivo.
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
- Volti e mani della bottega sul sito: chi compra una cosa fatta a mano vuole vedere chi la fa.

### 8. Volta la carta

Restyling di voltalacarta.it con lo stesso sistema grafico: catalogo della casa editrice, modulo d'ordine per le librerie, rimando a rilegaretesi per le tesi. In fase 3, dopo che rilegaretesi vende.

### 9. Sicurezza e continuità

Applicare le regole in [25-sicurezza-web](../25-sicurezza-web/) e [backup e continuità](../25-sicurezza-web/10-operazioni/backup-e-continuita.md): accessi personali per ognuno, verifica in due passaggi ovunque, backup del Registro e degli ordini, privacy policy aggiornata.

## Fasi

| Fase | Contenuto | Obiettivo |
| --- | --- | --- |
| 1 · Lancio | Pagamento, caricamento PDF con conteggio facciate, ordini nel Registro e su Drive, email di stato, urgente, ritiro in bottega, extra, recensioni, fatturazione, statistiche | Il nuovo sito sostituisce il vecchio prima della prossima sessione di laurea |
| 2 · Crescita | CRM e automazioni (auguri, magistrale, carrello), pagine per ateneo e guide, codici sconto, scheda di lavorazione, etichette, cruscotto | Più clienti da Google e dal passaparola, meno lavoro manuale |
| 3 · Consolidamento | Buono regalo, scorte, galleria, restyling di voltalacarta.it, ordini delle librerie | Il sistema regge anche la casa editrice |

## Domande aperte

1. Chi gestisce gli ordini ogni giorno, e da dove (computer in bottega, telefono)?
2. Quale corriere usate oggi, e con quale contratto?
3. Con cosa fate oggi le fatture elettroniche?
4. Su quale servizio sono le caselle email di rilegaretesi.it e voltalacarta.it?
5. Quando cade la prossima sessione di laurea importante per voi? È la scadenza della fase 1.
6. Che budget mensile è accettabile per i servizi esterni?
