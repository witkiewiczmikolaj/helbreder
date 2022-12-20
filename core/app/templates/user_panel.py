import flask_login
import time
import datetime
import json
import plotly
import plotly.express as px
import pandas as pd
from flask import request, flash
from modules.server import *
from templates.modules_fcn import *
from templates.psql import *

def cpu_usage():
    global usage_data, time_data
    cpu_num = request.form.get('cpu_num')
    rsa_key, rsa_password, ip, user = request.form.get('rsa_key'), request.form.get('rsa_password'), request.form.get('ip'), request.form.get('user')
    usage_data = []
    time_data = []
    client = server_connect_rsa(rsa_key, rsa_password, ip, user)

    for i in range(10):
        usage = get_cpu_usage(client, cpu_num)
        currentDateAndTime = datetime.datetime.now()
        currentTime = currentDateAndTime.strftime("%H:%M:%S")
        usage_data.append(usage)
        time_data.append(currentTime)
        time.sleep(1)

    client.close()

def cpu_usage_thread():
    cpu_usage_thread = threading.Thread(target=cpu_usage())
    cpu_usage_thread.start()
    return usage_data, time_data

def make_graph(usage_data, time_data):
    df = pd.DataFrame(dict(
        x = time_data,
        y = usage_data
    ))
    df = df.sort_values(by="x")
    fig = px.line(df, x="x", y="y", title="CPU Usage",labels={
                     "x": "Time [H:M:S]",
                     "y": "Usage [%]",
                    })
    fig.update_layout(
        paper_bgcolor="rgb(215, 214, 214)",
        plot_bgcolor="rgb(108, 106, 106)",
        width=1800
    )
    fig.update_traces(
        line_color="white"
    )
    graph = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    
    return graph

def module_psql_add(name, module):
    cur.execute(f"UPDATE ACCOUNTS_2 SET {module} = {module} + 1 WHERE username = '{name}';")
    c.commit()

def get_stats_module(name, module):
    cur.execute(f"SELECT {module} FROM ACCOUNTS_2 WHERE username = '{name}'")
    return cur.fetchone()[0]

def get_stats_module_combined():
    values_modules = []
    stats_modules = []
    all_modules = 0
    for i in range (len(modules())):
        values_modules.append(get_stats_module(flask_login.current_user.name, modules()[i]))
        all_modules += get_stats_module(flask_login.current_user.name, modules()[i])
    values_modules = [(x / all_modules * 100) for x in values_modules] 
    
    for i in range (len(modules())):
        stats_modules.append("<a>" + modules()[i].title() + ": " + str(get_stats_module(flask_login.current_user.name, modules()[i])) + " | " + str(round(values_modules[i],1)) + """%</a><div style="background-color:rgb(36, 36, 36); height: 10px; width: 100px;"><div style="background-color:rgb(238, 237, 237); height: 10px; float: left; width: """ + str(values_modules[i]) + """px;"></div></div>""")
        
    all_modules = "<p>All requests: " + str(all_modules) + "</p>"
    stats_modules.append(all_modules)
    stats_modules = ' '.join(stats_modules)
    return stats_modules