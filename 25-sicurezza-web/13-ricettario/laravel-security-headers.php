<?php
// =====================================================================
// Laravel — middleware App\Http\Middleware\SecurityHeaders (rev. 2026-10-15)
// Copiare come app/Http/Middleware/SecurityHeaders.php
// Registrazione (Laravel 11+), in bootstrap/app.php:
//   ->withMiddleware(function (Middleware $m) {
//       $m->append(\App\Http\Middleware\SecurityHeaders::class);
//   })
// Nei Blade: <script nonce="{{ Vite::cspNonce() }}"> ; per Vite usa
//   Vite::useCspNonce() prima del render (es. in questo middleware).
// In .env di produzione: APP_DEBUG=false, SESSION_SECURE_COOKIE=true,
//   SESSION_SAME_SITE=lax, SESSION_HTTP_ONLY=true
// =====================================================================

namespace App\Http\Middleware;

use Closure;
use Illuminate\Http\Request;
use Illuminate\Support\Facades\Vite;
use Symfony\Component\HttpFoundation\Response;

class SecurityHeaders
{
    public function handle(Request $request, Closure $next): Response
    {
        Vite::useCspNonce();
        $nonce = Vite::cspNonce();

        /** @var Response $response */
        $response = $next($request);

        $strict = "script-src 'nonce-{$nonce}' 'strict-dynamic'; object-src 'none'; base-uri 'none'";
        $base   = "frame-ancestors 'self'; object-src 'none'; base-uri 'self'; form-action 'self'; upgrade-insecure-requests";

        $response->headers->set('Content-Security-Policy', $base);
        // Porta $strict in enforce dopo aver verificato i report
        $response->headers->set('Content-Security-Policy-Report-Only', $strict);
        $response->headers->set('Strict-Transport-Security', 'max-age=63072000; includeSubDomains');
        $response->headers->set('X-Content-Type-Options', 'nosniff');
        $response->headers->set('Referrer-Policy', 'strict-origin-when-cross-origin');
        $response->headers->set('Cross-Origin-Opener-Policy', 'same-origin');
        $response->headers->set('Permissions-Policy', 'camera=(), microphone=(), geolocation=(), payment=(), usb=()');
        $response->headers->set('X-Frame-Options', 'SAMEORIGIN');
        $response->headers->remove('X-Powered-By');

        return $response;
    }
}
