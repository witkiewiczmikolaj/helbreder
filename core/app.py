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
    return "Roger that!"

@helbreder.route('/api/k8s',methods=['POST'])
@auth.login_required
def k8s():
    data = request.get_json()
    ns = data["namespace"]
    action = data["action"]
    t_name = data["target_name"]
    t_type = data["target_type"]

    if action == "kill":
        if t_type == "pod":
            kill_pod(ns,t_name)

    return f"Roger that!"

if __name__ == "__main__":
    helbreder.run(debug=True)