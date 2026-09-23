
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import os


ACCOUNT_EMAIL = "bora@test.com"
ACCOUNT_PASSWORD = "SuperSecretTestPassword"
GYM_URL = "https://appbrewery.github.io/gym/"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach" ,True)

user_data_dir = os.path.join(os.getcwd(), "chrome_profile")

chrome_options.add_argument(f"--user-data-dir={user_data_dir}")
driver = webdriver.Chrome(options=chrome_options)

driver.get(GYM_URL)

wait = WebDriverWait(driver, 2)
login_btn = wait.until(ec.element_to_be_clickable((By.ID, "login-button")))
login_btn.click()


e_mail_entry = wait.until(ec.presence_of_element_located((By.ID, "email-input")))
password_entry = wait.until(ec.presence_of_element_located((By.ID, "password-input")))

e_mail_entry.clear()
e_mail_entry.send_keys(ACCOUNT_EMAIL)

password_entry.clear()
password_entry.send_keys(ACCOUNT_PASSWORD)

submit_btn = driver.find_element(By.ID, "submit-button")
submit_btn.click()

wait.until(ec.presence_of_element_located((By.ID, "schedule-page")))


