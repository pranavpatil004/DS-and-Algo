import pyautogui as pg
import time

time.sleep(4)

for i in range(20):
    pg.write('Hello World!')
    pg.press('enter')
    time.sleep(1)