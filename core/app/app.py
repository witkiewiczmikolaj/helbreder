import datetime
from flask import Flask,request,json,render_template
from basic_auth import *

from modules.kubernetes import *
from modules.postgresql import *

from templates.modules_fcn import *
from templates.post import *

helbreder = Flask(__name__)

@helbreder.route('/', methods=['GET', 'POST'])
def static_main():
    global button_clicked
    module = modules_buttonized()
    action = '<h3>Waiting for module</h3>'
    target = '<h3>Waiting for module</h3>'
    code = 'Waiting for inputs'
    languages = lang_buttonized()
    if request.method == 'POST':
        action, target, code = collect_data()
    return render_template('index.html', module = module, action = action, target = target, button_clicked = button_clicked, code = code, languages = languages)

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
        t_name = t_name.replace('*', '')
        names = find_(ns, t_name, t_kind)
    else:
        names = [t_name]

    func = str(action + '_')

    for t_name in names:
        eval(func)(ns, t_name, t_kind)

    return f"[{datetime.datetime.now()}] action: {func.replace('_','')} on {t_kind}/{t_name}\n"

if __name__ == "__main__":
    helbreder.run(debug=True)
