import flask_login
import threading
from flask import request
from modules.server import *
from templates.modules_fcn import *
from templates.psql import *

def cpu_usage():
    cpu_num = request.form.get('cpu_num')
    arguments = ['0','1','2','3','4','5']
    arguments[0] = request.form.get('rsa_key')
    arguments[1] = request.form.get('rsa_password')
    arguments[5] = request.form.get('ip')
    arguments[3] = request.form.get('user')
    client = server_connect(arguments)
    nproc = int(execute_command(client, 'nproc'))

    if cpu_num == "all":
        stat_prev = execute_command(client, 'cat /proc/stat')
        time.sleep(1)
        stat = execute_command(client, 'cat /proc/stat')
        usage = server_info_calculation_cpu(stat, stat_prev)
    elif cpu_num.isdigit() and int(cpu_num) < nproc:
        stat_prev = execute_command(client, f'cat /proc/stat | grep cpu{cpu_num}')
        time.sleep(1)
        stat = execute_command(client, f'cat /proc/stat | grep cpu{cpu_num}')
        usage = server_info_calculation_cpu(stat, stat_prev)
    else:
        usage = 0
    client.close()
    
    return usage

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