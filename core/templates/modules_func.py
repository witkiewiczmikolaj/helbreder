import yaml

def modules():
    file = open("./doc/possibilities.yml")
    data = yaml.safe_load(file)
    modules = []
    modules_list = list(data['modules'].keys())
    for i in range (len(modules_list)):
        modules.append(list(data['modules'].keys())[i].title()) 
    return modules