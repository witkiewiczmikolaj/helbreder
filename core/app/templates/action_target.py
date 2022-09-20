from flask import request
from templates.modules_fcn import *
from templates.actions_fcn import *
from templates.targets_fcn import *
from templates.post import button_clicked

def action_target():
    global button_clicked
    rq = request.form.get

    for module in range (len(modules())):
            if rq(f'{modules()[module].title()}') == f'{modules()[module].title()}':
                action = actions_buttonized(actions(modules()[module]))
                target = targets_buttonized(targets(modules()[module]))
                button_clicked[0] = rq(f'{modules()[module].title()}')
                return action, target, button_clicked
                
            for act in range (len(actions(modules()[module]))):
                if rq(f'{actions(modules()[module])[act].title()}') == f'{actions(modules()[module])[act].title()}':
                    action = actions_buttonized(actions(modules()[module]))
                    target = targets_buttonized(targets(modules()[module]))
                    button_clicked[1] = rq(f'{actions(modules()[module])[act].title()}')
                    return action, target, button_clicked
            
            for targ in range (len(targets(modules()[module]))):
                if rq(f'{targets(modules()[module])[targ].title()}') == f'{targets(modules()[module])[targ].title()}':
                    action = actions_buttonized(actions(modules()[module]))
                    target = targets_buttonized(targets(modules()[module]))
                    button_clicked[2] = rq(f'{targets(modules()[module])[targ].title()}')
                    return action, target, button_clicked
                    
    return action, target, button_clicked

    