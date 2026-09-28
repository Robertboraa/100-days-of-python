from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import time
from selenium.common.exceptions import ElementClickInterceptedException
speed_test_url = "https://www.speedtest.net"
y_url = "https://app.100daysofpython.dev/services/y"
class InternetSpeedTwitterBot():

    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=chrome_options)

    def get_internet_speed(self):
        self.driver.get(speed_test_url)
        time.sleep(4)
        wait = WebDriverWait(self.driver, 10)
        go_button = wait.until(ec.element_to_be_clickable(
            (By.XPATH, '//*[@id="root"]/div/div[1]/div/div[2]/div[2]/div[2]/div/div/div[2]/div[2]/button')))
        go_button.click()
        time.sleep(60)
        download = wait.until(ec.element_to_be_clickable((By.XPATH,
                                                          '//*[@id="root"]/div/div[1]/div/div[2]/div[2]/div[2]/div/div/div/div[2]/div[2]/div[1]/div[1]/div/h3')))
        upload = wait.until(ec.element_to_be_clickable((By.XPATH,
                                                        '//*[@id="root"]/div/div[1]/div/div[2]/div[2]/div[2]/div/div/div/div[2]/div[2]/div[1]/div[2]/div/h3')))
        download_number = int(download.text.split(".")[0])
        upload_number = int(upload.text.split(".")[0])
        if download_number > 100 or upload_number > 100:
            self.tweet_company(download_number, upload_number)  # pass values
        return download_number, upload_number

    def tweet_company(self, download_number, upload_number):  # receive values
        self.driver.get(y_url)
        time.sleep(2)
        wait = WebDriverWait(self.driver, 10)

        cookie = wait.until(ec.element_to_be_clickable((By.XPATH, '//*[@id="y-cookie-banner"]/button')))
        cookie.click()

        login = wait.until(ec.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[1]/a[4]')))
        login.click()
        time.sleep(2)

        email = wait.until(ec.element_to_be_clickable((By.ID, "email")))
        password = wait.until(ec.element_to_be_clickable((By.ID, "password")))
        email.send_keys("robert.bora@hotmail.com")
        password.send_keys("_cAAmbCU-ok_HRfR")

        login2 = wait.until(ec.element_to_be_clickable((By.XPATH, '/html/body/div/div/form/button')))
        login2.click()

        post = wait.until(ec.element_to_be_clickable((By.XPATH, '/html/body/div[1]/nav/button')))
        post.click()

        tweet_entry = wait.until(ec.element_to_be_clickable((By.XPATH, '//*[@id="modal-compose"]')))
        tweet_entry.send_keys(
            f"My internet speed is download={download_number} upload={upload_number} it should be higher give me my money back scammers")

        post2 = wait.until(ec.element_to_be_clickable((By.ID, "modal-post-btn")))
        post2.click()
bot = InternetSpeedTwitterBot()
bot.get_internet_speed()







