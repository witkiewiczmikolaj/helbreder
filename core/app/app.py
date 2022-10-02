import datetime
from flask import Flask,request,json,render_template,abort
from basic_auth import *
import sys

from modules.kubernetes import *
from modules.postgresql import *

from templates.modules_fcn import *
from templates.api_safety import *
from templates.post import *

helbreder = Flask(__name__)

@helbreder.route('/', methods=['GET', 'POST'])
def static_main():
    global button_clicked
    module = modules_buttonized()
    action = '<h3>Waiting for module</h3>'
    target = '<h3>Waiting for module</h3>'
    languages = lang_buttonized()
    if request.method == 'POST':
        try:
            action, target = collect_data()
        except KeyError:
            print('Choose action and target_kind first!')
    return render_template('index.html', module = module, action = action, target = target, button_clicked = button_clicked, languages = languages)

@helbreder.route('/code', methods=['GET'])
@auth.login_required
def code_outcome():
    try:
        code = lang_gen(request.args.get('code'))
        return render_template('code.html', code = code)
    except AttributeError:
        abort(500)

@helbreder.route('/api',methods=['POST'])
@auth.login_required
def api_base():
    data = new_request(request.get_json(), 'api')
    return "Hi!"

@helbreder.route('/api/k8s',methods=['POST'])
@auth.login_required
def k8s():
    data = new_request(request.get_json(), 'k8s')

    if validate_request('kubernetes', data):
        ns = data["namespace"]
        action = data["action"]
        t_name = data["target_name"]
        t_kind = data["target_kind"]

        if t_name.endswith('*'):
            t_name = t_name.replace('*', '')
            names = find_(ns, t_name, t_kind)
        else:
            names = [t_name]

        func = str(action + '_')

        for t_name in names:
            eval(func)(ns, t_name, t_kind)

        return f"[{datetime.datetime.now()}] action: {func.replace('_','')} on {t_kind}/{t_name}\n"
    else:
        abort(501)

@helbreder.route('/api/psql',methods=['POST'])
@auth.login_required
def psql():
    data = new_request(request.get_json(), 'psql')

    if validate_request('postgresql', data):
        action = data["action"]
        t_name = data["target_name"]
        t_kind = data["target_kind"]

        func = str(action + '_')
        eval(func)(t_name, t_kind)

        return f"[{datetime.datetime.now()}] action: {func.replace('_','')} on {t_kind} {t_name}\n"
    else:
        abort(501)

if __name__ == "__main__":
    helbreder.run(debug=True)
