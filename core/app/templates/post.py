from flask import request
from templates.modules_fcn import *
from templates.actions_fcn import *
from templates.targets_fcn import *

def action_target():
    for i in range (len(modules())):
        if request.form.get(f'{modules()[i].title()}') == f'{modules()[i].title()}':
            action = actions_buttonized(actions(modules()[i]))
            target = targets_buttonized(targets(modules()[i]))
    return action, target
