import subprocess

def curl_to_code(command, language):
    return subprocess.run(['curlconverter', '--language', language, '-'], text=True, input=command, capture_output=True, shell=True).stdout
