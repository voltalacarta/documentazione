// =====================================================================
// Next.js (App Router) — CSP con nonce e header di sicurezza (rev. 2026-10-15)
// Basato sulla guida ufficiale "Content Security Policy" di Next.js
// (aggiornata a marzo 2026).
//
// NOME DEL FILE:
//   - Next.js 16+: salva come  proxy.ts   nella root (o src/), funzione "proxy"
//   - Next.js ≤15: salva come  middleware.ts, rinomina la funzione in "middleware"
//
// COME FUNZIONA:
//   - genera un nonce nuovo a ogni richiesta;
//   - lo passa a Next.js nell'header di RICHIESTA Content-Security-Policy:
//     Next.js lo estrae e lo applica da solo ai propri script e bundle;
//   - lo espone in "x-nonce" per gli script di terze parti:
//       const nonce = (await headers()).get("x-nonce")
//       <Script src="..." nonce={nonce} />
//
// CONSEGUENZE:
//   - con i nonce TUTTE le pagine devono essere renderizzate dinamicamente
//     (niente static generation, ISR, PPR, cache CDN delle pagine). Se serve,
//     forzalo con:  await connection()  (da "next/server") nella pagina.
//   - Alternativa che preserva il rendering statico: CSP con hash tramite
//     l'opzione sperimentale  experimental.sri  in next.config.js.
// =====================================================================
import { NextResponse, type NextRequest } from "next/server";

// Metti a false dopo aver verificato i report: passa da Report-Only a enforce
const SOLO_REPORT = true;

export function proxy(request: NextRequest) {
  const nonce = Buffer.from(crypto.randomUUID()).toString("base64");
  const isDev = process.env.NODE_ENV === "development";

  const csp = [
    "default-src 'self'",
    // React in sviluppo usa eval per il debug; in produzione non serve
    `script-src 'self' 'nonce-${nonce}' 'strict-dynamic'${isDev ? " 'unsafe-eval'" : ""}`,
    `style-src 'self' ${isDev ? "'unsafe-inline'" : `'nonce-${nonce}'`}`,
    "img-src 'self' blob: data:",
    "font-src 'self'",
    "object-src 'none'",
    "base-uri 'self'",
    "form-action 'self'",
    "frame-ancestors 'none'",
    "upgrade-insecure-requests",
  ].join("; ");

  // Header di richiesta: è da qui che Next.js legge il nonce
  const requestHeaders = new Headers(request.headers);
  requestHeaders.set("x-nonce", nonce);
  requestHeaders.set("Content-Security-Policy", csp);

  const response = NextResponse.next({ request: { headers: requestHeaders } });

  response.headers.set(SOLO_REPORT ? "Content-Security-Policy-Report-Only" : "Content-Security-Policy", csp);
  response.headers.set("Strict-Transport-Security", "max-age=63072000; includeSubDomains");
  response.headers.set("X-Content-Type-Options", "nosniff");
  response.headers.set("Referrer-Policy", "strict-origin-when-cross-origin");
  response.headers.set("Cross-Origin-Opener-Policy", "same-origin");
  response.headers.set("Permissions-Policy", "camera=(), microphone=(), geolocation=(), payment=(), usb=()");
  response.headers.set("X-Frame-Options", "DENY");
  return response;
}

// Esclude API, asset statici e prefetch di next/link (come da documentazione)
export const config = {
  matcher: [
    {
      source: "/((?!api|_next/static|_next/image|favicon.ico).*)",
      missing: [
        { type: "header", key: "next-router-prefetch" },
        { type: "header", key: "purpose", value: "prefetch" },
      ],
    },
  ],
};

// In next.config.js aggiungi anche:
//   poweredByHeader: false,
//   productionBrowserSourceMaps: false,
// Le API escluse dal matcher vanno protette a parte (autenticazione, CORS, rate limit).
