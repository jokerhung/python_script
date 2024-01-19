from random import randrange
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

import time
import pyautogui

channel = "https://www.youtube.com/@EmbeddedCoder-2023/videos"
videos = [
    "https://www.youtube.com/watch?v=YFFLzhKRFak&t=133s",
]
webdriver_path = 'D:\hungnm\chromedriver_win32\chromedriver.exe'

play_duration = 1800  # in seconds
play_interval = 900  # in seconds

def getURL():
    return videos[randrange(len(videos))]

def autoBrowse(play_duration):
    # Set up the webdriver
    driver = webdriver.Firefox()
    driver.maximize_window()
    time.sleep(5)
    
    #s = Service(webdriver_path)
    #driver = webdriver.Chrome(service=s)
    #driver.fullscreen_window()
    
    # Load the web page
    url = getURL()
    driver.get(url)

    pyautogui.click(181, 1168, duration=0.25)

    #fullScreen()
    #skipAd()
    # fast forward after 100 seconds
    time.sleep(play_duration)
    #forwardVideo()

    #time.sleep(interval)
    # Close the webdriver
    driver.quit()


def skipAd():
    # click to forward
    pyautogui.click(1, 0, duration=0.25)


def forwardVideo():
    # click to move mouse from skipAds position to forward slider
    pyautogui.moveRel(1, 0, duration=0.25)
    # click to forward
    pyautogui.click(1, 0, duration=0.25)
    # move mouse position back to skipAds position
    pyautogui.moveRel(-1, 0, duration=0.25)


def fullScreen():
    # double click to full screen
    pyautogui.doubleClick(1000, 1000, duration=0.25)

while True:
    autoBrowse(play_duration)
    time.sleep(play_interval)
