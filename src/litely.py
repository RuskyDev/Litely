import requests
import json
from colorama import init, Fore
import os

init()

class Litely:
    def __init__(self, current_version):
        self.current_version = current_version

    def get_latest_release(self, repo):
        url = f"https://api.github.com/repos/{repo}/releases/latest"
        response = requests.get(url)
        if response.status_code == 200:
            data = json.loads(response.text)
            return data["tag_name"]
        else:
            return None

    def check_for_updates(self, repo):
        print(f"{Fore.WHITE}[{Fore.YELLOW}Litely{Fore.WHITE}] Checking for Updates...")
        latest_release = self.get_latest_release(repo)
        if latest_release and latest_release != self.current_version:
            print(f"{Fore.WHITE}[{Fore.YELLOW}Litely{Fore.WHITE}] Update found! Latest version: {latest_release}")
            self.download_update(repo, latest_release)
        else:
            print(f"{Fore.WHITE}[{Fore.YELLOW}Litely{Fore.WHITE}] No updates available.")

    def download_update(self, repo, latest_version):
        print(f"{Fore.WHITE}[{Fore.YELLOW}Litely{Fore.WHITE}] Downloading update...")
        url = f"https://github.com/{repo}/raw/{latest_version}/update.bat"
        response = requests.get(url)
        if response.status_code == 200:
            with open("temp/update.bat", "wb") as file:
                file.write(response.content)
            print(f"{Fore.WHITE}[{Fore.YELLOW}Litely{Fore.WHITE}] Update downloaded successfully.")
        else:
            print(f"{Fore.WHITE}[{Fore.YELLOW}Litely{Fore.WHITE}] Failed to download the update.")