import time
from datetime import datetime
from bs4 import BeautifulSoup
import requests
import threading
import urllib.parse
import re
import urllib.parse


# ПАРСИНГ ССЫЛОК НА КОМПАНИИ
def get_urls():
    urls = []
    base_url = 'https://www.metalinfo.ru'
    url_link = 'https://www.metalinfo.ru/ru/directory/list.html?letter='
    r = requests.get(url_link)
    soup = BeautifulSoup(r.text, 'lxml')

    link = soup.findAll('div', class_='directory-list')

    for i in link:
        url = i.find_all('a')
        for j in url:
            url2 = j.get('href')
            urls.append(url2)
    return urls

# ПАРСИНГ НАЗВАНИЙ
def get_names(urls):
    base_url = 'https://www.metalinfo.ru'

    for j in range(len(urls)):
        name_from_link = base_url + urls[j]
        r_name = requests.get(name_from_link)
        soup_name = BeautifulSoup(r_name.text, 'lxml')

        name_company = soup_name.find('h1', {'class': 'title name'}).text
        print(name_company)

# ПАРСИНГ НОМЕРОВ
def get_phones(urls):
    base_url = 'https://www.metalinfo.ru'

    for x in range(len(urls)):
        phone_from_link = base_url + urls[x]
        r_phone = requests.get(phone_from_link)
        soup_phone = BeautifulSoup(r_phone.text, 'lxml')

        phone = soup_phone.find('dl', {'class': 'dl-horizontal'}).find('dd', {'itemprop': 'telephone'}).text
        print(phone)

# ПАРСИНГ ПОЧТ
def get_emails(urls):
    base_url = 'https://www.metalinfo.ru'

    for z in range(len(urls)):
        email_from_link = base_url + urls[z]
        r_email = requests.get(email_from_link)
        soup_email = BeautifulSoup(r_email.content, 'html.parser')

        scripts = soup_email.find_all('script', text=re.compile(r'eval\(unescape'))

        if len(scripts) == 0:
            print('None')
        else:
            for script in scripts:
                encoded_email = re.search(r"unescape\('(.*)'\)", script.string).group(1)
                decoded_email = urllib.parse.unquote(encoded_email)
                decoded_email = re.sub(r'document\.write', '', decoded_email)
                decoded_email = decoded_email.strip("'")

                text_email = BeautifulSoup(decoded_email, 'html.parser').get_text()
                r = []

                r.append(text_email[2:-3])
                print(*r)

# МНОГОПОТОЧНОСТЬ
def main_one():
    urls = get_urls()

    t1 = threading.Thread(target=get_names, args=(urls,))
    t2 = threading.Thread(target=get_phones, args=(urls,))
    t3 = threading.Thread(target=get_emails, args=(urls,))

    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()