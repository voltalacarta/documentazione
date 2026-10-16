// =====================================================================
// Node.js / Express — middleware di sicurezza (rev. 2026-10-15)
// Dipendenze: npm i helmet express-rate-limit
// =====================================================================
import crypto from "node:crypto";
import express from "express";
import helmet from "helmet";
import rateLimit from "express-rate-limit";

const app = express();

app.disable("x-powered-by");
app.set("trust proxy", 1); // se dietro un solo proxy/CDN: serve per IP corretti nel rate limit

// Nonce per richiesta, da usare nei template: <script nonce="<%= nonce %>">
app.use((req, res, next) => {
  res.locals.nonce = crypto.randomBytes(16).toString("base64");
  next();
});

app.use(
  helmet({
    contentSecurityPolicy: {
      useDefaults: false,
      directives: {
        "script-src": [(req, res) => `'nonce-${res.locals.nonce}'`, "'strict-dynamic'"],
        "object-src": ["'none'"],
        "base-uri": ["'none'"],
        "frame-ancestors": ["'self'"],
        "form-action": ["'self'"],
        "upgrade-insecure-requests": [],
      },
      // Metti a false dopo aver verificato i report
      reportOnly: true,
    },
    strictTransportSecurity: { maxAge: 63072000, includeSubDomains: true },
    referrerPolicy: { policy: "strict-origin-when-cross-origin" },
    crossOriginOpenerPolicy: { policy: "same-origin" },
    xFrameOptions: { action: "sameorigin" },
  })
);

app.use((req, res, next) => {
  res.setHeader("Permissions-Policy", "camera=(), microphone=(), geolocation=(), payment=(), usb=()");
  next();
});

// Limiti sul corpo delle richieste
app.use(express.json({ limit: "100kb" }));
app.use(express.urlencoded({ extended: false, limit: "100kb" }));

// Rate limiting mirato su autenticazione
const authLimiter = rateLimit({
  windowMs: 15 * 60 * 1000,
  limit: 10,
  standardHeaders: "draft-7",
  legacyHeaders: false,
});
app.use(["/login", "/password-reset", "/otp"], authLimiter);

// Cookie di sessione (es. con express-session):
// cookie: { httpOnly: true, secure: true, sameSite: "lax", maxAge: 8 * 3600 * 1000 }
// name: "__Host-session", e rigenera la sessione al login: req.session.regenerate(...)

// Gestore errori globale: niente dettagli all'utente
// eslint-disable-next-line no-unused-vars
app.use((err, req, res, next) => {
  const id = crypto.randomUUID();
  console.error({ id, err }); // usa un logger strutturato in produzione
  res.status(err.status && err.status < 500 ? err.status : 500).json({
    errore: "Si è verificato un problema. Codice di riferimento: " + id,
  });
});

export default app;
