from flask import request
import base64
from templates.modules_fcn import *
from templates.actions_fcn import *
from templates.targets_fcn import *

button_clicked = ["*module*", "*action*", "*target*"]

def collect_data():
    global button_clicked
    
    for module in range (len(modules())):
        if request.form.get(f'{modules()[module].title()}') == f'{modules()[module].title()}':
            action = actions_buttonized(actions(modules()[module]))
            target = targets_buttonized(targets(modules()[module]))
            button_clicked[0] = request.form.get(f'{modules()[module].title()}')
            username = 'username'
            password = 'password'
            if len(button_clicked) >= 2:
                button_clicked[1] = "*action*"
                button_clicked[2] = "*target*"
        for act in range (len(actions(modules()[module]))):
            if request.form.get(f'{actions(modules()[module])[act].title()}') == f'{actions(modules()[module])[act].title()}':
                action = actions_buttonized(actions(modules()[module]))
                target = targets_buttonized(targets(modules()[module]))
                username = 'username'
                password = 'password'
                button_clicked[1] = request.form.get(f'{actions(modules()[module])[act].title()}')
        for targ in range (len(targets(modules()[module]))):
            if request.form.get(f'{targets(modules()[module])[targ].title()}') == f'{targets(modules()[module])[targ].title()}':
                action = actions_buttonized(actions(modules()[module]))
                target = targets_buttonized(targets(modules()[module]))
                username = 'username'
                password = 'password'
                button_clicked[2] = request.form.get(f'{targets(modules()[module])[targ].title()}')
    if request.form.get("Submit") == "Submit":
        username = request.form.get("Username")
        username = base64.b64encode(username.encode("utf-8"))
        password = request.form.get("Password")
        password = base64.b64encode(password.encode("utf-8"))
        module = modules_buttonized()
        action = '<h3>Waiting for module</h3>'
        target = '<h3>Waiting for module</h3>'

    return action, target, username, password
