from flask import request
import json
from templates.curl_to_code import *
from templates.sql import *
from templates.post import button_clicked

def lang_gen():
    global button_clicked
    languages = get_lang_sql()
    action = '<h3>Waiting for module</h3>'
    target = '<h3>Waiting for module</h3>'
    data = {}

    if button_clicked[0] == "Kubernetes":
        data['namespace'] = button_clicked[0]
        data['action'] = button_clicked[1]
        data['target_name'] = button_clicked[5]
        data['target_kind'] = button_clicked[2]
        data_json = json.dumps(data)
    else:
        data['action'] = button_clicked[1]
        data['target_name'] = button_clicked[5]
        data['target_kind'] = button_clicked[2]
        data_json = json.dumps(data)
        
    curl = "curl --request POST \ --url http://helbreder_url/api/endpoint \ --header 'Accept: application/json' \ --header 'Authorization: Basic " + f'{button_clicked[3]}' + f'{button_clicked[4]}' + "' \ --header 'Content-Type: application/json'\ --data '" + f'{data_json}' + "'"
    curl_code = "curl    --request POST \ \n\t--url http://helbreder_url/api/endpoint \ \n\t--header 'Accept: application/json' \ \n\t--header 'Authorization: Basic " + f'{button_clicked[3]}' + f'{button_clicked[4]}' + "' \ \n\t--header 'Content-Type: application/json'\ \n\t--data '" + f'{data_json}' + "'"
    
    for lang in languages:
        if request.form.get(lang) == lang:
            code = curl_to_code(curl, lang.lower())
        elif request.form.get("Shell") == "Shell":
            code = curl_code

    return action, target, code

def lang_buttonized():
    languages = get_lang_sql()
    langs = []
    for lang in languages:
        langs.append('<button id="' + lang.lower() + '_butt" type="submit" name="' + lang + '" value="' + lang + '"><img src="../static/images/' + lang.lower() + '.png"/></button>')
    langs = ' '.join(langs)    
    return langs
