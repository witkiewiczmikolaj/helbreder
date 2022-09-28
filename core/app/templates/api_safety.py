from templates.modules_fcn import *

def validate_request(module, data):
    actions = allowed_actions(module)

    if data["action"] in actions:
        return True
    else:
        print('ILLEGAL/UNSUPPORTED OPERATION WAS REQUESTED!')
        return False