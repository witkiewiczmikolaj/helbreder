import datetime
from flask import Flask,request,json
from basic_auth import *
from modules.kubernetes import *

helbreder = Flask(__name__)

@helbreder.route('/')
def static_main():
    return '<h1>&#128137;</h1>'

@helbreder.route('/api',methods=['POST'])
@auth.login_required
def api_base():
    data = request.json
    print(data)
    return "Hi!"

@helbreder.route('/api/k8s',methods=['POST'])
@auth.login_required
def k8s():
    data = request.get_json()

    ns = data["namespace"]
    action = data["action"]
    t_name = data["target_name"]
    t_kind = data["target_kind"]

    if t_name.endswith('*'):
        func = str(t_kind + '_find')
        t_name = t_name.replace('*', '')
        t_name = eval(func)(ns, t_name)

    func = str(action + '_')
    eval(func)(ns, t_name, t_kind)

    return f"[{datetime.datetime.now()}] action: {func.replace('_','')} on {t_kind}/{t_name}\n"

if __name__ == "__main__":
    helbreder.run(debug=True)
