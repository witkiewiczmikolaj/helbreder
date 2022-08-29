from flask import Flask,request,json
from basic_auth import *

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

if __name__ == "__main__":
    helbreder.run(debug=True)