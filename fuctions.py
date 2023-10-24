import pyautogui as pa
import pyperclip as pp
import subprocess as sub
import threading
import winreg

class MOUSEc():
    def __init__(self) -> None:
        pass
    
    def setCoor(self, x, y, isClick):
        pa.moveTo(x, y)
        if isClick:
            pa.click()

    def autoMouse(self):
        while 1:
            pa.click()

class KEYBOARDc():
    def __init__(self) -> None:
        pass

    def write(self, s):
        pp.copy(s)
        pa.hotkey('ctrl', 'v')

class OSc():
    def __init__(self) -> None:
        pass

    def CMD(self, s):
        sub.Popen(s)

    def add_to_startup(program_name, executable_path):
        key = winreg.HKEY_CURRENT_USER
        key_path = r"Software\Microsoft\Windows\CurrentVersion\Run"

        try:
            with winreg.OpenKey(key, key_path, 0, winreg.KEY_WRITE) as reg_key:
                winreg.SetValueEx(reg_key, program_name, 0, winreg.REG_SZ, executable_path)
                print(f"{program_name}이(가) 시작 프로그램에 추가되었습니다.")
        except Exception as e:
            print(f"오류: {str(e)}")
