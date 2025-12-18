# HTTPS and Secure Redirects Implementation

## SECURE_SSL_REDIRECT
- Redirects all HTTP requests to HTTPS to ensure encrypted communication.

## SECURE_HSTS_SECONDS, SECURE_HSTS_INCLUDE_SUBDOMAINS, SECURE_HSTS_PRELOAD
- Implements HTTP Strict Transport Security (HSTS) to tell browsers to only use HTTPS for this site and all subdomains.
- Preloading allows browsers to remember this rule even before visiting the site.

## SESSION_COOKIE_SECURE and CSRF_COOKIE_SECURE
- Ensures that sensitive cookies are only sent over HTTPS.

## X_FRAME_OPTIONS
- Set to 'DENY' to prevent clickjacking attacks.

## SECURE_CONTENT_TYPE_NOSNIFF
- Prevents browsers from MIME-sniffing responses, reducing XSS risk.

## SECURE_BROWSER_XSS_FILTER
- Enables browser XSS protection mechanisms.

## Deployment Notes
- Ensure that the web server (Apache/Nginx) is configured with valid SSL/TLS certificates.
- Redirect all HTTP traffic to HTTPS at the server level as an additional layer of security.
