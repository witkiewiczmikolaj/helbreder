from flask import request
from templates.modules_fcn import *
from templates.actions_fcn import *
from templates.targets_fcn import *
from templates.curl_to_code import *
from templates.user_pass import *
from templates.languages import *
from templates.action_target import *

button_clicked = ["*module*", "*action*", "*target*", "*username*", "*password*"]

def collect_data():
    global button_clicked
    languages = open_lang()
    rq = request.form.get

    for module in range (len(modules())):
        if rq(f'{modules()[module].title()}') == f'{modules()[module].title()}':
            action, target, code, button_clicked = action_target()

        for act in range (len(actions(modules()[module]))):
            if rq(f'{actions(modules()[module])[act].title()}') == f'{actions(modules()[module])[act].title()}':
                action, target, code, button_clicked = action_target()
        
        for targ in range (len(targets(modules()[module]))):
            if rq(f'{targets(modules()[module])[targ].title()}') == f'{targets(modules()[module])[targ].title()}':
                action, target, code, button_clicked = action_target()
    
    if rq("Submit") == "Submit":
        action, target, code, button_clicked = user_pass()

    for lang in languages:
        if rq(lang) == lang:
            action, target, code = lang_gen()

    return action, target, code