import datetime
from flask import Flask, request, json, render_template
from basic_auth import *
from modules.kubernetes import *
from templates.modules_fcn import *
from templates.post import *

helbreder = Flask(__name__)

@helbreder.route('/', methods=['GET', 'POST'])
def static_main():
    module = modules_buttonized()
    action = '<h3>Waiting for module</h3>'
    target = '<h3>Waiting for module</h3>'
    if request.method == 'POST':
        action, target = action_target()
    return render_template('index.html', module = module, action = action, target = target)

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

