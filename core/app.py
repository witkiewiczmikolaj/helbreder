import datetime
from flask import Flask,request,json, render_template
from basic_auth import *
from modules.kubernetes import *
import yaml
import os

helbreder = Flask(__name__)

@helbreder.route('/')
def static_main():
    with open(os.path.abspath("D:/helbreder/doc/possibilities.yml"), 'r') as stream:
        data = yaml.safe_load(stream)
    
    kubernetes = list(data['modules'].keys())[0].title()
    server = list(data['modules'].keys())[1].title()
    welc = "Choose a module:"
    return render_template("index.html", welc = welc, kubernetes = kubernetes, server = server)

@helbreder.route('/actions')
def object():
    with open(os.path.abspath("D:/helbreder/doc/possibilities.yml"), 'r') as stream:
        data = yaml.safe_load(stream)

    action = str(request.args.get('jsdata'))
    action1 = data['modules'][f'{action}']['actions'][0].title()
    action2 = data['modules'][f'{action}']['actions'][1].title()
    action3 = data['modules'][f'{action}']['actions'][2].title()
    return render_template("actions.html", action1 = action1, action2 = action2, action3 = action3)

@helbreder.route('/targets')
def action():
    with open(os.path.abspath("D:/helbreder/doc/possibilities.yml"), 'r') as stream:
        data = yaml.safe_load(stream)

    target = str(request.args.get('jsdata'))
    target1 = data['modules'][f'{target}']['targets'][0].title()
    target2 = data['modules'][f'{target}']['targets'][1].title()
    target3 = data['modules'][f'{target}']['targets'][2].title()
    return render_template("targets.html", target1 = target1, target2 = target2, target3 = target3)

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

