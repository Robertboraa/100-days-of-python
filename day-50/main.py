from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import time
from selenium.common.exceptions import ElementClickInterceptedException
ACCOUNT_EMAIL = "robocopdog@hotmail.com"
ACCOUNT_PASSWORD = "12345"
URL = "https://app.100daysofpython.dev/services/tindog/u/SSobjMxbLF-xVEbKXJRQ7WI0A8E1iLNp"
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach" ,True)


driver = webdriver.Chrome(options=chrome_options)
driver.get(URL)
wait = WebDriverWait(driver, 10)

create_account_button = wait.until(ec.element_to_be_clickable((By.XPATH, "/html/body/section[1]/div[2]/a")))
create_account_button.click()
login_with_facebark_button = wait.until(ec.element_to_be_clickable((By.XPATH, '//*[@id="login-modal"]/div/div/div/button[1]')))
login_with_facebark_button.click()

driver.switch_to.window(driver.window_handles[-1])

e_mail_entry = wait.until(ec.element_to_be_clickable((By.ID, "email")))
e_mail_entry.clear()
e_mail_entry.send_keys(ACCOUNT_EMAIL)

password_entry = wait.until(ec.element_to_be_clickable((By.ID, "pass")))
password_entry.clear()
password_entry.send_keys(ACCOUNT_PASSWORD)


submit_btn = driver.find_element(By.XPATH, "/html/body/div[2]/div/form/button")
submit_btn.click()
driver.switch_to.window(driver.window_handles[0])


location_button = wait.until(ec.element_to_be_clickable((By.XPATH, "/html/body/main/div/div/form/button")))
location_button.click()

time.sleep(1)

notifications_button = wait.until(ec.element_to_be_clickable((By.XPATH, "/html/body/main/div/div/form/button[1]")))
notifications_button.click()

time.sleep(1)
cookies_button = wait.until(ec.element_to_be_clickable((By.XPATH, '/html/body/main/div/div/form/button')))
cookies_button.click()

from selenium.common.exceptions import StaleElementReferenceException

likes = 0
while likes < 20:
    try:
        like_button = driver.find_element(By.XPATH, '//*[@id="like-button-container"]/form/button')
        like_button.click()
        likes += 1  # only count successful likes
    except NoSuchElementException:
        time.sleep(2)
    except ElementClickInterceptedException:
        try:
            back_button = driver.find_element(By.XPATH, '/html/body/main/div[3]/a')
            back_button.click()
        except NoSuchElementException:
            time.sleep(2)
    except StaleElementReferenceException:
        time.sleep(1)




