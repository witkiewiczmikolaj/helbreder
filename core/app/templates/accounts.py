import flask_login
from flask import request, flash, redirect, url_for, render_template
from templates.psql import *
from hashlib import sha256

class User(flask_login.UserMixin):
    def __init__(self, name):
        self.name = name

def get_name(email):
    cur.execute(f"SELECT username FROM ACCOUNTS_ONLINE WHERE email = '{email}'")
    name = cur.fetchone()
    return name[0]

def email_check(email):
    try:
        cur.execute(f"SELECT email FROM ACCOUNTS_ONLINE WHERE email = '{email}'")
        emails_sql = cur.fetchone()
        if not emails_sql:
            return False
        return True
    except:
        return False
   
def username_check(username):
    cur.execute(f"SELECT username FROM ACCOUNTS_ONLINE WHERE username = '{username}'")
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
    cur.execute(f"INSERT INTO ACCOUNTS_ONLINE (username, password, email, verified) VALUES ('{username}', '{password_hash}', '{email}', FALSE);")
    c.commit()

def verified():
    email = request.form.get('email')
    cur.execute(f"UPDATE ACCOUNTS_ONLINE SET verified = TRUE WHERE email = '{email}';")
    c.commit()
    flash('Thank you! Now you can log in.')
    return render_template('html/login.html')

def check_pass(email, password_hash):
    cur.execute(f"SELECT password FROM ACCOUNTS_ONLINE WHERE email = '{email}'")
    password = cur.fetchall()
    if password[0][0] == password_hash:
        return True
    return False

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