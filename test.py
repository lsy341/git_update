import os
import requests

def get_local_version():
    base_dir = os.path.dirname(__file__)
    version_path = os.path.join(base_dir, "version.txt")
    with open(version_path) as f:
        return f.read().strip()
    
def get_curr_verison():
    url = "https://raw.githubusercontent.com/lsy341/git_update/main/version.txt"
    response = requests.get(url)
    return response.text

    

print(get_curr_verison() == get_local_version())