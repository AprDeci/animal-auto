import sys

from PyQt5 import QtCore
from PyQt5.QtGui import QTextCursor
from PyQt5.QtWidgets import QWidget, QApplication
from Ui.cmdoutput import Ui_Cmdoutput



class cmdoutput(QWidget, Ui_Cmdoutput):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.Cmd.setReadOnly(True)
        self.setContentsMargins(0,30,0,0)

    def append_to_log(self, text):
        cursor = self.Cmd.textCursor()
        cursor.movePosition(QTextCursor.End)
        cursor.insertText(text)
        self.Cmd.setTextCursor(cursor)
    def change_currentNum_Label(self,text):
        self.currentNumLabel.setText(text)

if __name__=="__main__":
    QApplication.setHighDpiScaleFactorRoundingPolicy(QtCore.Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)
    QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps)
    QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)

    app = QApplication(sys.argv)
    window = cmdoutput()
    window.show()
    app.exit(app.exec_())