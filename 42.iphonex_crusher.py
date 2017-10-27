import time

from selenium import webdriver
import winsound

browser = webdriver.Chrome()
while True:
    browser.get("https://www.apple.com/us/shop/goto/buy_iphone/iphone_x")
    try:
        found = browser.find_element_by_xpath('/html/body/div[3]/div/img')
        if not found:
            print("good!")
            frequency = 2500  # Set Frequency To 2500 Hertz
            duration = 1000  # Set Duration To 1000 ms == 1 second
            winsound.Beep(frequency, duration)
            break
    except BaseException as e:
        print(str(e))
browser.quit()
