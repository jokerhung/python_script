from random import randrange
from selenium import webdriver
import time
import pyautogui

channel = "https://www.youtube.com/@EmbeddedCoder-2023/videos"
videos = [
    "https://www.youtube.com/watch?v=YFFLzhKRFak&t=133s",
]
webdriver_path = 'D:\\Software\\web\\chromedriver\\chromedriver.exe'
play_interval = 100  # in seconds
interval = 30  # in seconds
def getURL():
    return videos[randrange(len(videos))]

def autoBrowse(play_interval):
    # Set up the webdriver
    driver = webdriver.Firefox()
    #options.headless = False  # Run the browser in headless mode to prevent a window from popping up
    #driver = webdriver.Chrome(executable_path=webdriver_path, options=options)
    #driver = webdriver.Chrome(webdriver_path)
    # Load the web page
    url = getURL()
    driver.get(url)

    pyautogui.click(181, 1168, duration=0.25)

    #fullScreen()
    #skipAd()
    # fast forward after 100 seconds
    time.sleep(play_interval)
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
    autoBrowse(play_interval)
    time.sleep(interval)
