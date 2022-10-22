import subprocess

def command_maker(command):
    return command.split(' ')

def curl_to_code(command, language):
    command = command_maker(command)
    curl_converted = ['curlconverter', '--language', language, command]
    curl_converted = subprocess.check_output(curl_converted).decode("utf-8") 
    return curl_converted
