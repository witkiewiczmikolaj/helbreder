import yaml
from templates.list_modifications import *
from templates.modules_fcn import *

def targets(module):
    file = open("/helbreder/app/doc/possibilities.yml")
    data = yaml.safe_load(file)
    targets_list = list(data['modules'][module]['targets'])
    return targets_list

def targets_buttonized(targets_list):
    buttons = []
    for i in range (len(targets_list)):
        buttons.append('<label class="container">' + targets_list[i].title() + '<input class="target_butt" type="radio" ' + 'name="targets" value="' + targets_list[i].title() + '"><span class="checkmark"></span></label>')
    buttons = list_insert(buttons, '<br>') 
    buttons = ' '.join(buttons)    
    return buttons
