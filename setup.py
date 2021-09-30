import os
import subprocess

dir_path = os.path.dirname(os.path.realpath(__file__))
os.chdir(dir_path)

# os.system(f"pip install -r {dir_path}\\requirements.txt")
# os.system(f"python {dir_path}\\main.py")
subprocess.check_call("pip install -r requirements.txt", shell=True)
subprocess.check_call("python main.py", shell=True)

while True:
    input()