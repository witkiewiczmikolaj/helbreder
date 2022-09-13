from flask import request
import base64
from templates.modules_fcn import *
from templates.actions_fcn import *
from templates.targets_fcn import *

butt_clicked = ["*module*", "*action*", "*target*"]

def collect_data():
    global butt_clicked
    
    for module in range (len(modules())):
        if request.form.get(f'{modules()[module].title()}') == f'{modules()[module].title()}':
            action = actions_buttonized(actions(modules()[module]))
            target = targets_buttonized(targets(modules()[module]))
            butt_clicked[0] = request.form.get(f'{modules()[module].title()}')
            user_pass = 'user:pass'
            if len(butt_clicked) >= 2:
                butt_clicked[1] = "*action*"
                butt_clicked[2] = "*target*"
        for act in range (len(actions(modules()[module]))):
            if request.form.get(f'{actions(modules()[module])[act].title()}') == f'{actions(modules()[module])[act].title()}':
                action = actions_buttonized(actions(modules()[module]))
                target = targets_buttonized(targets(modules()[module]))
                user_pass = 'user:pass'
                butt_clicked[1] = request.form.get(f'{actions(modules()[module])[act].title()}')
        for targ in range (len(targets(modules()[module]))):
            if request.form.get(f'{targets(modules()[module])[targ].title()}') == f'{targets(modules()[module])[targ].title()}':
                action = actions_buttonized(actions(modules()[module]))
                target = targets_buttonized(targets(modules()[module]))
                user_pass = 'user:pass'
                butt_clicked[2] = request.form.get(f'{targets(modules()[module])[targ].title()}')
    if request.form.get("Submit") == "Submit":
        username = request.form.get("Username")
        password = request.form.get("Password")
        user_pass = f'{username}' + ':' + f'{password}'
        user_pass = str(base64.b64encode(user_pass.encode("utf-8")))[2:-1]
        module = modules_buttonized()
        action = '<h3>Waiting for module</h3>'
        target = '<h3>Waiting for module</h3>'

    return action, target, user_pass
