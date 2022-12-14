import flask_login
import jwt
from datetime import datetime, timezone
from redmail import gmail
from flask import request, flash, redirect, url_for, render_template
from templates.psql import *
from hashlib import sha256
from templates.modules_fcn import *

gmail.user_name = os.environ.get('EMAIL')
gmail.password = os.environ.get('EMAIL_PASSWORD')

class User(flask_login.UserMixin):
    def __init__(self, name):
        self.name = name

def get_name(email):
    cur.execute(f"SELECT username FROM ACCOUNTS WHERE email = '{email}'")
    name = cur.fetchone()
    return name[0]

def email_check(email):
    try:
        cur.execute(f"SELECT email FROM ACCOUNTS WHERE email = '{email}'")
        emails_sql = cur.fetchone()
        if not emails_sql:
            return False
        return True
    except:
        return False
   
def username_check(username):
    cur.execute(f"SELECT username FROM ACCOUNTS WHERE username = '{username}'")
    username_sql = cur.fetchone()
    if not username_sql:
        return False
    return True

def hash_password(password):
    h = sha256()
    h.update(password.encode())
    return h.hexdigest()

def add_account(email, username, password):
    password_hash = hash_password(password)
    dt = datetime.now(timezone.utc)
    modules_list = modules()
    modules_list = ', '.join(modules_list)  
    cur.execute(f"INSERT INTO ACCOUNTS (username, password, email, verified, {modules_list}, created_on) VALUES ('{username}', '{password_hash}', '{email}', FALSE, 0, 0, 0,'{dt}');")
    c.commit()

def decode_email(token):
    data = jwt.decode(token, os.environ.get('SECRET_KEY'), algorithms=['HS256'])
    return data["email_address"]

def verify(email):
    try:
        cur.execute(f"UPDATE ACCOUNTS SET verified = TRUE WHERE email = '{email}';")
        c.commit()
        flash('Thank you! Now you can log in.')
    except:
        flash('Something went wrong!')

def delete_email(email):
    try:
        cur.execute(f"DELETE FROM ACCOUNTS WHERE email = '{email}';")
        c.commit()
        flash('Thank you! Your account has been deleted.')
    except:
        flash('Something went wrong!')

def verified(email):
    cur.execute(f"SELECT verified FROM ACCOUNTS WHERE email = '{email}'")
    is_verified = cur.fetchone()
    return is_verified[0]

def check_pass(email, password_hash):
    cur.execute(f"SELECT password FROM ACCOUNTS WHERE email = '{email}'")
    password = cur.fetchall()
    if password[0][0] == password_hash:
        return True
    return False

def send_email(email):
    token = jwt.encode(
        {
            "email_address": email,
        }, os.environ.get('SECRET_KEY')
    )
    gmail.send(
        subject = "Verify email",
        receivers = email,
        html = """<h1>Hi,</h1>
                <p>in order to use our services, please click the link below:
                <br>
                <a href="https://helbreder.online/verify-email/{{token}}">Verify email</a>
                </p>
                <p>If you did not create an account, you may delete your account by clicking in the link below:
                <br>
                <a href="https://helbreder.online/delete-account/{{token}}">Delete account</a>
                </p>
                """,
        body_params = {
            "token": token
        }
    )

def sign_up():
    email = request.form.get('email')
    username = request.form.get('username')
    password = request.form.get('password')
    if email_check(email):
        flash('You already have an account!')
    elif username_check(username):
        flash('Username already exists!')
    elif len(password) < 8:
        flash('Password needs to be at least 8 characters long!')
    else:
        try:
            add_account(email, username, password)
            send_email(email)
            flash('Please check your email and click the link to verify!')
        except:
            flash('Something went wrong!')

def log_in():
    email = request.form.get('email')
    password = request.form.get('password')
    remember = True if request.form.get('remember') else False
    if not email_check(email):
        flash('Please sign up first!')
        return render_template('html/login.html')
    elif not verified(email):
        flash('Please verify your email first!')
        return render_template('html/login.html')
    else:
        password_hash = hash_password(password)
        if check_pass(email, password_hash):
            user = User(get_name(email))
            user.id = email
            flask_login.login_user(user, remember=remember)
            return redirect(url_for('static_main'))
        else:
            flash('Wrong password!')
            return render_template('html/login.html')