import os
import requests
import zipfile
import shutil
import sys

base_dir = os.path.dirname(sys.executable)

def get_local_version():
    global base_dir
    version_path = os.path.join(base_dir, "version.txt")
    with open(version_path) as f:
        return f.read().strip()
    
def get_curr_version():
    url = "https://raw.githubusercontent.com/lsy341/git_update/main/version.txt"
    response = requests.get(url)
    return response.text.strip()

def get_latest_zip():
    global base_dir
    url = "https://github.com/lsy341/git_update/raw/refs/heads/main/latest.zip"
    response = requests.get(url)
    download_path = os.path.join(base_dir, "latest.zip")
    
    with open(download_path, "wb") as f:
        f.write(response.content)
        
    with zipfile.ZipFile(download_path, "r") as zip:
        zip.extractall("update_tmp")

def replace_file():
    update_dir = "update_tmp"
    update_files = ["version.txt", "main.exe"]
    
    for update_file in update_files:
        src = os.path.join(update_dir, update_file)
        dst = os.path.join('.', update_file)
        
        if os.path.exists(dst):
            os.remove(dst)
            
        shutil.move(src, dst)
        
    if os.path.exists("latest.zip"):
        os.remove("latest.zip")
        
    if os.path.exists("update_tmp"):
        shutil.rmtree("update_tmp")
        
def run_main():
    os.startfile("main.exe")
    
def main():
    local_version = get_local_version()
    curr_version = get_curr_version()
    
    if local_version != curr_version:
        print(f"local_version = {local_version}")
        print(f"curr_version = {curr_version}")
        print("업데이트 있음")
        get_latest_zip()
        replace_file()
        run_main()
    else:
        print("업데이트 없음")
        run_main()

    

if __name__ == "__main__":
    main()