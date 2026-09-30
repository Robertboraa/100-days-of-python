from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import ElementClickInterceptedException
import time

BASE_URL = "https://app.100daysofpython.dev/services/share-a-naan/welcome"
SIMILAR_ACCOUNT = "timferriss"  # account whose followers you want to follow

class InstaFollowerBot:

    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=chrome_options)
        self.wait = WebDriverWait(self.driver, 10)

    def login(self):
        self.driver.get(BASE_URL)
        email = self.wait.until(ec.element_to_be_clickable((By.XPATH, "/html/body/div/aside/div/form/input[1]")))
        email.send_keys("robert.bora@hotmail.com")
        password = self.driver.find_element(By.XPATH, "/html/body/div/aside/div/form/input[2]")
        password.send_keys("EsWhfqBt6tEuxD4a")
        self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, '//*[@id="popup-save-login"]/div/div[2]').click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, '//*[@id="popup-notifications"]/div/button[2]').click()

    def find_followers(self):
        self.driver.get("https://app.100daysofpython.dev/services/share-a-naan/u/rordongamsay/followers")
        time.sleep(2)



    def follow(self):
        all_buttons = self.driver.find_elements(By.CSS_SELECTOR, ".followers-scroll button")
        for button in all_buttons:
            try:
                button.click()
                time.sleep(1)
            except ElementClickInterceptedException:
                # An "Unfollow?" dialog opened (you already follow this account).
                cancel = self.driver.find_element(By.XPATH, "//button[contains(text(), 'Cancel')]")
                cancel.click()


bot = InstaFollowerBot()
bot.login()
bot.find_followers()
bot.follow()