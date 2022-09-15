from flask import request
import base64
from templates.modules_fcn import *
from templates.actions_fcn import *
from templates.targets_fcn import *
from templates.curl_to_code import *

button_clicked = ["*module*", "*action*", "*target*", "*username*", "*password*"]

def collect_data():
    global button_clicked

    for module in range (len(modules())):
        
        if request.form.get(f'{modules()[module].title()}') == f'{modules()[module].title()}':
            action = actions_buttonized(actions(modules()[module]))
            target = targets_buttonized(targets(modules()[module]))
            button_clicked[0] = request.form.get(f'{modules()[module].title()}')
            username = 'username'
            password = 'password'
            code = 'Waiting for inputs'
        
        for act in range (len(actions(modules()[module]))):
            
            if request.form.get(f'{actions(modules()[module])[act].title()}') == f'{actions(modules()[module])[act].title()}':
                action = actions_buttonized(actions(modules()[module]))
                target = targets_buttonized(targets(modules()[module]))
                username = 'username'
                password = 'password'
                code = 'Waiting for inputs'
                button_clicked[1] = request.form.get(f'{actions(modules()[module])[act].title()}')
        
        for targ in range (len(targets(modules()[module]))):
            
            if request.form.get(f'{targets(modules()[module])[targ].title()}') == f'{targets(modules()[module])[targ].title()}':
                action = actions_buttonized(actions(modules()[module]))
                target = targets_buttonized(targets(modules()[module]))
                username = 'username'
                password = 'password'
                code = 'Waiting for inputs'
                button_clicked[2] = request.form.get(f'{targets(modules()[module])[targ].title()}')
    
    if request.form.get("Submit") == "Submit":
        username = request.form.get("Username")
        username = base64.b64encode(username.encode("utf-8"))
        password = request.form.get("Password")
        password = base64.b64encode(password.encode("utf-8"))
        button_clicked[3] = username
        button_clicked[4] = password
        module = modules_buttonized()
        action = '<h3>Waiting for module</h3>'
        target = '<h3>Waiting for module</h3>'
        data = '{"namespace": "' + f'{button_clicked[0]}' + '", "action": "' + f'{button_clicked[1]}' + '", "target_name": "' + f'{button_clicked[2]}' + '", "target_kind": "target_kind"}'
        curl_code = "curl    --request POST \ \n\t--url http://helbreder_url/api/endpoint \ \n\t--header 'Accept: application/json' \ \n\t--header 'Authorization: Basic " + f'{button_clicked[3]}' + f'{button_clicked[4]}' + "' \ \n\t--header 'Content-Type: application/json'\ \n\t--data '" + f'{data}' + "'"
        code = curl_code

    if request.form.get("Shell") == "Shell" or \
       request.form.get("Python") == "Python" or \
       request.form.get("Java") == "Java" or \
       request.form.get("Javascript") == "Javascript" or \
       request.form.get("Node-axios") == "Node-axios" or \
       request.form.get("Php") == "Php" or \
       request.form.get("Go") == "Go" or \
       request.form.get("R") == "R" or \
       request.form.get("Ruby") == "Ruby" or \
       request.form.get("Rust") == "Rust" or \
       request.form.get("Csharp") == "Csharp" or \
       request.form.get("Elixir") == "Elixir" or \
       request.form.get("Dart") == "Dart" or \
       request.form.get("Matlab") == "Matlab":
        module = modules_buttonized()
        action = '<h3>Waiting for module</h3>'
        target = '<h3>Waiting for module</h3>'
        username = 'username'
        password = 'password'
        data = '{"namespace": "' + f'{button_clicked[0]}' + '", "action": "' + f'{button_clicked[1]}' + '", "target_name": "' + f'{button_clicked[2]}' + '", "target_kind": "target_kind"}'
        curl = "curl --request POST \ --url http://helbreder_url/api/endpoint \ --header 'Accept: application/json' \ --header 'Authorization: Basic " + f'{button_clicked[3]}' + f'{button_clicked[4]}' + "' \ --header 'Content-Type: application/json'\ --data '" + f'{data}' + "'"
        curl_code = "curl    --request POST \ \n\t--url http://helbreder_url/api/endpoint \ \n\t--header 'Accept: application/json' \ \n\t--header 'Authorization: Basic " + f'{button_clicked[3]}' + f'{button_clicked[4]}' + "' \ \n\t--header 'Content-Type: application/json'\ \n\t--data '" + f'{data}' + "'"

    if request.form.get("Shell") == "Shell":
        code = curl_code

    if request.form.get("Python") == "Python":
        code = curl_to_code(curl, "python")

    if request.form.get("Java") == "Java":
        code = curl_to_code(curl, "java")

    if request.form.get("Javascript") == "Javascript":
        code = curl_to_code(curl, "javascript")

    if request.form.get("Node-axios") == "Node-axios":
        code = curl_to_code(curl, "node-axios")

    if request.form.get("Php") == "Php":
        code = curl_to_code(curl, "php")

    if request.form.get("Go") == "Go":
        code = curl_to_code(curl, "go")

    if request.form.get("R") == "R":
        code = curl_to_code(curl, "r")

    if request.form.get("Ruby") == "Ruby":
        code = curl_to_code(curl, "ruby")

    if request.form.get("Rust") == "Rust":
        code = curl_to_code(curl, "rust")

    if request.form.get("Csharp") == "Csharp":
        code = curl_to_code(curl, "csharp")

    if request.form.get("Elixir") == "Elixir":
        code = curl_to_code(curl, "elixir")

    if request.form.get("Dart") == "Dart":
        code = curl_to_code(curl, "dart")

    if request.form.get("Matlab") == "Matlab":
        code = curl_to_code(curl, "matlab")

    return action, target, code