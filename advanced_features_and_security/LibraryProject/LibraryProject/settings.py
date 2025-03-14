
DEBUG = False

# Secure your application by setting these values
SECURE_BROWSER_XSS_FILTER = True  # Prevents some cross-site scripting (XSS) attacks
X_FRAME_OPTIONS = 'DENY'  # Prevent embedding of your site in a frame (Clickjacking protection)
SECURE_CONTENT_TYPE_NOSNIFF = True  # Prevent browsers from interpreting files as something else

# Ensure cookies are sent over HTTPS only
CSRF_COOKIE_SECURE = True  # CSRF cookie is only sent over HTTPS
SESSION_COOKIE_SECURE = True  # Session cookie is only sent over HTTPS

# Set a secure cookie for CSRF and session cookies
CSRF_COOKIE_HTTPONLY = True  # Prevent JavaScript from accessing the CSRF cookie
SESSION_COOKIE_HTTPONLY = True  # Prevent JavaScript from accessing session cookies

# HSTS (HTTP Strict Transport Security) to force HTTPS connections
SECURE_HSTS_SECONDS = 31536000  # 1 year
SECURE_HSTS_INCLUDE_SUBDOMAINS = True  # Include all subdomains in HSTS
SECURE_HSTS_PRELOAD = True  # Preload HSTS for browser support
