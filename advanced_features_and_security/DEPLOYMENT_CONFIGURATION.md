# Deployment Instructions

1. Install SSL certificate (Let’s Encrypt or commercial SSL) on web server.
2. Configure Apache/Nginx to serve Django project over HTTPS.
3. Ensure that `SECURE_SSL_REDIRECT = True` and secure cookie settings are enabled in `settings.py`.
4. Optionally, enable HSTS headers at the web server level for additional security.
