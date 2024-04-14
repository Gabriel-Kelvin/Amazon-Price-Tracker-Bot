import requests
from bs4 import BeautifulSoup
import smtplib

amazon_url = "https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1"
amazon_header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8,ta;q=0.7",
}

MY_MAIL = "gabrielkelvin184@gmail.com"
PASSWORD = "njkq qadl kxrn ovum"

response = requests.get(url=amazon_url, headers=amazon_header)
# print(response.text)

soup = BeautifulSoup(response.text, "html.parser")

# price = soup.find(name="span", class_="a-price-whole")
# print(price)

price = soup.find(class_="a-offscreen").get_text()
price_without_currency = price.split("$")[1]
cost = float(price_without_currency)
name = soup.find(name="span", class_="a-size-large product-title-word-break")
title = name.getText()
# print(cost)
# print(title)

if cost < 100:
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=MY_MAIL, password=PASSWORD)
        subject = "Low price alert"
        email_content = f"Subject: {subject} \n\n Your amazon product: {title} price has dropped down to ${cost}"
        msg = email_content.encode('utf-8')

        connection.sendmail(from_addr=MY_MAIL,
                            to_addrs="gabriel_kelvin@myyahoo.com",
                            msg=msg)