import time
import mss
import cv2
import numpy as np
import pygetwindow as gw
from PIL import ImageGrab

getpic = mss.mss()
tolerancex,tolerancey = 20,20
explocation = {
    "room": (1500, 400, 300, 200),
    "quickgame": (1500, 200, 300, 200),
}

def getWindowPic():
    start = time.time()
    window = gw.getWindowsWithTitle('猛兽派对')[0]
    left, top, width, height = window.left, window.top, window.width, window.height
    screenshot =ImageGrab.grab((left, top, left+width, top+height))
    image = np.array(screenshot)
    image = cv2.cvtColor(image, cv2.COLOR_RGBA2BGR)
    cv2.imwrite("./imgs/exp_r.png", image)
    end = time.time()
    print(end - start)



def getAllExp(bounding_rects):
    try:
        sorted_arr = bounding_rects[bounding_rects[:, 1].argsort()]
        return sorted_arr[0]
    except:
        print('没有数字')
        return None

# 加载图像
def getExpimg(model):
    getWindowPic()
    time.sleep(0.3)
    image_path = cv2.imread('./imgs/exp_r.png')
    if model == 'room':
        region_x, region_y, region_w, region_h = explocation["room"]
    else:
        region_x, region_y, region_w, region_h = explocation["quickgame"]
    image = image_path[region_y:region_y+region_h, region_x:region_x+region_w]
    lower_color = np.array([42,180,140])
    upper_color = np.array([45, 200, 150])
    mask = cv2.inRange(image, lower_color, upper_color)
    # 形态学操作
    kernel = np.ones((10, 10), np.uint8)
    mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
    # 查找轮廓
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE,)
    # 处理每个轮廓
    bounding_rects = []
    for contour in contours:
        x, y, w, h = cv2.boundingRect(contour)
        bounding_rects.append([x+region_x,y+region_y,w,h])
    bounding_rects = np.array(bounding_rects)
    print(bounding_rects)
    result = getAllExp(bounding_rects)
    if result is None:
        return
    rectangle_x,rectangle_y,rectangle_w,rectangle_h = result[0]-tolerancex,result[1]-tolerancey,result[2]+tolerancex+10,result[3]+tolerancey+10
    exp_pic = image_path[rectangle_y:rectangle_y+rectangle_h,rectangle_x:rectangle_x+rectangle_w]
    cv2.imwrite('./imgs/exp.png',exp_pic)
