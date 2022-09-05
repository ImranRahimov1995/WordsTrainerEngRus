import subprocess
import sys

word = sys.argv[1]

command = f"echo \"{word}\" | RHVoice-client -s Anna+CLB | aplay"

subprocess.call(command,shell=True)
