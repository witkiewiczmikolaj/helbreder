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
        languages = get_lang_sql()
    except psycopg2.errors.UndefinedTable:
        cur.execute("ROLLBACK")
        create_table()
        languages = get_lang_sql()
        print('Helbreder started with an empty languages table, please fill it in.')
    
    try:
        action, target, code, button_clicked = action_target()
    except UnboundLocalError:
        pass
    
    if request.form.get("Submit") == "Submit":
        action, target, code, button_clicked = user_pass()
        button_clicked[5] = request.form.get("Target_name")

    for lang in languages:
        if request.form.get(lang) == lang:
            action, target, code = lang_gen()

    return action, target, code