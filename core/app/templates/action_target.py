from flask import request
from templates.modules_fcn import *
from templates.actions_fcn import *
from templates.targets_fcn import *
from templates.post import button_clicked

def action_target():
    global button_clicked

    for module in range (len(modules())):
            if request.form.get(f'{modules()[module].title()}') == f'{modules()[module].title()}':
                action = actions_buttonized(actions(modules()[module]))
                target = targets_buttonized(targets(modules()[module]))
                button_clicked[0] = request.form.get(f'{modules()[module].title()}')
                return action, target, button_clicked

    button_clicked[1] = request.form['actions']
    button_clicked[2] = request.form['targets']
                    
    return action, target, button_clicked

    