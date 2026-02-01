import pyautogui
import time

pyautogui.FAILSAFE = True

time.sleep(1)

pyautogui.press('winleft')
pyautogui.write('power bi')
pyautogui.press('enter')

time.sleep(2)

