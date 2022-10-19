import subprocess
import sys

def curl_to_code(command, language):
    print(command, file=sys.stderr)
    return subprocess.run(['curlconverter', '--language', language, '-'], text=True, input=command, capture_output=True, shell=True).stdout