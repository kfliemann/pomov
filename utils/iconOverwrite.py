from enum import Enum
from qfluentwidgets import getIconColor, Theme, FluentIconBase


class IconOverwrite(FluentIconBase, Enum):
    """ Custom icons """

    RESTART = "Restart"
    TIMER_ON = "TimerOn"
    TIMER_OFF = "TimerOff"

    def path(self, theme=Theme.AUTO):
        # getIconColor() return "white" or "black" according to current theme
        return f'./pomov/media/img/icon/{self.value}_{getIconColor(theme)}.svg'
