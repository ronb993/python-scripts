import platform
import subprocess
import winsound
import os
import time

frequency = 1000
duration = 1000
host = '8.8.8.8'

def ping(host):
    """
    returns true if host (str) responds
    """
    param = '-n' if platform.system().lower()=='windows' else '-c'
    command = ['ping', param, '1', host]

    return subprocess.call(command) == 0

while True:
    if ping(host) == True:
        print("host is up!")
        winsound.Beep(frequency, duration)
        break
    else:
        print("We are down, trying again")
        
