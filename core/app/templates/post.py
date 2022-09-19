from flask import request
from templates.modules_fcn import *
from templates.actions_fcn import *
from templates.targets_fcn import *
from templates.curl_to_code import *
from templates.user_pass import *
from templates.languages import *

button_clicked = ["*module*", "*action*", "*target*", "*username*", "*password*"]

def collect_data():
    global button_clicked
    file = open("D:/helbreder/core/app/doc/languages.yml")
    languages = yaml.safe_load(file)
    
    for module in range (len(modules())):
        
        if request.form.get(f'{modules()[module].title()}') == f'{modules()[module].title()}':
            action = actions_buttonized(actions(modules()[module]))
            target = targets_buttonized(targets(modules()[module]))
            button_clicked[0] = request.form.get(f'{modules()[module].title()}')
            code = 'Waiting for inputs'
            
        for act in range (len(actions(modules()[module]))):
            
            if request.form.get(f'{actions(modules()[module])[act].title()}') == f'{actions(modules()[module])[act].title()}':
                action = actions_buttonized(actions(modules()[module]))
                target = targets_buttonized(targets(modules()[module]))
                button_clicked[1] = request.form.get(f'{actions(modules()[module])[act].title()}')
                code = 'Waiting for inputs'
        
        for targ in range (len(targets(modules()[module]))):
            
            if request.form.get(f'{targets(modules()[module])[targ].title()}') == f'{targets(modules()[module])[targ].title()}':
                action = actions_buttonized(actions(modules()[module]))
                target = targets_buttonized(targets(modules()[module]))
                button_clicked[2] = request.form.get(f'{targets(modules()[module])[targ].title()}')
                code = 'Waiting for inputs'
    
    if request.form.get("Submit") == "Submit":
        action, target, code, button_clicked = user_pass()

    for lang in languages:
        if request.form.get(lang) == lang:
            action, target, code = lang_gen()

    return action, target, code