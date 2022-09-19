import yaml
from templates.list_modifications import *
from templates.modules_fcn import *

def targets(module):
    file = open("D:/helbreder/core/app/doc/possibilities.yml")
    data = yaml.safe_load(file)
    targets_list = list(data['modules'][module]['targets'])
    return targets_list

def targets_buttonized(targets_list):
    buttons = []
    for i in range (len(targets_list)):
        buttons.append('<input class="target_butt" type="submit" ' + 'name="' + targets_list[i].title() + '" value="' + targets_list[i].title() + '">')
    buttons = list_insert(buttons, '<br>') 
    buttons = ' '.join(buttons)    
    return buttons
