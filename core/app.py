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

    func = str(action + '_' + t_kind)
    eval(func)(ns, t_name)

    return f"[{datetime.datetime.now()}] action: {func} on {t_kind}/{t_name}\n"

if __name__ == "__main__":
    helbreder.run(debug=True)