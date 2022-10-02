import os
from werkzeug.security import generate_password_hash, check_password_hash
from flask_httpauth import HTTPBasicAuth

user = os.environ.get('AUTH_USER')
password = os.environ.get('AUTH_PASSWORD')
users = {
    user: generate_password_hash(password),
}

auth = HTTPBasicAuth()

@auth.verify_password
def verify_password(username, password):
    if username in users:
        return check_password_hash(users.get(username), password)
    return False
