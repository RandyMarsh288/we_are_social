from base import *

DEBUG = True

INSTALLED_APPS.append('debug_toolbar')

MIDDLEWARE_CLASSES.append('debug_toolbar.middleware.DebugToolbarMiddleware')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# CI data commented out. This was in the github version but not in the lesson
# I had a disqus_website_shortname in blog_app but not an api_key - maybe that was why disqus didn't work?
# DISQUS_API_KEY = 'ZruTajAt8E3Ao1F2fzL2Dx9VUra9u0XABGKdSLXtAIHN3gL0qoUwJYywaqMEKkB8'
# DISQUS_WEBSITE_SHORTNAME = 'codeinstitutesocialstaging'

# Stripe environment variables
STRIPE_PUBLISHABLE = os.getenv('STRIPE_PUBLISHABLE', 'pk_test_kLdDMq39gQJuwVRHNbtROldY')
STRIPE_SECRET = os.getenv('STRIPE_SECRET', 'sk_test_sNgcHOXBxiaZuVTDDAnX2AIQ')

# Paypal environment variables
SITE_URL = 'http://127.0.0.1:8000'
PAYPAL_NOTIFY_URL = 'http://127.0.0.1/a-very-hard-to-guess-url/'
PAYPAL_RECEIVER_EMAIL = 'business03@gmail.com'
