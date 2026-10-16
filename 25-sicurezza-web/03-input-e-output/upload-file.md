---
titolo: Upload e gestione dei file
stato: attivo
creato: 2026-10-15
aggiornato: 2026-10-16
tag: [sicurezza-web, input-e-output]
prossima_revisione: 2027-04-15
owasp: [A05:2025, A01:2025]
asvs: [V5]
---

# Upload e gestione dei file

> **In sintesi.** Un file caricato può essere codice eseguibile, una XSS travestita da immagine, una bomba di decompressione o un path traversal. Va validato, rinominato, conservato fuori dalla web root e servito da un'origine separata.

## Pratiche

### 🔴 Obbligatorio

- **Allowlist** delle estensioni e verifica del tipo reale (magic bytes, es. `libmagic`), non del `Content-Type` dichiarato dal client.
- **Limite di dimensione** lato server (anche a livello di reverse proxy).
- **Rinomina** con un identificativo casuale; il nome originale va solo nei metadati, sanitizzato.
- Conserva **fuori dalla web root** o su object storage (S3, R2, GCS) senza permessi di esecuzione.
- Mai usare input utente per costruire percorsi (`../../etc/passwd`): normalizza e verifica che il percorso finale resti nella directory prevista.
- Download con `Content-Disposition: attachment` e `X-Content-Type-Options: nosniff`.

### 🟠 Raccomandato

- Servi i file caricati da un **dominio separato** (es. `usercontent.example-cdn.net`) così una eventuale XSS non accede ai cookie del sito principale.
- **Ri-codifica le immagini** (es. con libvips/Sharp) per eliminare payload e metadati EXIF (anche per privacy: geolocalizzazione).
- SVG: trattali come HTML (contengono script). Sanitizza o converti in PNG.
- Scansione antimalware (ClamAV o servizio cloud) per file che altri utenti scaricheranno.
- Archivi ZIP: limita numero di file, dimensione decompressa e profondità; attenzione allo *zip slip*.
- URL di download firmati e a scadenza (pre-signed URL) per file privati.

### 🟢 Avanzato

- Elaborazione (thumbnail, conversione documenti, PDF) in sandbox isolata: librerie come ImageMagick e Ghostscript hanno una lunga storia di vulnerabilità.

## Fonti

- [OWASP-ASVS] (capitolo V5) — vedi [fonti.md](../fonti.md)
