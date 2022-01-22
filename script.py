import psutil
import time
import os

blocked_apps = open("blocked.txt").read().split("\n")

print(blocked_apps)

while True:
    for app in blocked_apps:
        if app in (process.name() for process in psutil.process_iter()):
            os.system(f'TASKKILL /F /IM {app}')
    time.sleep(5)
