import time
import pyautogui
def keylong_a():
    print('a')
    pyautogui.keyDown('a')
    time.sleep(1)
    pyautogui.keyUp('a')
def keylong_w():
    print('w')
    pyautogui.keyDown('w')
    time.sleep(1)
    pyautogui.keyUp('w')
def keylong_s():
    print('s')
    pyautogui.keyDown('s')
    time.sleep(1)
    pyautogui.keyUp('s')
def keylong_d():
    print('d')
    pyautogui.keyDown('d')
    time.sleep(1)
    pyautogui.keyUp('d')
def press_j():
    print('j')
    for i in range(8,14):
        pyautogui.press('j')
        time.sleep(0.1)
def space():
    print('space')
    pyautogui.press('space')

def press_simulta_aw():
    pyautogui.keyDown('a')
    pyautogui.keyDown('w')
    time.sleep(1)
    pyautogui.keyUp('w')
    pyautogui.keyUp('a')
def press_simulta_dw():
    pyautogui.keyDown('d')
    pyautogui.keyDown('w')
    time.sleep(1)
    pyautogui.keyUp('w')
    pyautogui.keyUp('d')
def press_simulta_sd():
    pyautogui.keyDown('s')
    pyautogui.keyDown('d')
    time.sleep(1)
    pyautogui.keyUp('d')
    pyautogui.keyUp('s')
def press_simulta_sa():
    pyautogui.keyDown('s')
    pyautogui.keyDown('a')
    time.sleep(1)
    pyautogui.keyUp('d')
    pyautogui.keyUp('a')
def press_simulta_spacea():
    pyautogui.keyDown('space')
    pyautogui.keyDown('a')
    time.sleep(1)
    pyautogui.keyUp('space')
    pyautogui.keyUp('a')
def press_simulta_spaceaw():
    pyautogui.keyDown('space')
    pyautogui.keyDown('a')
    pyautogui.keyDown('w')
    time.sleep(1)
    pyautogui.keyUp('space')
    pyautogui.keyUp('a')
    pyautogui.keyUp('w')
# 同时长按'a'和'b'键
