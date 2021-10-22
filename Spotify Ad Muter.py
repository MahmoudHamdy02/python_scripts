import time
from SwSpotify import spotify
import pyautogui
ad = False
while not ad:
    try:
        if spotify.song() == "Advertisement":
            ad = True
            pyautogui.press("volumemute")
        while ad:
            if spotify.song() != "Advertisement":
                pyautogui.press("volumemute")
                ad = False
        time.sleep(2)
    except:
        pass
