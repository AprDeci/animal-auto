import os
import sys
import time
import configparser as ini
import cv2
import mss
import numpy as np
import pyautogui
from PyQt5.QtCore import QThread, pyqtSignal
import doacntion
import freeocr
import paddleOcr
from Ui.controWin import Ui_mainWindow
from PyQt5.QtWidgets import QWidget, QMainWindow
from qfluentwidgets import FluentIcon as FIF

from circle_detection import isthereCircle
from PickExpnumber import getExpimg
import pygetwindow as gw


THRESHOLD=0.02


class WorkerThread(QThread):
    send_signal = pyqtSignal(str)
    QcurrentNum_signal = pyqtSignal(str)
    Qgetexp_signal = pyqtSignal(str)
    def __init__(self, operation_func, *args, **kwargs):
        super().__init__()
        self.operation_func = operation_func
        self.args = args
        self.kwargs = kwargs
        self.ingame = False
        self.to_action = True
        self.last_executed_times = {
            'begin_room.png': 0,
            'begin.png': 0,
            'ready.png': 0,
            'endgame.png': 0,
            'expup2.png': 0,
            'quickgame.png': 0,
            'cemera.png': 0,
            'gamenum':0,
            'longtimeO.png':0,
            'whengame.png':0,
        'openrewards.png':0
        }
        self.action_ready = False
        self.current_gameNum = 0
        conf = ini.ConfigParser()
        conf.read("./imgs/config.ini",encoding='utf-8')
        self.localOcr = conf.get("ocr", "localocr")
        self.FreeOcr = conf.get("ocr", "freeocr")
        self.FreeOcr_api = conf.get("ocr", "freeocrapi")
    def run(self):
        if self.operation_func=="quickgame":
            self.quickgame(*self.args, **self.kwargs)
        elif self.operation_func=="roomgame":
            self.roomgame(*self.args, **self.kwargs)
    def stop(self):
        self.terminate()
        self.finished.emit()

    def get_screenshot(self,region=None):
        if region==None:
            pyautogui.screenshot().save("./imgs/screenshot.png")
        else:
            pyautogui.screenshot(region=region).save("./imgs/exp.png")

    def get_xy(self, img_path):
        img = cv2.imread("./imgs/screenshot.png")
        img_aim = cv2.imread(img_path)
        height, width, channel = img_aim.shape
        result = cv2.matchTemplate(img, img_aim, cv2.TM_SQDIFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
        if min_val < THRESHOLD:
            upper_left = min_loc
            # 计算出匹配区域右下角图标（左上角坐标加上模板的长宽即可得到）
            lower_right = (upper_left[0] + width, upper_left[1] + height)
            # 计算坐标的平均值并将其返回
            avg = (int((upper_left[0] + lower_right[0]) / 2), int((upper_left[1] + lower_right[1]) / 2))
        else:  # 左上角坐标
            avg = None
        return avg

    def auto_click(self, coords):
        pyautogui.click(coords[0], coords[1], button='left')
        time.sleep(1)

    def routine_click(self, img_path, name):
        avg = self.get_xy(img_path)
        if avg == None:
            pass
        else:
            print(f"正在点击{name},{avg}")
            self.send_signal.emit(f"正在点击{name},{avg}\n")
            self.auto_click(avg)
            self.to_action = False

    def ifrouutineclick(self, img_path, name):
        avg = self.get_xy(img_path)
        if avg == None:
            return False
        else:
            print(f"正在点击{name},{avg}")
            self.send_signal.emit(f"正在点击{name},{avg}\n")
            time.sleep(0.5)
            pyautogui.click(avg)
            self.to_action = False
            return True

    def ifthereimg(self, img_path, name):
        avg = self.get_xy(img_path)
        if avg == None:
            return False,avg
        else:
            print(f"{name},{avg}")
            self.send_signal.emit(f"{name},{avg}\n")
            return True,avg

    def routinespace(self, img_path, name):
        avg = self.get_xy(img_path)
        if avg == None:
            pass
        else:
            print(f"正在点击{name},{avg}")
            self.send_signal.emit(f"正在点击{name},{avg}\n")
            time.sleep(0.5)
            pyautogui.press('space')
            self.to_action = False

    def ifroutinpress(self, img_path, name, key):
        avg = self.get_xy(img_path)
        if avg == None:
            return False
        else:
            print(f"正在点击{name},{avg}")
            self.send_signal.emit(f"正在点击{name},{avg}\n")
            time.sleep(0.5)
            pyautogui.press(key)
            self.to_action = False
            return True

    def Ocr(self, img_path):
        if self.localOcr=='True':
            return paddleOcr.getexp(img_path)
        else:
            if self.FreeOcr_api==None:
                return freeocr.getexp(img_path)
            else:
                return freeocr.getexp(img_path,self.FreeOcr_api)

    def execute_condition(self, current_time, condition, interval):
        if current_time - self.last_executed_times[condition] >= interval:
            self.last_executed_times[condition] = current_time
            return True
        else:
            return False

    def quickgame(self, limit_number, shutdown, game_number):
        while True:
            current_time = time.time()
            self.get_screenshot()
            time.sleep(0.3)
            if not self.ingame:#游戏状态外
                if self.execute_condition(current_time, 'ready.png', 30):
                    if self.ifroutinpress('./imgs/ready3.png', '准备', 'space'):
                        time.sleep(20)
                        self.action_ready = True
                        self.ingame = True
                if self.execute_condition(current_time, 'endgame.png', 5):
                    avg=self.ifthereimg('./imgs/end.png', '结束游戏')[1]
                    if avg is not None:
                        getExpimg('quickgame')
                        pyautogui.leftClick(avg[0],avg[1])
                        self.action_ready = False
                        if (limit_number):
                            if (self.current_gameNum == game_number):
                                self.exit(shutdown)
                            break
                        getexp=self.Ocr("./imgs/exp.png")
                        if getexp == 'error' or getexp =='Network error':
                            self.send_signal.emit(f"没有读取到数字或网络请求失败了\n")
                            continue
                        else:
                            self.send_signal.emit(f"获取经验: {getexp}\n")
                            self.Qgetexp_signal.emit(getexp)
                if self.execute_condition(current_time, 'begin.png', 5):
                    if self.ifrouutineclick('./imgs/begin.png', '开始游戏'):
                        self.current_gameNum += 1
                        self.QcurrentNum_signal.emit(f"🎮当前进行第{self.current_gameNum}局")
                if self.execute_condition(current_time, 'expup2.png', 50):
                    self.routine_click('./imgs/expup.png', '升级')
                if self.execute_condition(current_time, 'expup2.png', 50):
                    self.routine_click('./imgs/expup2.png', '升级2')
                if self.execute_condition(current_time, 'openrewards.png', 50):
                    self.ifrouutineclick('./imgs/openrewards.png', '领取奖励')
                if self.execute_condition(current_time, 'quickgame.png', 50):
                    self.routine_click('./imgs/quickgame.png', '快速游戏')
                if self.execute_condition(current_time, 'longtimeO.png', 50):
                    self.routine_click('./imgs/longtimeO.png', '长时间不操作')
            else:
                if self.execute_condition(current_time,'whengame.png',50):
                    if isthereCircle('./imgs/screenshot.png'):#检测头像
                        self.action_ready=True
                if self.execute_condition(current_time, 'cemera.png', 5):
                    if self.ifthereimg('./imgs/cemera.png', '暂停行动')[0]:
                        self.action_ready = False
                        self.ingame=False
                if self.action_ready:  # 只在准备后结束前运行
                    if self.to_action:  # 只在没有检测到目标图片时运行
                        doacntion.action(self.current_gameNum)
                self.to_action = True
                time.sleep(0.3)

    def exit(self, shutdown):
        time.sleep(2)
        while True:
            self.get_screenshot()
            time.sleep(0.8)
            self.routine_click('./imgs/return.png', '返回主界面')
            self.routine_click('./imgs/exit.png', '退出游戏')
            time.sleep(3)
            if self.ifrouutineclick('./imgs/exitis.png', '是'):
                if shutdown:
                    os.system("shutdown -s -t  30 ")
                sys.exit()  # 退出程序

    def roomgame(self, shutdown):
        while True:
            current_time = time.time()
            self.get_screenshot()
            time.sleep(0.3)
            pyautogui.press('w')
            self.routinespace('./imgs/ready3.png', '准备')
            if self.ifrouutineclick('./imgs/begin_room.png', '开始游戏'):
                self.current_gameNum += 1
                self.QcurrentNum_signal.emit(f"🎮当前进行第{self.current_gameNum}局")
            self.routine_click('./imgs/expup.png', '升级')
            self.routine_click('./imgs/expup2.png', '升级2')
            if self.execute_condition(current_time, 'openrewards.png', 50):
                self.routine_click('./imgs/openrewards.png', '领取奖励')
            if self.ifthereimg('./imgs/xiangce.png', '结算')[0]:
                getExpimg('room')
                time.sleep(0.3)
                getexp=self.Ocr("./imgs/exp.png")
                if getexp == 'error':
                    continue
                elif getexp == '0':
                    if(shutdown):
                        os.system("shutdown -s -t  30 ")
                    sys.exit()
                else:
                    self.send_signal.emit(f"获取经验: {getexp}\n")
                    self.Qgetexp_signal.emit(getexp)
                    time.sleep(8)
class controlWin_inter(QMainWindow,Ui_mainWindow):
    print_signal = pyqtSignal(str)
    switch_signal = pyqtSignal()
    currentNum_signal=pyqtSignal(str)
    currentExp_signal=pyqtSignal(str)
    def __init__(self,parent=None):
        super().__init__(parent=parent)
        self.setupUi(self)
        self.setContentsMargins(0, 40, 0, 0)
        self.Githublink.setIcon(FIF.GITHUB)
        self.BlogLink.setIcon(FIF.LINK)
        self.operation_thread=None
        self.ifshutdown.clicked.connect(lambda: self.ifNumber.setChecked(True))




    def getinfo(self):
        self.shutdown = self.ifshutdown.isChecked()
        self.limitNumber = self.ifNumber.isChecked()
        self.gameNumber = self.gameNumberInput.value()

    def start_operation_thread(self, operation_func, *args, **kwargs):
        if not self.operation_thread or not self.operation_thread.isRunning():
            self.operation_thread = WorkerThread(operation_func, *args, **kwargs)
            self.operation_thread.send_signal.connect(self.sendmessage)
            self.operation_thread.QcurrentNum_signal.connect(self.currentNumLabel_change)
            self.operation_thread.Qgetexp_signal.connect(self.currentExpLabel_change)
            self.operation_thread.start()
            match operation_func:
                case "roomgame":
                    self.roombuttom.setText("停止脚本")
                    self.quickgamebutton.setEnabled(False)
                    self.switch_signal.emit()
                case "quickgame":
                    self.quickgamebutton.setText("停止脚本")
                    self.roombuttom.setEnabled(False)
                    self.switch_signal.emit()
        else:
            self.operation_thread.stop()
            match operation_func:
                case "roomgame":
                    self.roombuttom.setText("自建房间")
                    self.quickgamebutton.setEnabled(True)
                case "quickgame":
                    self.quickgamebutton.setText("快速游戏")
                    self.roombuttom.setEnabled(True)


    def on_operation_finished(self):
        pass

    def beginquick(self):
        self.getinfo()
        self.start_operation_thread("quickgame",self.limitNumber, self.shutdown, self.gameNumber)

    def beginroom(self):
        self.getinfo()
        self.start_operation_thread("roomgame",self.shutdown)

    def sendmessage(self,str):
        self.print_signal.emit(str)
        
    def currentNumLabel_change(self,str):
        self.currentNum_signal.emit(str)
    def currentExpLabel_change(self,str):
        self.currentExp_signal.emit(str)



