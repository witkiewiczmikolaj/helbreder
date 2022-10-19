import subprocess
import sys

def curl_to_code(command, language):
    return subprocess.run(['curlconverter', '--language', str(language + ' ' + command)], text=True, capture_output=True, shell=True).stdout