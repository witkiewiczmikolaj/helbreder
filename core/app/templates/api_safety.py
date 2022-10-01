from templates.actions_fcn import *
from templates.log_collector import *
from flask import request

def new_request(data, module):
    data = request.get_json()
    save_api_request(request.authorization.username, module, data)
    return data

def validate_request(module, data):
    action_list = actions(module)

    if data["action"] in action_list:
        return True
    else:
        print('ILLEGAL/UNSUPPORTED OPERATION WAS REQUESTED!')
        return False