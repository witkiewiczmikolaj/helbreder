import subprocess
import sys

def curl_to_code(command, language):
    curl_conversion = ['curlconverter', '--language', language, command]
    return subprocess.check_output(curl_conversion)