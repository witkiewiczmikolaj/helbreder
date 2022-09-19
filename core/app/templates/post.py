from flask import request
from templates.modules_fcn import *
from templates.actions_fcn import *
from templates.targets_fcn import *
from templates.curl_to_code import *
from templates.user_pass import *
from templates.languages import *
from templates.action_target import *
from templates.sql import *

button_clicked = ["*module*", "*action*", "*target*", "*username*", "*password*"]

def collect_data():
    global button_clicked
    languages = get_lang_sql()
    rq = request.form.get
    
    try:
        action, target, code, button_clicked = action_target()
    except UnboundLocalError:
        pass
    
    if rq("Submit") == "Submit":
        action, target, code, button_clicked = user_pass()

    for lang in languages:
        if rq(lang) == lang:
            action, target, code = lang_gen()

    return action, target, code