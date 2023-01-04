from audioop import add
from flask import request
from templates.modules_fcn import *
from templates.actions_fcn import *
from templates.targets_fcn import *
from templates.curl_to_code import *
from templates.user_pass import *
from templates.languages import *
from templates.action_target import *
from templates.sql import *

button_clicked = ["*module*", "*action*", "*target*", "*username*", "*password*", "*target_name*", "*user*", "*IP*", "*resource_type*"]

def collect_data():
    global button_clicked
        
    try:
        action, target, button_clicked, additional = action_target()
    except UnboundLocalError:
        pass
    
    if request.form.get("Submit") == "Submit":
        action, target, button_clicked, additional = user_pass()
        button_clicked[5] = request.form.get("Target_name")
        button_clicked[6] = request.form.get("User")
        button_clicked[7] = request.form.get("IP")
        button_clicked[8] = request.form.get("Resource_type")

    return action, target, additional, button_clicked