import yaml
from flask import request
from templates.curl_to_code import *
from templates.post import button_clicked

def lang_gen():
    global button_clicked
    file = open("D:/helbreder/core/app/doc/languages.yml")
    languages = yaml.safe_load(file)
    data = '{"namespace": "' + f'{button_clicked[0]}' + '", "action": "' + f'{button_clicked[1]}' + '", "target_name": "' + f'{button_clicked[2]}' + '", "target_kind": "target_kind"}'
    curl = "curl --request POST \ --url http://helbreder_url/api/endpoint \ --header 'Accept: application/json' \ --header 'Authorization: Basic " + f'{button_clicked[3]}' + f'{button_clicked[4]}' + "' \ --header 'Content-Type: application/json'\ --data '" + f'{data}' + "'"
    action = '<h3>Waiting for module</h3>'
    target = '<h3>Waiting for module</h3>'
    curl_code = "curl    --request POST \ \n\t--url http://helbreder_url/api/endpoint \ \n\t--header 'Accept: application/json' \ \n\t--header 'Authorization: Basic " + f'{button_clicked[3]}' + f'{button_clicked[4]}' + "' \ \n\t--header 'Content-Type: application/json'\ \n\t--data '" + f'{data}' + "'"
    for lang in languages:
        if request.form.get(lang) == lang:
            code = curl_to_code(curl, lang.lower())
        elif request.form.get("Shell") == "Shell":
            code = curl_code

    return action, target, code
