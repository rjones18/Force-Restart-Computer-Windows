# Force-Restart-Computer(Windows)
***Note: This only works for computers running Windows 10

This script if ran will force a Windows computer to restart by controlling the mouse movements. This is done by using the `pyautogui` library and the mouse movements are controlled by using x and y coordinates. 
Below is how the final code looks:

```
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
```
