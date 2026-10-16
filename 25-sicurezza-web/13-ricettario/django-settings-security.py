# =====================================================================
# Django — impostazioni di sicurezza per settings.py (rev. 2026-10-15)
# Verifica con: python manage.py check --deploy
# Django 6.0+ include il supporto CSP nativo (verificato sulla documentazione
# ufficiale 6.0). Per versioni precedenti usa il pacchetto django-csp.
# =====================================================================
import os

from django.utils.csp import CSP  # Django 6.0+

# --- Content Security Policy nativa ---
# Aggiungi a MIDDLEWARE:
#   "django.middleware.csp.ContentSecurityPolicyMiddleware",
# e a TEMPLATES[0]["OPTIONS"]["context_processors"]:
#   "django.template.context_processors.csp",
# Nei template:  <script nonce="{{ csp_nonce }}">...</script>

# Policy di base, applicata (non rompe quasi nulla)
SECURE_CSP = {
    "frame-ancestors": [CSP.SELF],
    "object-src": [CSP.NONE],
    "base-uri": [CSP.SELF],
    "form-action": [CSP.SELF],
}

# Policy strict in osservazione: portala in SECURE_CSP dopo aver letto i report
SECURE_CSP_REPORT_ONLY = {
    "script-src": [CSP.NONCE, CSP.STRICT_DYNAMIC],
    "object-src": [CSP.NONE],
    "base-uri": [CSP.NONE],
    # "report-uri": "https://example.it/csp-report/",
}

DEBUG = False
SECRET_KEY = os.environ["DJANGO_SECRET_KEY"]          # mai nel codice
ALLOWED_HOSTS = ["example.it", "www.example.it"]

# --- HTTPS e HSTS ---
SECURE_SSL_REDIRECT = True
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")  # solo se dietro proxy fidato
SECURE_HSTS_SECONDS = 63072000
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = False   # True solo dopo verifica dei sottodomini

# --- Cookie ---
SESSION_COOKIE_SECURE = True
SESSION_COOKIE_HTTPONLY = True
SESSION_COOKIE_SAMESITE = "Lax"
SESSION_COOKIE_AGE = 8 * 3600
CSRF_COOKIE_SECURE = True
CSRF_COOKIE_SAMESITE = "Lax"
CSRF_TRUSTED_ORIGINS = ["https://example.it", "https://www.example.it"]

# --- Header ---
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_REFERRER_POLICY = "strict-origin-when-cross-origin"
SECURE_CROSS_ORIGIN_OPENER_POLICY = "same-origin"
X_FRAME_OPTIONS = "SAMEORIGIN"

# --- Password: Argon2 come primo hasher (pip install django[argon2]) ---
PASSWORD_HASHERS = [
    "django.contrib.auth.hashers.Argon2PasswordHasher",
    "django.contrib.auth.hashers.PBKDF2PasswordHasher",  # per ri-hash dei vecchi
]
AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
     "OPTIONS": {"min_length": 15}},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    # Nessun validatore di composizione (maiuscole/simboli): vedi NIST SP 800-63B-4
]

# --- Upload ---
DATA_UPLOAD_MAX_MEMORY_SIZE = 2_621_440   # 2,5 MB
FILE_UPLOAD_MAX_MEMORY_SIZE = 2_621_440
FILE_UPLOAD_PERMISSIONS = 0o640

# --- Permissions-Policy: aggiungila con un middleware o nel reverse proxy ---
