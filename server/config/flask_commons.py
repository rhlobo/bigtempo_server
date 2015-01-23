import os
import random
import string


def _random_string(length):
    chars = string.ascii_lowercase + string.digits
    return ''.join(random.choice(chars) for _ in range(length))


# FLASK
SECRET_KEY = _random_string(18)

# FLASK-SESSION
PERMANENT_SESSION_LIFETIME = 600
SESSION_TYPE = 'filesystem'

# FLASK-BASICAUTH
BASIC_AUTH_USERNAME = os.getenv('BASIC_AUTH_USERNAME', None)
BASIC_AUTH_PASSWORD = os.getenv('BASIC_AUTH_PASSWORD', None)
