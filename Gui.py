import sys
from PyQt5 import QtCore
from PyQt5.QtCore import QThread, QLocale, pyqtSignal
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow, QApplication
from qfluentwidgets import setThemeColor, FluentTranslator,FluentIcon as FIF
import room
from fluentuidemo1 import Ui_mainWindow
import main
class WorkerThread(QThread):
    finished = pyqtSignal()  # 操作完成时发射的信号
    def __init__(self, operation_func, *args, **kwargs):
        super().__init__()
        self.operation_func = operation_func
        self.args = args
        self.kwargs = kwargs
    def run(self):
        self.operation_func(*self.args, **self.kwargs)
    def stop(self):
        self.terminate()
        self.finished.emit()
class MymainWindow(QMainWindow, Ui_mainWindow):
    shutdown = False
    limitNumber = False
    gameNumber = 0
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        setThemeColor('#0066CC')
        # change title bar
        self.setWindowTitle('动物排队挂机脚本')
        self.setWindowIcon(QIcon('ico.png'))
        self.Githublink.setIcon(FIF.GITHUB)
        self.BlogLink.setIcon(FIF.LINK)
        self.operation_thread = None
        self.ifshutdown.clicked.connect(lambda: self.ifNumber.setChecked(True))
    def getinfo(self):
        self.shutdown = self.ifshutdown.isChecked()
        self.limitNumber = self.ifNumber.isChecked()
        self.gameNumber = self.gameNumberInput.value()

    def start_operation_thread(self, operation_func, *args, **kwargs):
        if not self.operation_thread or not self.operation_thread.isRunning():
            self.operation_thread = WorkerThread(operation_func, *args, **kwargs)
            self.operation_thread.finished.connect(self.on_operation_finished)
            self.operation_thread.start()
            match operation_func:
                case room.roomgame:
                    self.roombuttom.setText("停止脚本")
                    self.quickgamebutton.setEnabled(False)
                case main.main:
                    self.quickgamebutton.setText("停止脚本")
                    self.roombuttom.setEnabled(False)
        else:
            self.operation_thread.stop()
            match operation_func:
                case room.roomgame:
                    self.roombuttom.setText("自建房间")
                    self.quickgamebutton.setEnabled(True)
                case main.main:
                    self.quickgamebutton.setText("快速游戏")
                    self.roombuttom.setEnabled(True)


    def on_operation_finished(self):
        pass



    def beginquick(self):
        self.getinfo()
        self.start_operation_thread(main .main, self.limitNumber, self.shutdown, self.gameNumber)
    def beginroom(self):
        self.start_operation_thread(room.roomgame)



if __name__ == '__main__':
    #enabel dpi scaling
    QApplication.setHighDpiScaleFactorRoundingPolicy(QtCore.Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)
    QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps)
    QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
    app = QApplication(sys.argv)  # 在 QApplication 方法中使用，创建应用程序对象
    app.installTranslator(FluentTranslator(QLocale()))
    myWin = MymainWindow()  # 实例化 MyMainWindow 类，创建主窗口
    myWin.show()  # 在桌面显示控件 myWin
    sys.exit(app.exec_())  # 结束进程，退出程序