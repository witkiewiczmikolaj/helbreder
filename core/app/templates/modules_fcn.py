import yaml
from templates.list_modifications import *

def modules():
    file = open("/helbreder/app/doc/possibilities.yml")
    data = yaml.safe_load(file)
    modules = []
    modules_list = list(data['modules'].keys())
    for i in range (len(modules_list)):
        modules.append(list(data['modules'].keys())[i])  
    return modules

def allowed_actions(module):
    file = open("/helbreder/app/doc/possibilities.yml")
    data = yaml.safe_load(file)
    
    return data['modules'][module]['actions']

def modules_buttonized():
    buttons = []
    for i in range (len(modules())):
        buttons.append('<input class="module_butt" type="submit" ' + 'name="' + modules()[i].title() + '" value="' + modules()[i].title() + '">')
    buttons = list_insert(buttons, '<br>')
    buttons = ' '.join(buttons)    
    return buttons
