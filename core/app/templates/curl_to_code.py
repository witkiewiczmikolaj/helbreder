import subprocess

def curl_to_code(command, language):
    #return subprocess.run(['curlconverter', '--language', language, '-'], text=True, input=command, capture_output=True, shell=True).stdout
    curl_converted = ['curlconverter', '--language', language] + command.split(' ')
    curl_converted = subprocess.check_output(curl_converted).decode("utf-8") 
    return curl_converted