import yaml
from flask import request
from templates.curl_to_code import *
from templates.post import button_clicked

def open_lang():
    file = open("/helbreder/app/doc/languages.yml")
    languages = yaml.safe_load(file)
    return languages

def lang_gen():
    global button_clicked
    rq = request.form.get
    languages = open_lang()
    action = '<h3>Waiting for module</h3>'
    target = '<h3>Waiting for module</h3>'

    data = '{"namespace": "' + f'{button_clicked[0]}' + '", "action": "' + f'{button_clicked[1]}' + '", "target_name": "' + f'{button_clicked[2]}' + '", "target_kind": "target_kind"}'
    curl = "curl --request POST \ --url http://helbreder_url/api/endpoint \ --header 'Accept: application/json' \ --header 'Authorization: Basic " + f'{button_clicked[3]}' + f'{button_clicked[4]}' + "' \ --header 'Content-Type: application/json'\ --data '" + f'{data}' + "'"
    curl_code = "curl    --request POST \ \n\t--url http://helbreder_url/api/endpoint \ \n\t--header 'Accept: application/json' \ \n\t--header 'Authorization: Basic " + f'{button_clicked[3]}' + f'{button_clicked[4]}' + "' \ \n\t--header 'Content-Type: application/json'\ \n\t--data '" + f'{data}' + "'"
    
    for lang in languages:
        if rq(lang) == lang:
            code = curl_to_code(curl, lang.lower())
        elif rq("Shell") == "Shell":
            code = curl_code

    return action, target, code

def lang_buttonized():
    languages = open_lang()
    langs = []
    for lang in languages:
        langs.append('<button id="' + lang.lower() + '_butt" type="submit" name="' + lang + '" value="' + lang + '"><img src="../static/images/' + lang.lower() + '.png"/></button>')
    langs = ' '.join(langs)    
    return langs
