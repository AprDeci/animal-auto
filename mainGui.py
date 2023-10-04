import sys
import requests
from PyQt5 import QtCore
from PyQt5.QtCore import  QUrl,Qt
from PyQt5.QtGui import QDesktopServices, QIcon
from PyQt5.QtWidgets import QApplication
from qfluentwidgets import SplitFluentWindow, setThemeColor, NavigationAvatarWidget, NavigationItemPosition, MessageBox, \
    InfoBar, InfoBarPosition, FluentIcon
from Ui.cmdoutput_inter import cmdoutput
from Ui.controWin_inter import  controlWin_inter
from Ui.myIcon import myIcon
from Ui.setup_inter import setupWin

current_version = 1.8
class mainwindow(SplitFluentWindow):
    def __init__(self):
        super().__init__()
        setThemeColor('#0066CC')
        self.setWindowTitle("动物排队挂机脚本")
        self.setWindowIcon(QIcon("./imgs/ui/ico.png"))
        self.setMinimumSize(500,260)
        self.resize(500, 290)
        self.setFixedSize(self.width(), self.height())
        self.controwin=controlWin_inter()
        self.addSubInterface(self.controwin, myIcon.GAME, "游戏")
        self.cmdoutput = cmdoutput()
        self.addSubInterface(self.cmdoutput, myIcon.CMD, "统计")
        self.setupWin = setupWin()
        self.navigationInterface.addWidget(
            routeKey='avatar',
            widget=NavigationAvatarWidget('AprDec', './imgs/ui/aprdec.jpg'),
            onClick=self.showMessageBox,
            position=NavigationItemPosition.BOTTOM,
        )
        self.addSubInterface(self.setupWin, FluentIcon.SETTING, "设置",position=NavigationItemPosition.BOTTOM)


        self.controwin.print_signal.connect(self.cmdoutput.append_to_log)
        self.controwin.switch_signal.connect(self.Switchto)
        self.controwin.currentNum_signal.connect(self.cmdoutput.change_currentNum_Label)
        self.controwin.currentExp_signal.connect(self.cmdoutput.change_currentexp)
        self.check_version()

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

    def check_version(self):
        latest_version= requests.get('https://api.github.com/repos/q1263868407/animal-auto/releases/latest').json()['tag_name'][1:]
        if current_version<float(latest_version):
            InfoBar.new(
                icon=FluentIcon.GITHUB,
                title='',
                content=f"作者又叕叒更新啦,新版本{latest_version}已经发布啦,快去下载吧",
                orient=Qt.Horizontal,
                isClosable=True,  # disable close button
                position=InfoBarPosition.TOP_LEFT,
                duration=4000,
                parent=self
            ).setCustomBackgroundColor("#F5C563","#000000")
        else:
            InfoBar.success(
                title='',
                content=f"最新版本呢!",
                orient=Qt.Horizontal,
                isClosable=True,  # disable close button
                position=InfoBarPosition.TOP_LEFT,
                duration=2000,
                parent=self
            )
if __name__=="__main__":
    QApplication.setHighDpiScaleFactorRoundingPolicy(QtCore.Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)
    QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps)
    QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
    app = QApplication(sys.argv)
    window = mainwindow()
    window.show()
    app.exit(app.exec_())