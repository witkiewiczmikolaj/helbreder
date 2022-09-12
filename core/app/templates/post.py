from flask import request
from templates.modules_fcn import *
from templates.actions_fcn import *
from templates.targets_fcn import *

output = ["*module*", "*action*", "*target*"]

def action_target():
    global output
    
    for i in range (len(modules())):
        if request.form.get(f'{modules()[i].title()}') == f'{modules()[i].title()}':
            action = actions_buttonized(actions(modules()[i]))
            target = targets_buttonized(targets(modules()[i]))
            output[0] = request.form.get(f'{modules()[i].title()}')
            if len(output) >= 2:
                output[1] = "*action*"
                output[2] = "*target*"
        for j in range (len(actions(modules()[i]))):
            if request.form.get(f'{actions(modules()[i])[j].title()}') == f'{actions(modules()[i])[j].title()}':
                action = actions_buttonized(actions(modules()[i]))
                target = targets_buttonized(targets(modules()[i]))
                output[1] = request.form.get(f'{actions(modules()[i])[j].title()}')
        for j in range (len(targets(modules()[i]))):
            if request.form.get(f'{targets(modules()[i])[j].title()}') == f'{targets(modules()[i])[j].title()}':
                action = actions_buttonized(actions(modules()[i]))
                target = targets_buttonized(targets(modules()[i]))
                output[2] = request.form.get(f'{targets(modules()[i])[j].title()}')
    return action, target
