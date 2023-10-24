import subprocess

script_path = r"C:\WRCp\folder_encrypt.ps1"
subprocess.call(["powershell.exe", "-ExecutionPolicy", "Unrestricted", script_path])
