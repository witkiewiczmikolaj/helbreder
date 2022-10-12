from paramiko import SSHClient, AutoAddPolicy
import paramiko
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

def Get_stats_CPU(rsa_key, rsa_password, ip, user, cpu_num):
    client = server_connect(rsa_key, rsa_password, ip, user)

    if cpu_num == 0:
        stat_prev = execute_command(client, 'cat /proc/stat')
        time.sleep(1)
        stat = execute_command(client, 'cat /proc/stat')
    else:
        stat_prev = execute_command(client, f'cat /proc/stat | grep cpu{cpu_num}')
        time.sleep(1)
        stat = execute_command(client, f'cat /proc/stat | grep cpu{cpu_num}')

    client.close()
    
    cpu_usage = str(server_info_calculation_cpu(stat, stat_prev))
    return "CPU USAGE: " + cpu_usage + "%"

def Get_stats_RAM(rsa_key, rsa_password, ip, user, temp):
    client = server_connect(rsa_key, rsa_password, ip, user)

    ram = execute_command(client, 'free -h')
    
    client.close()

    free_ram = server_info_calculation_ram(ram)
    return "FREE RAM: " + free_ram

def Get_stats_Primary_hard_drive_memory(rsa_key, rsa_password, ip, user, temp):
    client = server_connect(rsa_key, rsa_password, ip, user)

    mem = execute_command(client, 'df /')
    
    client.close()
    
    total, used, free = server_info_calculation_mem(mem)
    return "Total memory: " + total + " Kb\nUsed memory: " + used + " Kb\nFree memory: " + free + " Kb"

def Reboot_(rsa_key, rsa_password, ip, user, temp):
    client = server_connect(rsa_key, rsa_password, ip, user)

    reboot = execute_command(client, '/sbin/reboot')
    
    client.close()
    
    return "Server received a command to be rebooted. 'Is the server down?' you may ask. Idk man ping it or sth and see for yourself."
