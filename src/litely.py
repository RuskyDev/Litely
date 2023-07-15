import requests
import json

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
        print("[Litely] Checking for Updates...")
        latest_release = self.get_latest_release(repo)
        if latest_release and latest_release != self.current_version:
            print(f"[Litely] Update found! Latest version: {latest_release}")
        else:
            print("[Litely] No updates available.")
