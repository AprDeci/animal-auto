import random

import pyautogui
import time

# 模拟按下和释放多个按键的函数
def press_simulta_keys(keys):
    for key in keys:
        pyautogui.keyDown(key)
    time.sleep(random.randint(1,3))
    for key in keys:
        pyautogui.keyUp(key)

# 定义一些游戏操作函数
keys=[
    ['a','w'],
    ['d','s'],
    ['j','space'],
    ['a','s'],
    ['d','a'],
    ['space','a'],
    ['d','w'],
    ['d','space'],
    ['w','space'],
    ['s','space'],
    ['j','w','a'],
    ['j','s','a'],
    ['j','d','a'],
    ['j','d','w'],
    ['j','space','a'],
    ['j','space','w'],
    ['j','space','s'],
    ['j','space','d'],
    ['w','shift'],
    ['s','shift'],
    ['a','shift'],
    ['d','shift'],
    ['w','a','shift'],
    ['w','d','shift'],
    ['s','a','shift'],
    ['s','d','shift'],
]

def action(game_number):
    for i in range(3,5):
        nextkeys = random.choice(keys)
        print(f"第{game_number}局:".join(nextkeys))
        press_simulta_keys(nextkeys)
