---
titolo: Hardening di WordPress
stato: attivo
creato: 2026-10-15
aggiornato: 2026-10-16
tag: [sicurezza-web, ricettario]
prossima_revisione: 2027-01-15
owasp: [A02:2025, A03:2025, A07:2025]
---

# Hardening di WordPress

> **In sintesi.** La grande maggioranza delle compromissioni WordPress passa da plugin e temi non aggiornati o da credenziali admin deboli. Le prime tre voci contano più di tutto il resto. Principi generali in [cms-e-hosting](../09-infrastruttura/cms-e-hosting.md).

## Le tre cose che contano di più

1. 🔴 **Aggiornamenti automatici** di core, plugin e temi (Bacheca → Aggiornamenti, o per singolo plugin "Abilita aggiornamenti automatici").
2. 🔴 **MFA/passkey** per tutti gli account con ruolo Editor o superiore (plugin come *Two Factor* o soluzioni con passkey).
3. 🔴 **Meno plugin possibile**, solo da autori affidabili; rimuovi quelli disattivati. Mai versioni "nulled".

## wp-config.php

```php
// Chiavi e salt unici: generali su https://api.wordpress.org/secret-key/1.1/salt/
define('DISALLOW_FILE_EDIT', true);     // niente editor di file dal pannello
define('FORCE_SSL_ADMIN', true);
define('WP_DEBUG', false);
define('WP_DEBUG_DISPLAY', false);
define('WP_AUTO_UPDATE_CORE', true);    // anche le major
// define('DISALLOW_FILE_MODS', true);  // blocca installazioni dal pannello: solo se aggiorni via deploy
```

- 🟠 Sposta `wp-config.php` una cartella sopra la root pubblica, se l'hosting lo consente.
- 🟠 Prefisso tabelle diverso da `wp_` sulle nuove installazioni (difesa minore, ma gratuita).
- 🔴 Utente del database con permessi solo sul proprio database.

## functions.php (o plugin "must-use")

```php
// Disattiva XML-RPC se non usi app mobili o Jetpack
add_filter('xmlrpc_enabled', '__return_false');

// Nasconde la versione di WordPress
remove_action('wp_head', 'wp_generator');

// Limita l'enumerazione degli utenti via REST per i visitatori anonimi
add_filter('rest_endpoints', function ($endpoints) {
    if (!is_user_logged_in()) {
        unset($endpoints['/wp/v2/users'], $endpoints['/wp/v2/users/(?P<id>[\d]+)']);
    }
    return $endpoints;
});
```

## .htaccess

- Usa [apache.htaccess](apache.htaccess), che blocca anche `wp-config.php`, `readme.html`, `license.txt`.
- 🔴 In `wp-content/uploads/.htaccess` blocca l'esecuzione di PHP (snippet nel file).

## Account e ruoli

- 🔴 Nessun utente chiamato `admin`; un account per persona, mai condiviso.
- 🟠 Ruolo minimo necessario: i redattori sono *Editor* o *Author*, non *Administrator*.
- 🔴 Rimuovi subito gli account di collaboratori che hanno terminato.
- 🟠 Limite ai tentativi di login (plugin o WAF).

## Protezione e monitoraggio

- 🟠 WAF: quello del CDN (es. Cloudflare) o un plugin di sicurezza con firewall applicativo.
- 🟠 Avvisi sulle vulnerabilità dei plugin installati (Wordfence Intelligence, Patchstack, WPScan).
- 🔴 Backup automatici **fuori dal server** con ripristino testato.

## Verifica

```bash
# Scansione esterna (WPScan, richiede token gratuito per il database vulnerabilità)
wpscan --url https://example.it --enumerate vp,vt,u --api-token $WPSCAN_TOKEN
```
