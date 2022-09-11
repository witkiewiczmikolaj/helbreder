import yaml
from templates.list_modifications import *
from templates.modules_fcn import *

def targets(module):
    file = open("./doc/possibilities.yml")
    data = yaml.safe_load(file)
    targets = []
    targets_list = list(data['modules'][module]['targets'])
    for i in range (len(targets_list)):
        targets.append(list(data['modules'][module]['targets'][i]))
    return targets_list

def targets_buttonized(targets_list):
    buttons = []
    for i in range (len(targets_list)):
        buttons.append('<input class="target_butt" type="submit" ' + 'name="' + targets_list[i].title() + '" value="' + targets_list[i].title() + '">')
    buttons = list_insert(buttons, '<br>') 
    buttons = ' '.join(buttons)    
    return buttons
