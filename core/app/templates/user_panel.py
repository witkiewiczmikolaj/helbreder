from flask import request
from modules.server import *
from templates.psql import *
from templates.post import button_clicked

def cpu_usage():
    cpu_num = request.form.get('cpu_num')
    arguments = ['0','1','2','3','4','5']
    arguments[0] = os.environ.get('RSA_PRIVATE_KEY_FILE_PATH')
    arguments[1] = os.environ.get('RSA_PASSWORD')
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

def module_psql_add(name):
    module = button_clicked[0]
    cur.execute(f"UPDATE ACCOUNTS_ONLINE SET '{module}' = '{module}' + 1 WHERE username = '{name}';")
    c.commit()