import datetime
import flask_login
from flask import Flask,request,json,render_template,abort
from basic_auth import *

from modules.kubernetes import *
from modules.postgresql import *
from modules.server import *
from modules.arguments import *

from templates.modules_fcn import *
from templates.api_safety import *
from templates.post import *
from templates.accounts import *
from templates.user_panel import *

helbreder = Flask(__name__)
helbreder.secret_key = os.environ.get('SECRET_KEY')

login_manager = flask_login.LoginManager()
login_manager.init_app(helbreder)

@login_manager.user_loader
def user_loader(email):
    if not email_check(email):
        return

    user = User(get_name(email))
    user.id = email
    return user

@login_manager.request_loader
def request_loader(request):
    email = request.form.get('email')
    if not email_check(email):
        return

    user = User(get_name(email))
    user.id = email
    return user

@helbreder.route('/', methods=['GET', 'POST'])
def static_main():
    global button_clicked
    module = modules_buttonized()
    action = '<h3>Waiting for module</h3>'
    target = '<h3>Waiting for module</h3>'
    languages = lang_buttonized()
    additional = '<h3>Waiting for module</h3>'
    if request.method == 'POST':
        try:
            action, target, additional, button_clicked = collect_data()
            if flask_login.current_user.is_authenticated:
                mod = request.form.get(button_clicked[0])
                module_psql_add(flask_login.current_user.name, mod)
        except KeyError:
            print('Choose action and target_kind first!')
    return render_template('html/index.html', module = module, action = action, target = target, button_clicked = button_clicked, languages = languages, additional = additional)

@helbreder.route('/code', methods=['GET'])
def code_outcome():
    try:
        code = lang_gen(request.args.get('code'))
        return render_template('html/code.html', code = code)
    except AttributeError:
        abort(500)

@helbreder.route('/login',methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return log_in()
    return render_template('html/login.html')

@helbreder.route('/signup',methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        sign_up()
    return render_template('html/signup.html')

@helbreder.route("/verify-email/<token>",methods=['GET'])
def verify_email(token):
    email = decode_email(token)
    if email_check(email) and not verified(email):
        try:
            verify(email)
        except jwt.exceptions.DecodeError:
            flash('Wrong link!')
    else:
        flash('You are already verified or you deleted your account earlier!')
    return render_template('html/login.html')

@helbreder.route("/panel",methods=['GET', 'POST'])
def user_panel():
    stats_modules = get_stats_module_combined()
    if request.method == 'POST':
        stats_modules = cpu_usage()
    return render_template('html/user_panel.html', stats_modules = stats_modules)

@helbreder.route("/delete-account/<token>",methods=['GET'])
def delete_account(token):
    email = decode_email(token)
    if email_check(email):
        try:
            delete_email(email)
        except jwt.exceptions.DecodeError:
            flash('Wrong link!')
    else:
        flash('There is no account assigned to this email!')
    return render_template('html/signup.html')

@helbreder.route('/logout')
@flask_login.login_required
def logout():
    flask_login.logout_user()
    flash('Logged out')
    return redirect(url_for('static_main'))

@helbreder.route('/api',methods=['POST'])
@auth.login_required
def api_base():
    data = new_request(request.get_json(), 'api')
    return "Hi!"

@helbreder.route('/api/server',methods=['POST'])
@auth.login_required
def server():
    data = new_request(request.get_json(), 'server')

    if validate_request('server', data):
        action = data["action"]
        t_kind = data["target_kind"]
        
        args = [os.environ.get('RSA_PRIVATE_KEY_FILE_PATH'), os.environ.get('RSA_PASSWORD')] + arguments(data)

        func = str(action + '_' + t_kind)
        server_response = eval(func)(args)
       
        return server_response
    else:
        abort(501)

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
