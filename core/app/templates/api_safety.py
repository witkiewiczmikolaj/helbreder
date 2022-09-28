from templates.actions_fcn import *

def validate_request(module, data):
    action_list = actions(module)

    if data["action"] in action_list:
        return True
    else:
        print('ILLEGAL/UNSUPPORTED OPERATION WAS REQUESTED!')
        return False