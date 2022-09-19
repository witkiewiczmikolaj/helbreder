from flask import request
import base64

button_clicked = ["*module*", "*action*", "*target*", "*username*", "*password*"]

def encode(item):
    return base64.b64encode(request.form.get(item).encode("utf-8"))

def get_user_pass():
    username = encode("Username")
    password = encode("Password")
    return username, password

def user_pass():
    global button_clicked
    action = '<h3>Waiting for module</h3>'
    target = '<h3>Waiting for module</h3>'
    code = 'Waiting for inputs'
    button_clicked[3], button_clicked[4] = get_user_pass()
    return action, target, code, button_clicked