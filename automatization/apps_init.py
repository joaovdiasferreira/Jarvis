import pyautogui
import time


def chrome_init():
    pyautogui.hotkey("Win")
    pyautogui.write("chrome")
    pyautogui.press("enter")
    time.sleep(2)
    pyautogui.click(x=852, y=598)
    time.sleep(1)

def lenovo_vantage_init():
    pyautogui.hotkey("win")
    pyautogui.write("lenovo vantage")
    pyautogui.press("enter")
    time.sleep(2)
    pyautogui.click(x=48, y=249)
    time.sleep(1)

#For app that doesn't need specific startups
def app_init(app):
    pyautogui.hotkey("Win")
    pyautogui.write(app)
    pyautogui.press("enter")
