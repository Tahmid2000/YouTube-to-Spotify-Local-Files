import pyautogui
import time

def position_finder():
    try:
        while True:
            x, y = pyautogui.position()
            print(f"\rThe current mouse position is {x}, {y}", end="")
            time.sleep(0.2)  # Adjust the sleep time as needed
    except KeyboardInterrupt:
        print("\nDone.")

def open_spotify_app():
    pyautogui.press('volumeup')
    pyautogui.hotkey('command', 'space')
    pyautogui.write('Spotify')
    pyautogui.press('enter')

def open_local_files_playlist():
    pyautogui.moveTo(140, 320)
    pyautogui.click()
    pyautogui.click()

def scroll_to_bottom():
    pyautogui.moveTo(617,633)
    time.sleep(2)
    pyautogui.scroll(-500)
    
def like_song():
    pyautogui.moveTo(1549,889)
    time.sleep(2)
    pyautogui.click()

def close_spotify(): 
    time.sleep(2)
    pyautogui.hotkey('command', 'q')

def main():
    open_spotify_app()
    open_local_files_playlist()
    scroll_to_bottom()
    like_song()
    close_spotify()
    time.sleep(2)
    open_spotify_app()