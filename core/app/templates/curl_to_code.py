import subprocess

def curl_to_code(command, language):
    curl_converted = ['curlconverter', '--language', language] + command.split(' ')
    curl_converted = subprocess.check_output(curl_converted).decode("utf-8") 
    return curl_converted