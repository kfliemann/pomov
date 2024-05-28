import appGui as Gui
import appTimer as Timer
import appConfig as Config

class App:

    def __init__(self) -> None:
        config = Config.AppConfig()
        Gui.start_gui()
        Timer.start_timer()

if __name__ == "__main__":
    app = App()