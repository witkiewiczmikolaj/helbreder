from flask import request
import base64

button_clicked = ["*module*", "*action*", "*target*", "*username*", "*password*", "*target_name*", "*user*", "*IP*", "*resource_type*"]

def encode(item):
    return base64.b64encode(request.form.get(item).encode("utf-8"))

def get_user_pass():
    #no encoding since it may be sant in plain text before the url
    # username = encode("Username")
    # password = encode("Password")
    return 'username', 'password'

def user_pass():
    global button_clicked
    action = '<h3>Waiting for module</h3>'
    target = '<h3>Waiting for module</h3>'
    additional = '<h3>Waiting for module</h3>'
    button_clicked[3], button_clicked[4] = request.form.get("Username"), request.form.get("Password")
    return action, target, button_clicked, additional