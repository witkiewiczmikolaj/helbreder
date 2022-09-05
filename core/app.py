import datetime
from flask import Flask,request,json, render_template
from basic_auth import *
from modules.kubernetes import *

helbreder = Flask(__name__)

@helbreder.route('/')
def static_main():
    img = "What bothers you?"
    return render_template("index.html", img = img)

@helbreder.route('/hi')
def object():
    resp = str(request.args.get('jsdata'))
    return render_template("object.html", resp = resp)

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

    func = str(action + '_' + t_kind)
    eval(func)(ns, t_name)

    return f"[{datetime.datetime.now()}] action: {func} on {t_kind}/{t_name}\n"

if __name__ == "__main__":
    helbreder.run(debug=True)

