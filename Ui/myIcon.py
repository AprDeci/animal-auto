from enum import Enum

from qfluentwidgets import getIconColor, Theme, FluentIconBase


class myIcon(FluentIconBase, Enum):
    """ Custom icons """

    CMD='cmd'
    GAME='游戏'

    def path(self, theme=Theme.AUTO):
        return f'./imgs/ui/{self.value}.svg'
