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
