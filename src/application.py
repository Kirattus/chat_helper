import sys
from PyQt6.QtWidgets import QApplication, QSystemTrayIcon, QMenu
from PyQt6.QtGui import QIcon, QAction
import keyboard

from src.jsonManager import load as json_load
from src.mouseMenu import MouseMenu

class ChatHelperIconApp(QApplication):
    def __init__(self, argv):
        super().__init__(argv)
        self.keyboard_listener = None
        self.data = None
        self.initUI()

    def initUI(self):
        # Criar o ícone para a bandeja do sistema
        self.tray_icon = QSystemTrayIcon(QIcon("src/app.ico"), parent=self)
        self.tray_icon.setToolTip("Meu Aplicativo Tray")

        # Criar um menu para o ícone
        self.tray_menu = QMenu()

        # Adicionar ação "Ativar/Desativar"
        self.active_action = QAction("Ativar", parent=self)
        self.active_action.setCheckable(True)
        self.active_action.setChecked(False)
        self.active_action.triggered.connect(self.toggle_active)
        self.tray_menu.addAction(self.active_action)

        # Adicionar uma separador
        self.tray_menu.addSeparator()

        # Adicionar ação "Sair"
        self.exit_action = QAction("Sair", parent=self)
        self.exit_action.triggered.connect(self.exit)
        self.tray_menu.addAction(self.exit_action)

        # Configurar o menu para o ícone da bandeja
        self.tray_icon.setContextMenu(self.tray_menu)

        # Exibir o ícone na bandeja do sistema
        self.tray_icon.show()

    def toggle_active(self):
        if self.active_action.isChecked():
            self.data = json_load()
            if not self.data:
                self.active_action.setChecked(False)
            else:
                keyboard.add_hotkey(self.data['hotkey'], self.show_menu)
        else:
            keyboard.remove_hotkey(self.data['hotkey'])

    def show_menu(self):
        MouseMenu(self.data).show_menu()

    def exit(self):
        self.quit()

def application():
    app = ChatHelperIconApp(sys.argv)
    sys.exit(app.exec())
