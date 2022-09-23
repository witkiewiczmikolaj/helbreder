import yaml
from templates.list_modifications import *
from templates.modules_fcn import *

def actions(module):    
    file = open("/helbreder/app/doc/possibilities.yml")
    data = yaml.safe_load(file)
    actions_list = list(data['modules'][module]['actions'])
    return actions_list

def actions_buttonized(action_list):
    buttons = []
    for i in range (len(action_list)):
        buttons.append('<label class="container">' + action_list[i].title() + '<input class="action_butt" type="radio" ' + 'name="actions" value="' + action_list[i].title() + '"><span class="checkmark"></span></label>')
    buttons = list_insert(buttons, '<br>') 
    buttons = ' '.join(buttons)    
    return buttons
