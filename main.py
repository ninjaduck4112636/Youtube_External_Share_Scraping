from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
import pyperclip

try:
    driver = webdriver.Chrome("C:/Users/NinjaDuck/Downloads/chromedriver.exe")

    driver.get("https://www.youtube.com/channel/UCqL4rm4nwqhjsOOpFn4Bg7A/videos")
    time.sleep(40)

    ihref = driver.find_element_by_xpath('//a[@id="video-title"]').get_attribute("href")
    time.sleep(5)
    print(ihref)
except Exception as e:
    print(e)
finally:
    driver.close()    
    print("Driver Closed")
