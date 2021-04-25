import pyautogui

pyautogui.FAILSAFE = False

def dragmouse():
    pyautogui.dragTo(0, 1100, button='left')
    pyautogui.click()
    pyautogui.dragTo(30, 975, button='left')
    pyautogui.click()
    pyautogui.moveTo(30, 920, duration=.1)
    pyautogui.click()
    pyautogui.click()

dragmouse()
