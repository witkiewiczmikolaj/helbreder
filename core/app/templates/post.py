from flask import request
from templates.modules_fcn import *
from templates.actions_fcn import *
from templates.targets_fcn import *

butt_clicked = ["*module*", "*action*", "*target*"]

def action_target():
    global butt_clicked
    
    for module in range (len(modules())):
        if request.form.get(f'{modules()[module].title()}') == f'{modules()[module].title()}':
            action = actions_buttonized(actions(modules()[module]))
            target = targets_buttonized(targets(modules()[module]))
            butt_clicked[0] = request.form.get(f'{modules()[module].title()}')
            if len(butt_clicked) >= 2:
                butt_clicked[1] = "*action*"
                butt_clicked[2] = "*target*"
        for act in range (len(actions(modules()[module]))):
            if request.form.get(f'{actions(modules()[module])[act].title()}') == f'{actions(modules()[module])[act].title()}':
                action = actions_buttonized(actions(modules()[module]))
                target = targets_buttonized(targets(modules()[module]))
                butt_clicked[1] = request.form.get(f'{actions(modules()[module])[act].title()}')
        for targ in range (len(targets(modules()[module]))):
            if request.form.get(f'{targets(modules()[module])[targ].title()}') == f'{targets(modules()[module])[targ].title()}':
                action = actions_buttonized(actions(modules()[module]))
                target = targets_buttonized(targets(modules()[module]))
                butt_clicked[2] = request.form.get(f'{targets(modules()[module])[targ].title()}')
    return action, target
