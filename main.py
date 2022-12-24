import cv2
import time
import keyboard
from myfunctions import*

time.sleep(5)
while keyboard.is_pressed('q') == False:
   img = pyautogui.screenshot()
   img = np.array(img)
   gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
   gray_blurred = cv2.blur(gray, (4, 4))
   circles = cv2.HoughCircles(gray_blurred, cv2.HOUGH_GRADIENT, 1, 10, param1 = 50,
                  param2 = 30, minRadius =25, maxRadius = 35)
   if circles is not None:
      circles = np.round(circles[0, :]).astype("int")
      mn = 99999
      for (x, y, r) in circles:
          d = dis(x, y)
          if d<mn:
              cx=x
              cy=y
              cr=r
              mn = d
      mouse_click(cx, cy)
