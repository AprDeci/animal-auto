import sys

from PyQt5.QtCore import QObject, pyqtSignal, QProcess
from PyQt5.QtWidgets import QMainWindow, QApplication

from window import Ui_MainWindow
import main

class MymainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def beginmain(self):
        main.main()

if __name__ == '__main__':
    app = QApplication(sys.argv)  # 在 QApplication 方法中使用，创建应用程序对象
    myWin = MymainWindow()  # 实例化 MyMainWindow 类，创建主窗口
    myWin.show()  # 在桌面显示控件 myWin
    sys.exit(app.exec_())  # 结束进程，退出程序