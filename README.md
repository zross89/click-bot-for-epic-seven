# Epic Seven Auto-Click Bot

## Description

This is a Python script that automates certain actions in the mobile game Epic Seven using the pyautogui library. Specifically, the bot will search for and click the 'Bookmark' and 'Mystic' buttons on the game screen, wait for 2 seconds, and then search for and click the 'Buy' button if found. It will then scroll down the screen and repeat these actions once more. 

The bot will also refresh the game screen by clicking the 'Refresh' button and then confirm the refresh by clicking the 'Confirm' button.

## Prerequisites

To run this code, you will need the following:

- Python 3 installed on your computer
- The PyAutoGUI library installed in Python
- The following image files in the same directory as your Python script: 
	- Bookmark.png
	- Mystic.png
	- Buycov.png
	- Refresh.png
	- Confirm.png
*NOTE* take the screenshots of the buttons at your full screen resolution, include the price of the bookmarks as this is what pyautogui will pick up on to differ between mystics anad covonants.

## Installation and Usage

1. Clone or download the code from this repository to your local machine.
2. Install Python 3 and PyAutoGUI library, if you haven't already.
3. Place the image files in the same directory as the Python script.
4. Open a command prompt or terminal window and navigate to the directory where the script is saved.
5. Run the script and move the mouse cursor over the game window
6. Wait for the 10-second delay before the bot starts running. During this time, make sure the game is open and in the correct location on your screen.
7. The bot will run in a loop until you manually exit the program by right-clicking.

## Notes
- The game will sometimes not register a click on the button even though the visualization shows a click. Could be the emulator but sometimes happens on mobile too.
- The bot may not work as expected if the game window is not in the correct location on your screen, or if the game is in a different language or version than expected.
- The bot is designed to run in a specific way and may not work as intended if you modify the code.
- Use this script at your own risk. The author is not responsible for any consequences that may result from using this code.
