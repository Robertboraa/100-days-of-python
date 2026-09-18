from bs4 import BeautifulSoup
import requests
import smtplib
import os
from dotenv import load_dotenv

load_dotenv()
URL = "https://www.amazon.com.tr/dp/B0HJB3F359/?_encoding=UTF8&th=1&pd_rd_w=658fg&content-id=amzn1.sym.67d3fa80-6861-40c5-a29b-6cd440131598&pf_rd_p=67d3fa80-6861-40c5-a29b-6cd440131598&pf_rd_r=7A4ET2B9PVA9WC7JBQ13&pd_rd_wg=tKFUl&pd_rd_r=a9c7206a-b2b6-47fd-b382-d9e751d6b23a&ref_=pd_hp_d_r_atf_unk"
my_email = os.environ.get("MY_EMAIL")
password = os.environ.get("EMAIL_PASSWORD")

response = requests.get(URL,headers= {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "tr-TR,tr;q=0.9",
    "Priority": "u=0, i",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "cross-site",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/26.6.1 Safari/605.1.15"
  }
)

amaozon_website = response.text
soup = BeautifulSoup(amaozon_website, "html.parser")
product = soup.find("span", class_="aok-offscreen")
price_text = product.getText()
product_price = int(price_text.split(",")[0].replace(".", "")) #Because of turkish format there is a .

if product_price < 180000:
    with smtplib.SMTP('smtp.gmail.com', 587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=my_email,
            msg=f"Subject:Low Price Alert!!\n\n the product price is {product_price}$!! i wouldnt miss this offer "
        )

