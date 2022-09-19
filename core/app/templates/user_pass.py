from flask import request
import base64

button_clicked = ["*module*", "*action*", "*target*", "*username*", "*password*"]

def encode():
    rq = request.form.get
    username = base64.b64encode(rq("Username").encode("utf-8"))
    password = base64.b64encode(rq("Password").encode("utf-8"))
    return username, password

def user_pass():
    global button_clicked
    action = '<h3>Waiting for module</h3>'
    target = '<h3>Waiting for module</h3>'
    code = 'Waiting for inputs'
    button_clicked[3], button_clicked[4] = encode()
    return action, target, code, button_clicked