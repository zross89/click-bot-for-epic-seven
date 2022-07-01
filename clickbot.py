
import pyautogui
import time

time.sleep(10)

stop = pyautogui.rightClick
while stop != True:

    bookmark_button = pyautogui.locateOnScreen('Bookmark.png', confidence=0.9) #bookmark search
    mystic_button = pyautogui.locateOnScreen('Mystic.png', confidence=0.9) #mystic search
    loop_count = 0

    while loop_count < 2:
        if bookmark_button == True:
            pyautogui.moveTo(bookmark_button)
            pyautogui.leftClick(bookmark_button)
            time.sleep(2)
            buy_button = pyautogui.locateOnScreen('Buycov.png', confidence=0.9)
            pyautogui.moveTo(buy_button)
            pyautogui.leftClick(buy_button)

    
        if mystic_button == True:   
            pyautogui.moveTo(mystic_button)
            pyautogui.leftClick(mystic_button)
            time.sleep(2)
            buy_mbutton = pyautogui.locateOnScreen('Buycov.png', confidence=0.9)
            pyautogui.moveTo(buy_mbutton)
            pyautogui.leftClick(buy_mbutton)

        pyautogui.scroll(-5)
        loop_count = loop_count + 1

    time.sleep(5)
    refresh_button = pyautogui.locateOnScreen('Refresh.png', confidence=0.9) #refesh shop
    pyautogui.moveTo(refresh_button)
    time.sleep(2)
    pyautogui.leftClick(refresh_button) 

    time.sleep(2)
    confirm_button = pyautogui.locateOnScreen('Confirm.png', confidence=0.9)
    pyautogui.moveTo(confirm_button)
    time.sleep(2)
    pyautogui.leftClick(confirm_button)
    







