import requests
import smtplib
from bs4 import BeautifulSoup
import time

url = 'https://www.hepsiburada.com/xiaomi-mi-band-5-akilli-bileklik-global-versiyon-p-HBV00000V3WEC?magaza=BUSE%20MOBILE'

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36'}


def check_price():
    page = requests.get(url, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    title = soup.find(id='product-name').get_text().strip()
    title = title[0:17]
    print(title)
    span = soup.find(id='offering-price')
    content = span.attrs.get('content')
    price = float(content)
    print(content)

    if (price <= 210):
        send_mail(title)


def send_mail(title):
    sender = 'adilaxmedov13@gmail.com'
    receiver = 'kamil.axmedov.1950@gmail.com'
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login(sender, 'zkuloaioixjjdvxe')
        subject = title + 'Istedigin fiyata dustu!'
        body = 'Bu linkten Gide bilirsin =>' + url
        mailContent = f"To:{receiver}\nFrom:{sender}\nSubject:{subject}\n\n{body}"
        server.sendmail(sender, receiver, mailContent)
        print('Mail Gonderildi')
    except smtplib.SMTPException as e:
        print(e)
    finally:
        server.quit()


while (1):
    check_price()
    time.sleep(60 * 60)
