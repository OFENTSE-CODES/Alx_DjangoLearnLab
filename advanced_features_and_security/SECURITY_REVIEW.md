 HTTPS Enforcement
- `SECURE_SSL_REDIRECT = True`: All HTTP traffic is redirected to HTTPS.
- Nginx configuration redirects all HTTP traffic to port 443.

HSTS (HTTP Strict Transport Security)
- `SECURE_HSTS_SECONDS = 31536000`: Browsers enforce HTTPS for 1 year.
- `SECURE_HSTS_INCLUDE_SUBDOMAINS = True`: Applies HSTS to all subdomains.
- `SECURE_HSTS_PRELOAD = True`: Eligible for browser preload lists.

 Secure Cookies
- `SESSION_COOKIE_SECURE = True`: Session cookies sent only over HTTPS.
- `CSRF_COOKIE_SECURE = True`: CSRF tokens only sent over HTTPS.

  Security Headers
- `X_FRAME_OPTIONS = 'DENY'`: Prevents clickjacking.
- `SECURE_CONTENT_TYPE_NOSNIFF = True`: Prevents MIME-type sniffing.
- `SECURE_BROWSER_XSS_FILTER = True`: Enables XSS protection in browsers.
- Nginx config reinforces headers and HSTS.

 Potential Improvements
- Add a Web Application Firewall (e.g., Cloudflare, AWS WAF).
- Enable `Referrer-Policy`, `Permissions-Policy`, and `Content-Security-Policy` headers.
- Integrate automated security testing (e.g., OWASP ZAP).
- Implement rate-limiting for authentication endpoints.

 Testing
- Verified HTTPS redirection.
- Verified headers using browser dev tools → "Security" tab.
- Used SSL Labs: https://www.ssllabs.com/ssltest/