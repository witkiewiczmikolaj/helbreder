from paramiko import SSHClient, AutoAddPolicy
import paramiko
import os
import time

def server_connect(rsa_key, rsa_password, ip, user):
    k = paramiko.RSAKey.from_private_key_file(f'{rsa_key}', f'{rsa_password}')
    client = SSHClient()
    client.set_missing_host_key_policy(AutoAddPolicy())
    client.connect(f'{ip}', username=user, pkey=k)
    return client

def execute_command(client, command):
    exec = client.exec_command(f'{command}')
    response = exec[1].read().decode("utf8")
    exec[1].close()
    return response

def server_info_calculation_cpu(stat, stat_prev):
    stat = [int(x) for x in stat.split()[1:11]]
    stat_prev = [int(x) for x in stat_prev.split()[1:11]]
    
    PrevIdle = stat_prev[3] + stat_prev[4]
    Idle = stat[3] + stat[4]

    PrevNonIdle = stat_prev[0] + stat_prev[1] + stat_prev[2] + stat_prev[5] + stat_prev[6] + stat_prev[7]
    NonIdle = stat[0] + stat[1] + stat[2] + stat[5] + stat[6] + stat[7]

    PrevTotal = PrevIdle + PrevNonIdle
    Total = Idle + NonIdle
    totald = Total - PrevTotal
    idled = Idle - PrevIdle

    cpu_load = round((totald - idled)/totald * 100, 2)
    return cpu_load

def server_info_calculation_ram(ram):
    ram = ram.split()
    return ram[9]   

def server_info_calculation_mem(mem):
    mem = mem.split()
    return mem[8], mem[9], mem[10]

def server_info_cpu(rsa_key, rsa_password, ip, user, cpu_num):
    client = server_connect(rsa_key, rsa_password, ip, user)

    if cpu_num == 0:
        stat_prev = execute_command(client, 'cat /proc/stat')
        time.sleep(1)
        stat = execute_command(client, 'cat /proc/stat')
    else:
        num = cpu_num - 1
        stat_prev = execute_command(client, f'cat /proc/stat | grep cpu{num}')
        time.sleep(1)
        stat = execute_command(client, f'cat /proc/stat | grep cpu{num}')

    client.close()
    
    return server_info_calculation_cpu(stat, stat_prev)

def server_info_ram(rsa_key, rsa_password, ip, user):
    client = server_connect(rsa_key, rsa_password, ip, user)

    ram = execute_command(client, 'free -h')
    
    client.close()
    
    return server_info_calculation_ram(ram)

def server_info_mem(rsa_key, rsa_password, ip, user):
    client = server_connect(rsa_key, rsa_password, ip, user)

    mem = execute_command(client, 'df /')
    
    client.close()
    
    return server_info_calculation_mem(mem)

def server_reboot(rsa_key, rsa_password, ip, user):
    client = server_connect(rsa_key, rsa_password, ip, user)

    reboot = execute_command(client, '/sbin/reboot')
    
    client.close()
    
    return reboot

def server_response(action, t_kind, t_name, user):
    if action == 'Get_stats' and t_kind == 'CPU':
        response = "CPU USAGE: " + str(server_info_cpu(os.environ.get('RSA_PRIVATE_KEY_FILE_PATH'), os.environ.get('RSA_PASSWORD'), t_name, user, 0)) + "%"
    elif action == 'Get_stats' and t_kind == 'CPU0':
        response = "CPU USAGE: " + str(server_info_cpu(os.environ.get('RSA_PRIVATE_KEY_FILE_PATH'), os.environ.get('RSA_PASSWORD'), t_name, user, 1)) + "%"
    elif action == 'Get_stats' and t_kind == 'CPU1':
        response = "CPU USAGE: " + str(server_info_cpu(os.environ.get('RSA_PRIVATE_KEY_FILE_PATH'), os.environ.get('RSA_PASSWORD'), t_name, user, 2)) + "%"
    elif action == 'Get_stats' and t_kind == 'RAM':
        response = "FREE RAM: " + server_info_ram(os.environ.get('RSA_PRIVATE_KEY_FILE_PATH'), os.environ.get('RSA_PASSWORD'), t_name, user)
    elif action == 'Get_stats' and t_kind == 'Primary hard drive memory':
        total, used, free = server_info_mem(os.environ.get('RSA_PRIVATE_KEY_FILE_PATH'), os.environ.get('RSA_PASSWORD'), t_name, user)
        response = "Total memory: " + total + " Kb\nUsed memory: " + used + " Kb\nFree memory: " + free + " Kb"
    elif action == 'Reboot':
        response = "Server rebooted! " + server_reboot(os.environ.get('RSA_PRIVATE_KEY_FILE_PATH'), os.environ.get('RSA_PASSWORD'), t_name, user)
    return response
