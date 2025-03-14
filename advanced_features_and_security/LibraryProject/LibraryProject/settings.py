# settings.py

# Enforce HTTPS redirection
SECURE_SSL_REDIRECT = True  # Redirect all HTTP requests to HTTPS

# HTTP Strict Transport Security (HSTS)
SECURE_HSTS_SECONDS = 31536000  # 1 year
SECURE_HSTS_INCLUDE_SUBDOMAINS = True  # Apply HSTS to all subdomains
SECURE_HSTS_PRELOAD = True  # Allow your site to be included in browser preloading lists

# Ensure secure cookies
SESSION_COOKIE_SECURE = True  # Session cookies will only be sent over HTTPS
CSRF_COOKIE_SECURE = True  # CSRF cookies will only be sent over HTTPS
# settings.py

# Enforce secure cookies
SESSION_COOKIE_SECURE = True  # Ensure session cookies are transmitted securely
CSRF_COOKIE_SECURE = True  # Ensure CSRF cookies are transmitted securely
# settings.py

# Prevent your site from being framed (Clickjacking protection)
X_FRAME_OPTIONS = 'DENY'  # Block any framing of your site

# Secure content-type handling (MIME sniffing protection)
SECURE_CONTENT_TYPE_NOSNIFF = True  # Prevent browsers from interpreting files as different MIME types

# Enable browser XSS filter
SECURE_BROWSER_XSS_FILTER = True  # Protect against cross-site scripting attacks

