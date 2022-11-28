from modules.server import *

def cpu_usage(arguments):
    cpu_num = arguments[6]
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