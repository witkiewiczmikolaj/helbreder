import yaml
from templates.list_modifications import *

def modules():
    file = open("/helbreder/app/doc/possibilities.yml")
    data = yaml.safe_load(file)
    modules_list = list(data['modules'].keys())
    return modules_list

def modules_buttonized():
    buttons = []
    for i in range (len(modules())):
        buttons.append('<input class="module_butt" type="submit" ' + 'name="' + modules()[i].title() + '" value="' + modules()[i].title() + '">')
    buttons = list_insert(buttons, '<br>')
    buttons = ' '.join(buttons)    
    return buttons
