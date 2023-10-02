import sys
import time

from PyQt5 import QtCore
from PyQt5.QtCore import pyqtSignal, QUrl
from PyQt5.QtGui import QDesktopServices, QIcon
from PyQt5.QtWidgets import QApplication
from qfluentwidgets import  FluentIcon as FIF, SplitFluentWindow, setTheme, Theme, setThemeColor, \
    NavigationAvatarWidget, NavigationItemPosition, MessageBox

from Ui.cmdoutput_inter import cmdoutput
from Ui.controWin_inter import  controlWin_inter
from Ui.myIcon import myIcon


class mainwindow(SplitFluentWindow):
    def __init__(self):
        super().__init__()
        setThemeColor('#0066CC')
        self.setWindowTitle("动物排队挂机脚本")
        self.setWindowIcon(QIcon("./imgs/ui/ico.png"))
        self.setMinimumSize(500,245)
        self.resize(500, 245)
        self.setFixedSize(self.width(), self.height())
        self.controwin=controlWin_inter()
        self.addSubInterface(self.controwin, myIcon.GAME, "游戏")
        self.cmdoutput = cmdoutput()
        self.addSubInterface(self.cmdoutput, myIcon.CMD, "统计")
        self.navigationInterface.addWidget(
            routeKey='avatar',
            widget=NavigationAvatarWidget('AprDec', './imgs/ui/aprdec.jpg'),
            onClick=self.showMessageBox,
            position=NavigationItemPosition.BOTTOM,
        )

        self.controwin.print_signal.connect(self.cmdoutput.append_to_log)
        self.controwin.switch_signal.connect(self.Switchto)
        self.controwin.currentNum_signal.connect(self.cmdoutput.change_currentNum_Label)

    def showMessageBox(self):
        w = MessageBox(
            '支持作者🥰',
            '学习作品,如果觉得不错,打赏一杯柠檬水吧🍸,或者给本项目点个Star吧✨',
            self
        )
        w.yesButton.setText('支持一波')
        w.cancelButton.setText('下次一定')
        if w.exec():
            QDesktopServices.openUrl(QUrl("https://afdian.net/a/Aprdec"))
    def Switchto(self):
        self.switchTo(self.cmdoutput)
if __name__=="__main__":
    QApplication.setHighDpiScaleFactorRoundingPolicy(QtCore.Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)
    QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps)
    QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
    app = QApplication(sys.argv)
    window = mainwindow()
    window.show()
    app.exit(app.exec_())