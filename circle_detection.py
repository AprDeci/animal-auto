import cv2

def isthereCircle(filepath):
    img = cv2.imread(filepath, 0)
    size = 200
    x1 = 0
    y1 = 0
    x2 = x1+size
    y2 = y1+size
    cut = img[y1:y2, x1:x2]
    numpy_img = cv2.adaptiveThreshold(cut, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 9, 13)   # 自动阈值二值化
    circles = cv2.HoughCircles(numpy_img, cv2.HOUGH_GRADIENT , 1 , 90 , param1=100 , param2= 30 , minRadius=30 , maxRadius=60)
    if circles is not None:
        print(f'圆形坐标{circles}')
        return True
    else:
        return False
