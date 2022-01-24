import psutil
import time
import os
import requests
from dotenv import load_dotenv

load_dotenv()

blocked_apps = open("blocked.txt").read().split("\n")

def are_all_complete(dailies):
    for daily in dailies:
        if daily["isDue"] and not daily["completed"]:
            return False
    return True

while True:
    for app in blocked_apps:
        if app in (process.name() for process in psutil.process_iter()):
            headers = {
            "x-client": os.getenv("X_CLIENT"),
            "x-api-user": os.getenv("X_API_USER"),
            "x-api-key": os.getenv("X_API_KEY")
        }

            dailies = requests.get(
                "https://habitica.com/api/v3/tasks/user?type=dailys",
                headers=headers
            ).json()["data"]
            is_asleep = requests.get(
                "https://habitica.com/api/v3/user",
                headers=headers
            ).json()["data"]["preferences"]["sleep"]

            if not are_all_complete(dailies) and not is_asleep:
                os.system(f'TASKKILL /F /IM {app}')
    
    time.sleep(5)
