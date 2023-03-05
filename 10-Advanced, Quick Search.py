from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from tkinter import *


# Add the path to your chromedriver executable file
path = "chromedriverPath"

root = Tk()

inp = Label(root, text="Enter what you want to search for...")
inp.pack()

e = Entry(root, width=50)
e.pack()

def re_direct_search():
    driver = webdriver.Chrome(path)
    driver.get("https://www.youtube.com/")
    driver.maximize_window()
    search1 = driver.find_element_by_xpath("/html/body/ytd-app/div[1]/div/ytd-masthead/div[4]/div[2]/ytd-searchbox/form/div[1]/div[1]/input")
    search1.send_keys(e.get())
    time.sleep(5)
    search_button = driver.find_element_by_id("search-icon-legacy")
    search_button.click()
    time.sleep(3)

    driver.execute_script("window.open('');")
    driver.switch_to.window(driver.window_handles[1])
    driver.get("https://www.google.com.eg/")
    search = driver.find_element_by_name("q")
    search.send_keys(e.get())
    search.send_keys(Keys.RETURN)
    time.sleep(3)

    driver.execute_script("window.open('');")
    driver.switch_to.window(driver.window_handles[2])
    driver.get("https://www.bing.com/")
    search = driver.find_element_by_name("q")
    search.send_keys(e.get())
    search.send_keys(Keys.RETURN)
    time.sleep(3)


action = Button(root, text="SEARCH", command=re_direct_search)
action.pack()


root.mainloop()
