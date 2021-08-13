import requests
import smtplib
from bs4 import BeautifulSoup
import time

url = ''

headers = {
    'User-Agent': ''}


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
    sender = ''
    receiver = ''
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login(sender, '')
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
