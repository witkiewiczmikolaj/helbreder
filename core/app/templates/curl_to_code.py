import subprocess
import sys

def curl_to_code(command, language):
    print(language, command, file=sys.stderr)
    return subprocess.run(['curlconverter', '--language', language, command], text=True, capture_output=True, shell=True).stdout