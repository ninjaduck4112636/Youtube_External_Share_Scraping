from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
import pyperclip

try:
    driver = webdriver.Chrome("C:/Users/NinjaDuck/Downloads/chromedriver.exe")

    driver.get("https://www.youtube.com/channel/UCqL4rm4nwqhjsOOpFn4Bg7A/videos")
    time.sleep(40)

    counter = 1;
    istring = '//a[@id="video-title"]'
    x_path_details = driver.find_element_by_xpath(istring)
    
    while True:
        if(counter==1):
            ihref = x_path_details.get_attribute("href")
        else:
            istring += '/following::a/following::a'
            ihref = driver.find_element_by_xpath(istring).get_attribute("href")
        time.sleep(5)
        print(ihref)
        counter += 1
        
except Exception as e:
    print(e)
finally:
    driver.close()    
    print("Driver Closed")
