import pyautogui
import time


# majority of code stolen from
# https://github.com/BigchillRK/Zoom-Meeting-and-Recording/blob/master/zoom_record_template1.py

def join_zoom(meet_id: str, password: str = None):
    pyautogui.press('esc', interval=0.1)

    time.sleep(0.2)

    # these lines are simulating starting up zoom by pressing windows key and typing zoom to open program
    pyautogui.press('win', interval=0.1)
    pyautogui.write('zoom')
    pyautogui.press('enter', interval=.1)
    # wait for the window

    # time delay to factor for zoom app to load up, good buffer is like 10 sec but its case specific
    time.sleep(.5)

    # this part simulates clicking join meeting, entering meeting id and pressing enter to join
    ##Make sure the joinButton.png file is located in the same folder as the python file or else it will not work
    ##this tells the script where to click to join the meeting

    x, y = pyautogui.locateCenterOnScreen('joinButton.png')
    pyautogui.click(x, y)
    pyautogui.press('enter', interval=.1)
    ## the interval of 1 second is important, if not there, then the meeting id will not be inputted
    pyautogui.write(meet_id)
    pyautogui.press('enter', interval=.1)

    if password:
        time.sleep(.1)
        pyautogui.press('enter', interval=.1)
        pyautogui.write(password)
        pyautogui.press('enter', interval=.1)

    input()


join_zoom('123456', '796')
