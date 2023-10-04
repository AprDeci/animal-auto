import os.path

from PyQt5.QtWidgets import QWidget
import configparser
from Ui.setup import Ui_setup


class setupWin(QWidget, Ui_setup):
    def __init__(self):
        super().__init__()
        self.conf = configparser.ConfigParser()
        self.conf.read(os.path.abspath('./imgs/config.ini'), encoding='utf-8')
        self.setupUi(self)
        self.LocalOcr.setChecked(True)
        self.OK.clicked.connect(self.setConfig)
        self.freeocrApi.setText(self.conf.get('ocr', 'freeocrapi'))


    def setConfig(self):

        if not self.LocalOcr.isChecked():
            self.conf.set("ocr", "localOcr", "False")
        else:
            self.conf.set("ocr", "localOcr", "True")
        if not self.FreeOcr.isChecked():
            self.conf.set("ocr", "FreeOcr", "False")
        else:
            self.conf.set("ocr", "FreeOcr", "True")
        if self.freeocrApi.text():
            self.conf.set("ocr", "freeocrapi", self.freeocrApi.text())
        else:
            self.conf.set("ocr", "freeocrapi", "")
        with open("./imgs/config.ini", "r+", encoding='utf-8') as configfile:
            self.conf.write(configfile)
