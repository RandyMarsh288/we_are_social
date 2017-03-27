from base import *
# import dj_database_url
# import settings

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# DATABASES['default'] = dj_database_url.parse("mysql://b0a9eb36128587:6e79e9a2@eu-cdbr-west-01.cleardb.com/heroku_068d026402bf6b2?reconnect=true")

# Stripe environment variables
STRIPE_PUBLISHABLE = os.getenv('STRIPE_PUBLISHABLE', 'pk_test_kLdDMq39gQJuwVRHNbtROldY')
STRIPE_SECRET = os.getenv('STRIPE_SECRET', 'sk_test_sNgcHOXBxiaZuVTDDAnX2AIQ')

# Paypal environment variables
SITE_URL = 'code-institute-was-staging.herokuapp.com'
PAYPAL_NOTIFY_URL = 'code-institute-was-staging.herokuapp.com'
PAYPAL_RECEIVER_EMAIL = 'business03@gmail.com'
