import pyautogui
import time

def open_spotify_app():
    pyautogui.press('volumeup')
    pyautogui.hotkey('command', 'space')
    pyautogui.write('Spotify')
    pyautogui.press('enter')

def open_local_files_playlist():
    local_files_point = [140, 320]
    pyautogui.moveTo(local_files_point[0], local_files_point[1])
    pyautogui.click()
    pyautogui.click()

def scroll_to_bottom():
    middle_of_screen = [617, 633]
    pyautogui.moveTo(middle_of_screen[0], middle_of_screen[1])
    time.sleep(2)
    pyautogui.scroll(-500)
    
def like_song():
    newest_file_like_button = [1549, 889]
    pyautogui.moveTo(newest_file_like_button[0],newest_file_like_button[1])
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