import sys
import gui.appGui as Gui
import config.appConfig as Config
from PyQt6.QtWidgets import QApplication


class App:

    def __init__(self) -> None:
        self.config = Config.AppConfig()
        print(self.config.readSettings)
        self.gui = Gui.AppGui()  

if __name__ == "__main__":
    window = QApplication(sys.argv)
    app = App()
    sys.exit(window.exec())