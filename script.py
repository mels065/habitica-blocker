import psutil
import time
import os
import requests
from dotenv import load_dotenv

from utils.util import *

load_dotenv()

blocked_apps = open("blocked.txt").read().split("\n")

def run_blocker():
    while True:
        for app in blocked_apps:
            if app in (process.name() for process in psutil.process_iter()):
                headers = {
                "x-client": "b7d26b77-2aa8-4f99-9876-aeaf57b46d92",
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

if __name__ == "__main__":
    run_blocker()
