import time

import pyautogui

import main

while True:
    current_time = time.time()
    main.getScreemshot()
    time.sleep(0.3)
    main.routinespace('./imgs/ready3.png', '准备')
    main.routineclick('./imgs/begin_room.png', '开始游戏')
    main.routineclick('./imgs/expup.png', '升级')
    main.routineclick('./imgs/expup2.png', '升级2')
    pyautogui.press('w')