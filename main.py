import os
import pyautogui
import cv2
import time
import doacntion
import sys
threshold = 0.01
imgs = ['begin_room.png','ready.png']
To_action = True

def getScreemshot():
    pyautogui.screenshot().save("./imgs/screenshot.png")
def getxy(img_path):
    img = cv2.imread("./imgs/screenshot.png")
    img_aim = cv2.imread(img_path)
    height,width,channel = img_aim.shape
    result = cv2.matchTemplate(img,img_aim,cv2.TM_SQDIFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    if min_val <threshold:
        upper_left = min_loc
        # 计算出匹配区域右下角图标（左上角坐标加上模板的长宽即可得到）
        lower_right = (upper_left[0] + width, upper_left[1] + height)
        # 计算坐标的平均值并将其返回
        avg = (int((upper_left[0] + lower_right[0]) / 2), int((upper_left[1] + lower_right[1]) / 2))
    else:#左上角坐标
        avg = None
    return avg

def auto_Click(var_avg):
    pyautogui.click(var_avg[0], var_avg[1], button='left')
    time.sleep(1)

def routineclick(img_path,name):
    avg = getxy(img_path)
    if avg == None:
        pass
    else:
        print(f"正在点击{name},{avg}")
        auto_Click(avg)
        global To_action
        To_action = False

def ifrouutineclick(img_path,name):
    avg = getxy(img_path)
    if avg == None:
        return False
    else:
        print(f"正在点击{name},{avg}")
        time.sleep(0.5)
        pyautogui.click(avg)
        global To_action
        To_action = False
        return True
def ifthereimg(img_path,name):
    avg = getxy(img_path)
    if avg == None:
        return False
    else:
        print(f"{name},{avg}")
        return True
def routinespace(img_path,name):
    avg = getxy(img_path)
    if avg == None:
        pass
    else:
        print(f"正在点击{name},{avg}")
        time.sleep(0.5)
        pyautogui.press('space')
        global To_action
        To_action = False
def ifroutinpress(img_path,name,key):
    avg = getxy(img_path)
    if avg == None:
        return False
    else:
        print(f"正在点击{name},{avg}")
        time.sleep(0.5)
        pyautogui.press(key)
        global To_action
        To_action = False
        return True
#时间戳
last_executed_times = {
    'begin_room.png': 0,
    'begin.png': 0,
    'ready.png': 0,
    'endgame.png': 0,
    'expup2.png': 0,
    'quickgame.png': 0,
    'cemera.png':0
}
def execute_condition(current_time,condition, last_executed_times, interval):
    if current_time - last_executed_times[condition] >= interval:
        last_executed_times[condition] = current_time
        return True
    else:
        return False
actionready = False
game_number = 0
time_exit=False
isshutdown = False

def exit(shutdown):
    time.sleep(2)
    while True:
        getScreemshot()
        time.sleep(0.8)
        routineclick('./imgs/return.png','返回主界面')
        routineclick('./imgs/exit.png','退出游戏')
        time.sleep(3)
        if ifrouutineclick('./imgs/exitis.png','是'):
            if shutdown:
                os.system("shutdown -s -t  30 ")
            sys.exit()#退出程序

def main(limitNumber,shutdown,gameNumber):
    global game_number, actionready, To_action
    while True:
        current_time = time.time()
        getScreemshot()
        time.sleep(0.3)
        if execute_condition(current_time,'ready.png', last_executed_times, 30):
            if ifroutinpress('./imgs/ready3.png', '准备', 'space'):
                time.sleep(20)
                actionready = True
        if execute_condition(current_time,'cemera.png', last_executed_times, 5):
            if ifthereimg('./imgs/cemera.png', '暂停行动'):
                actionready = False
        if execute_condition(current_time, 'endgame.png', last_executed_times, 5):
            if ifrouutineclick('./imgs/end.png', '结束游戏'):
                actionready = False
                if (limitNumber):
                    if (game_number == gameNumber):
                        exit(shutdown)
        if execute_condition(current_time,'begin.png', last_executed_times, 5):
           if ifrouutineclick('./imgs/begin.png', '开始游戏'):
                game_number = game_number + 1
        if execute_condition(current_time,'expup2.png', last_executed_times, 50):
            routineclick('./imgs/expup.png', '升级')
        if execute_condition(current_time,'expup2.png', last_executed_times, 50):
            routineclick('./imgs/expup2.png', '升级2')
        if execute_condition(current_time,'quickgame.png', last_executed_times, 50):
            routineclick('./imgs/quickgame.png', '快速游戏')
        if actionready:  # 只在准备后结束前运行
            if To_action:  # 只在没有检测到目标图片时运行
                doacntion.action(game_number)
        To_action = True
        time.sleep(0.3)
if __name__ == '__main__':
    main(False,False,1)
    # exit(False)