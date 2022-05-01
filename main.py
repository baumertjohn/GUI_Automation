# 100 Days of Code
# GUI Automation - Autoplay Google's T-Rex Game

import time

import pyautogui
from selenium import webdriver

WEBPAGE = "https://elgoog.im/t-rex/"
CHROMEDRIVER = "D:/Python_Code/chromedriver.exe"
driver = webdriver.Chrome(executable_path=CHROMEDRIVER)

driver.get(WEBPAGE)
current_time = time.time()
loop_stop = current_time + 60
DETECT_DISTANCE = 75


def run_game():
    try:
        trex_x, trex_y = pyautogui.locateCenterOnScreen("./images/t-rex.png")
    except TypeError:
        pyautogui.alert(
            text="Game Error - Restart App", title="GAME ERROR", button="OK"
        )
        driver.quit()
    obstacle_x, obstacle_y = trex_x + DETECT_DISTANCE, trex_y + 15
    gameover_x, gameover_y = trex_x + 255, trex_y - 5
    pyautogui.alert(
        text="Ready to autoplay for 60 seconds.", title="Game Start", button="OK"
    )
    pyautogui.press("up")
    while time.time() < loop_stop:
        if pyautogui.pixelMatchesColor(
            obstacle_x, obstacle_y, (83, 83, 83), tolerance=5
        ):  # Jump for obstacle
            pyautogui.press("up")
            time.sleep(0.2)  # Jumping over cacti
        elif pyautogui.pixelMatchesColor(
            gameover_x, gameover_y, (83, 83, 83), tolerance=5
        ):  # Reset game
            pyautogui.press("up")
    pyautogui.alert(text="I'm Done!!", title="Game Over", button="OK")
    driver.quit()


if __name__ == "__main__":
    run_game()
