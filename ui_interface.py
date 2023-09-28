from PyQt5.QtWidgets import  QWidget
from fluentuidemo1 import Ui_mainWindow
from qfluentwidgets import FluentIcon as FIF
class uiInter(QWidget,Ui_mainWindow):
    def __init__(self,parent=None):
        super().__init__(parent=parent)
        self.setupUi(self)
        self.Githublink.setIcon(FIF.GITHUB)
        self.BlogLink.setIcon(FIF.LINK)