import tkinter as tk
import pyautogui
import keyboard
import pygetwindow as gw
import psutil
import win32process
from time import sleep

class MouseMenu:
    def __init__(self, data):
        self.root = tk.Tk()
        self.root.geometry("0x0")
        self.root.overrideredirect(True)
        self.menu = tk.Menu(self.root, tearoff=0)
        self.menu_position = (0, 0)  # Inicializa a posição do menu como (0, 0)
        self.data = data

    def show_menu(self):
        x, y = pyautogui.position()
        self.menu_position = (x, y)
        self.build_menu_by_type()
        self.menu.post(x, y)
        self.root.update()

    def getActiveWindow(self):
        active_window = gw.getActiveWindow()
        # Obtém o ID do processo da janela ativa
        if active_window:
            hwnd = active_window._hWnd
            _, pid = win32process.GetWindowThreadProcessId(hwnd)
            
            # Obtém o nome do processo com base no ID do processo
            process = psutil.Process(pid)
            process_name = process.name().lower()
            
            return process_name, active_window
        else:
            return False, None

    def build_menu_by_type(self):
        process_name, active_window = self.getActiveWindow()
        if process_name in self.data["chat"]:
            options = self.data["chat"][process_name]
            self.build_menu(options)
        else:
            options = self.data["chat"]["default"]
            self.build_menu(options)

    def build_menu(self, options, parent=None):
        for key, value in options.items():
            if isinstance(value, dict):
                submenu = tk.Menu(parent or self.menu, tearoff=0)
                if parent is None:
                    self.menu.add_cascade(label=key, menu=submenu)
                else:
                    parent.add_cascade(label=key, menu=submenu)
                self.build_menu(value, submenu)
            else:
                parent.add_command(label=key, command=lambda v=value: self.menu_command(v))

    def menu_command(self, command):
        action, message = command
        menu_x, menu_y = self.menu_position
        pyautogui.click(menu_x, menu_y)
        if action == "paste":
            message = message.split("$newLine$")
            for index, line in enumerate(message):
                keyboard.write(line)
                if index == len(message)-1:
                    continue
                    # TODO - check if necessary | avoid to send the last msg, allows the user edit something.
                    keyboard.press_and_release('enter')
                    sleep(.4)
                else:
                    keyboard.press_and_release('shift+enter')
                    sleep(.3)
        elif action == "write":
            keyboard.write(message)
        self.root.quit()

