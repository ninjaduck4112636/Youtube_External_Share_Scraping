from selenium import webdriver
import time

try:
    driver = webdriver.Chrome("C:/Users/NinjaDuck/Downloads/chromedriver.exe")

    driver.get("https://www.youtube.com/channel/UCqL4rm4nwqhjsOOpFn4Bg7A/videos")
    time.sleep(40)

    driver.find_element_by_xpath('//img[@class="style-scope yt-img-shadow"]/following::img/following::img/following::img/following::img/following::img/following::img')
except Exception as e:
    print(e)
finally:
    driver.close()    
    print("Driver Closed")
