import sys

from PyQt5 import QtCore
from PyQt5.QtCore import QThread, QLocale, pyqtSignal
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow, QApplication
from qfluentwidgets import setThemeColor, FluentTranslator
import room
from ui_interface import uiInter
import main

class WorkerThread(QThread):
    finished = pyqtSignal()  # 操作完成时发射的信号

    def __init__(self, limitNumber, shutdown, gameNumber):
        super().__init__()
        self.limitNumber = limitNumber
        self.shutdown = shutdown
        self.gameNumber = gameNumber
    def run(self):
        main.main(self.limitNumber, self.shutdown, self.gameNumber)
class MymainWindow(QMainWindow, uiInter):
    shutdown = False
    limitNumber = False
    gameNumber = 0
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        setThemeColor('#28afe9')
        # change title bar
        self.setWindowTitle('动物排队挂机脚本')
        self.setWindowIcon(QIcon('ico.png'))

        self.worker_thread = None
    def getinfo(self):
        self.shutdown = self.ifshutdown.isChecked()
        self.limitNumber = self.ifNumber.isChecked()
        self.gameNumber = self.gameNumberInput.value()

    def start_worker_thread(self):
        if self.worker_thread is None or not self.worker_thread.isRunning():
            self.worker_thread = WorkerThread(self.limitNumber, self.shutdown, self.gameNumber)
            self.worker_thread.start()

    def on_worker_finished(self):
        pass

    def beginquick(self):
        self.getinfo()
        self.start_worker_thread()
    def beginroom(self):
        room.roomgame()
if __name__ == '__main__':
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
    app = QApplication(sys.argv)  # 在 QApplication 方法中使用，创建应用程序对象
    app.installTranslator(FluentTranslator(QLocale()))
    myWin = MymainWindow()  # 实例化 MyMainWindow 类，创建主窗口
    myWin.show()  # 在桌面显示控件 myWin
    sys.exit(app.exec_())  # 结束进程，退出程序