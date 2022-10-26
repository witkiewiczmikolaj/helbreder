import re
from datetime import datetime
import random
from flask import request, flash
from templates.psql import *

def get_lang_sql():
    cur.execute('''SELECT name FROM LANGUAGES''')
    lang = cur.fetchall()
    languages = []
    for i in range (len(lang)):
        languages.append(''.join(lang[i]))
    return languages

def create_table(table_name, columns):
    columns = re.sub(r"'|:|{|}", "", str(columns))
    cur.execute(f"CREATE TABLE IF NOT EXISTS {table_name}({columns})")
    c.commit()

def email_check(email):
    cur.execute('''SELECT email FROM ACCOUNTS''')
    emails_sql = cur.fetchall()
    emails = []
    for i in range (len(emails_sql)):
        emails.append(''.join(emails_sql[i]))
    if email in emails:
        return True
    return False

def add_account(email, name, password):
    user_id = random.randint(0,1000000)
    time = datetime.now()
    cur.execute(f"INSERT INTO ACCOUNTS (user_id, username, password, email, created_on, last_login) VALUES ({user_id}, '{name}', '{password}', '{email}', '{time.isoformat()}', '{time.isoformat()}');")
    c.commit()

def sign_up():
    email = request.form.get('email')
    name = request.form.get('name')
    password = request.form.get('password')
    if email_check(email):
        flash('You already have an account!')
    else:
        add_account(email, name, password)
        flash('Succesfully created an account!')
    