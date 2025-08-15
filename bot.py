# open_chrome_type_url.py
import time
import pyautogui as pg

URL = "aakash"
LAUNCH_WAIT = 2.5   # adjust if Chrome opens slowly
TYPE_DELAY = 0.25   # keypress delay for visible typing

# Safety: moving mouse to a screen corner aborts the script
pg.FAILSAFE = True
pg.PAUSE = 0.15

def open_chrome_and_type(url: str):
    # 1) Open Start menu, type "chrome", press Enter
    pg.press('win')
    time.sleep(0.4)
    pg.typewrite('chrome', interval=TYPE_DELAY)
    pg.press('enter')

    # 2) Wait for Chrome to appear
    time.sleep(LAUNCH_WAIT)

    # 3) Focus the address bar (Ctrl+L), then type URL and go
    pg.hotkey('ctrl', 'l')
    time.sleep(0.2)
    pg.typewrite(url, interval=TYPE_DELAY)
    pg.press('enter')

    # 4) Optional: move mouse a bit so it looks “alive”
    w, h = pg.size()
    pg.moveTo(w//2, h//2, duration=0.4)
    pg.moveRel(0, 60, duration=0.25)

if __name__ == "__main__":
    open_chrome_and_type(URL)

