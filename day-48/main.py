from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach" ,True)

driver = webdriver.Chrome(options=chrome_options)

driver.get("http://orteil.dashnet.org/cookieclicker/")
products = ["product0","product1","product2","product3","product4","product5","product6","product7","product8","product9","product10"]

time.sleep(5)
lang_select = driver.find_element(By.ID, value="langSelect-EN")
cookie = driver.find_element(By.ID, value="bigCookie")
time.sleep(2)
lang_select.click()
while True:

    for i in range(100):
        cookie.click()

    
    for p in products:
        try:
            product = driver.find_element(By.ID, value=p)
            product.click()
        except:
            pass  # product not available yet, skip it





