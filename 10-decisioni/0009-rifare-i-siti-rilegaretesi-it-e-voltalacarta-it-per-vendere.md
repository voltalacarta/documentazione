---
titolo: Rifare i siti rilegaretesi.it e voltalacarta.it per vendere di più
stato: accettato
creato: 2026-10-24
aggiornato: 2026-10-24
tag: [decisioni, siti, rilegaretesi, voltalacarta, obiettivi]
sintesi: "Rilegaretesi.it si rifà da zero, voltalacarta.it riceve un restyling pesante; obiettivo: vendere di più nei prossimi 5 anni, partendo subito."
collegati: [0001]
---

# 0009 · Rifare i siti rilegaretesi.it e voltalacarta.it per vendere di più

## Contesto

Il sito attuale di rilegaretesi.it (WordPress, Elementor, WooCommerce) ha problemi che frenano le vendite: la pagina dello shop è esclusa da Google (`noindex`), titoli e descrizioni sono vuoti o incoerenti, le promesse sulla spedizione si contraddicono e manca una home che racconti qualità ed esperienza. Anche voltalacarta.it ha pagine di prova pubbliche e cataloghi tesi duplicati. Analisi del 13/10/2026.

## Decisione

- **rilegaretesi.it** si rifà da zero. Il codice vive nella repo [`voltalacarta/rt2`](https://github.com/voltalacarta/rt2).
- **voltalacarta.it** riceve un restyling pesante, mantenendo la casa editrice come contenuto principale.
- **Obiettivo** dei due siti per i prossimi 5 anni: vendere di più. Si parte il prima possibile, quindi le correzioni rapide hanno la precedenza sulla perfezione.
- Prezzi e catalogo stanno nel *Registro VLC* (Google Sheets, `ProduzioneVLC` su Drive).
- Ancora da decidere: tecnologia, chi aggiorna i contenuti, stile grafico.

## Alternative considerate

| Alternativa | Perché scartata |
| --- | --- |
| Ritoccare solo il sito attuale di rilegaretesi.it | I problemi riguardano struttura, SEO e configuratore: un ritocco non basta per crescere |
| Rifare da zero anche voltalacarta.it | Il sito ha già contenuti validi (catalogo editoriale): basta un restyling |
| Unire i due siti in uno | Rilegaretesi è un marchio riconoscibile con un pubblico diverso (studenti) |

## Conseguenze

- ✅ Ogni scelta successiva (tecnologia, stile, contenuti) si misura su un criterio solo: fa vendere di più?
- ✅ Catalogo e prezzi in un unico Registro, aggiornabile senza toccare il codice.
- ⚠️ Due cantieri insieme: rilegaretesi.it ha la priorità perché porta gli ordini online.
- ⚠️ Finché il nuovo sito non è online, conviene correggere subito i problemi gravi di quello attuale (noindex, titoli).
