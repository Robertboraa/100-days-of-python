import requests
from bs4 import BeautifulSoup
import re
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import time
url_to_google_docs = "https://docs.google.com/forms/d/e/1FAIpQLSevIl7QXFdaSibCLRXmqtgGS4P-EltpZdi28cLL8UkutMZ_qw/viewform?usp=publish-editor"
zillow_url = "https://appbrewery.github.io/Zillow-Clone/"

headers = {"Accept-Language": "en-GB,en;q=0.9", "User-Agent": "Mozilla/5.0"}
response = requests.get(zillow_url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

links = [a["href"] for a in soup.find_all("a", attrs={"data-test": "property-card-link"})]
prices = [re.split(r'[+/]', span.getText())[0] for span in soup.find_all("span", attrs={"data-test": "property-card-price"})]
addresses = [addr.getText().strip() for addr in soup.find_all("address", attrs={"data-test": "property-card-addr"})]
print(links)
print(prices)
print(addresses)
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
wait = WebDriverWait(driver, 10)

for i in range(len(addresses)):
    driver.get(url_to_google_docs)
    time.sleep(2)

    # Address field
    address_field = wait.until(ec.element_to_be_clickable((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')))
    address_field.send_keys(addresses[i])

    # Price field
    price_field = wait.until(ec.element_to_be_clickable((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')))
    price_field.send_keys(prices[i])

    # Link field
    link_field = wait.until(ec.element_to_be_clickable((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')))
    link_field.send_keys(links[i])

    # Submit
    submit = wait.until(ec.element_to_be_clickable((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')))
    submit.click()
    time.sleep(2)

driver.quit()