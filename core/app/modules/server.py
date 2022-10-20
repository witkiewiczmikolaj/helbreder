from paramiko import SSHClient, AutoAddPolicy
import paramiko
import time
import os
import threading

def server_connect(arguments):
    rsa_key, rsa_password, ip, user = arguments[0], arguments[1], arguments[5], arguments[3]
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
    # /proc/stat returns info about how much time CPU 
    # needed to do some actions so we have to calculate 
    # all of them and compare the change between current
    # one and previous one

    # First we add the idle times for previous and current readings
    # Then we do the same for non idle times
    # We subject previous times from current ones
    # At last by dividing the total times minus idle by total time we 
    # get percentage use of CPU

    PrevIdle = stat_prev[3] + stat_prev[4]
    Idle = stat[3] + stat[4]

    PrevNonIdle = stat_prev[0] + stat_prev[1] + stat_prev[2] + stat_prev[5] + stat_prev[6] + stat_prev[7]
    NonIdle = stat[0] + stat[1] + stat[2] + stat[5] + stat[6] + stat[7]

    PrevTotal = PrevIdle + PrevNonIdle
    Total = Idle + NonIdle
    totald = Total - PrevTotal
    idled = Idle - PrevIdle

    cpu_load = round((totald - idled)/totald * 100, 10)
    return cpu_load

def server_info_calculation_ram(ram):
    ram = ram.split()
    return ram[9]   

def server_info_calculation_mem(mem):
    mem = mem.split()
    return mem[8], mem[9], mem[10]

def Get_stats_CPU(arguments):
    cpu_num = arguments[6]
    client = server_connect(arguments)
    nproc = int(execute_command(client, 'nproc'))

    if cpu_num == "all":
        stat_prev = execute_command(client, 'cat /proc/stat')
        time.sleep(1)
        stat = execute_command(client, 'cat /proc/stat')
        usage = "CPU USAGE: " + str(server_info_calculation_cpu(stat, stat_prev)) + "%"
    elif cpu_num.isdigit() and int(cpu_num) < nproc:
        stat_prev = execute_command(client, f'cat /proc/stat | grep cpu{cpu_num}')
        time.sleep(1)
        stat = execute_command(client, f'cat /proc/stat | grep cpu{cpu_num}')
        usage = "CPU USAGE: " + str(server_info_calculation_cpu(stat, stat_prev)) + "%"
    else:
        usage = "Resource type exceeds cpu number used by the server, or you passed wrong argument!"

    client.close()
    
    return usage

def Get_stats_RAM(arguments):
    client = server_connect(arguments)

    ram = execute_command(client, 'free -h')
    
    client.close()

    free_ram = server_info_calculation_ram(ram)
    return "FREE RAM: " + free_ram

def Get_stats_Memory_main(arguments):
    client = server_connect(arguments)

    mem = execute_command(client, 'df /')
    
    client.close()
    
    total, used, free = server_info_calculation_mem(mem)
    return "Total memory: " + total + " Kb\nUsed memory: " + used + " Kb\nFree memory: " + free + " Kb"

def uptime_loop(arguments):
    response = 1
    global uptime
    while(response != 0):
        try:
            client = server_connect(arguments)
            uptime = execute_command(client, 'uptime')
            client.close()
            response = 0
        except:
            pass
        time.sleep(10)

def Reboot_None(arguments):
    ip = arguments[5]
    client = server_connect(arguments)

    execute_command(client, '/sbin/reboot')
    
    client.close()

    uptime_thread = threading.Thread(target=uptime_loop(arguments))
    uptime_thread.start()
            
    return "Server " + ip + " rebooted successfully!\n" + "Uptime: " + uptime
