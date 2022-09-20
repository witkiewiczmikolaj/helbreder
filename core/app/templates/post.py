from flask import request
from templates.modules_fcn import *
from templates.actions_fcn import *
from templates.targets_fcn import *
from templates.curl_to_code import *
from templates.user_pass import *
from templates.languages import *
from templates.action_target import *
from templates.sql import *

button_clicked = ["*module*", "*action*", "*target*", "*username*", "*password*", "*target_name*"]

def collect_data():
    global button_clicked
        
    try:
        action, target, button_clicked = action_target()
    except UnboundLocalError:
        pass
    
    if request.form.get("Submit") == "Submit":
        action, target, button_clicked = user_pass()
        button_clicked[5] = request.form.get("Target_name")

    return action, target