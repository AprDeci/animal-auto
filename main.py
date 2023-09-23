import pyautogui
import cv2
import time
import actions as ac
import ingame

threshold = 0.02
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
action=[ac.keylong_w,ac.keylong_a,ac.keylong_d,ac.keylong_s,ac.press_j,ac.space,ac.press_simulta_aw,ac.press_simulta_dw,ac.press_simulta_sd,ac.press_simulta_sa,ac.press_simulta_spacea]

# 同时长按'a'和'b'键
#时间戳
last_executed_times = {
    'begin_room.png': 0,
    'begin.png': 0,
    'ready.png': 0,
    'endgame.png': 0,
    'expup2.png': 0
}
def execute_condition(condition, last_executed_times, interval):
    if current_time - last_executed_times[condition] >= interval:
        last_executed_times[condition] = current_time
        return True
    else:
        return False
actionready = False
while True:
    print("action状态",actionready)
    current_time = time.time()
    getScreemshot()
    time.sleep(1)
    if execute_condition('ready.png', last_executed_times, 60):
        if ifroutinpress('ready3.png', '准备','space'):
            actionready = True
    if execute_condition('endgame.png', last_executed_times, 10):
        if ifrouutineclick('end.png', '结束游戏'):
            actionready = False
    if execute_condition('begin_room.png', last_executed_times, 20):
        routineclick('begin_room.png','开始游戏')
    if execute_condition('begin.png', last_executed_times, 10):
        routineclick('begin.png','开始游戏')
    if execute_condition('expup2.png', last_executed_times,300):
        routineclick('expup.png', '升级')
    if execute_condition('expup2.png', last_executed_times, 300):
        routineclick('expup2.png', '升级2')
    if actionready: #只在准备后结束前运行
        if To_action: #只在没有检测到目标图片时运行
            ingame.doaction(action)
    To_action = True
    time.sleep(0.3)


