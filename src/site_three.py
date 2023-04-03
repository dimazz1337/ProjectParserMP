import time
from datetime import datetime
from bs4 import BeautifulSoup
import requests
import concurrent.futures
from PIL import Image
from pytesseract import pytesseract
import shutil
import os
from config import html_file_path


def get_company_urls_3(urls_region):
    urls_company = []
    passtext = ['https://www.metalbulletin.ru/companies/',
                'https://www.metalbulletin.ru/companies/region/',
                'https://www.metalbulletin.ru/companies/industry/',
                'https://www.metalbulletin.ru/companies//',
                'https://www.metalbulletin.ru/companies/region/0009001D/',
                'https://www.metalbulletin.ru/companies/region/000A000E/',
                'https://www.metalbulletin.ru/companies/region/000A000F/',
                'https://www.metalbulletin.ru/companies/region/000A000C/',
                'https://www.metalbulletin.ru/companies/region/0009001B/',
                'https://www.metalbulletin.ru/companies/region/0009001A/',
                'https://www.metalbulletin.ru/companies/region/0009001C/',
                'https://www.metalbulletin.ru/companies/region/000A000D/']

    with concurrent.futures.ThreadPoolExecutor() as executor:
        responses = executor.map(requests.get, urls_region)

    for response in responses:
        soup_2 = BeautifulSoup(response.text, 'lxml')
        uniq_company = soup_2.find_all('b')
        for z in uniq_company:
            s = z.find_all('a')
            for j in s:
                s2 = j.get('href')
                if s2 in urls_region or s2 in passtext:
                    pass
                else:
                    #print(s2)
                    urls_company.append(s2)

    return urls_company

def get_name_3(url_link):
    r_name = requests.get(url_link)
    soup_name = BeautifulSoup(r_name.text, 'lxml')

    uniq_name = soup_name.find('div', class_='text2').text
    print(uniq_name)
    return uniq_name

def get_phone_3(url_link):
    r_name = requests.get(url_link)
    soup_phone = BeautifulSoup(r_name.text, 'lxml')

    phone_c = soup_phone.find('div', text='Телефон:').find_next()
    print(phone_c.text)
    return phone_c.text

def get_emails_3(download_url):
    src_urls = []
    #for t in range(len(download_url)):
    response = requests.get(download_url)
    soup = BeautifulSoup(response.content, 'html.parser')

    img_tag = soup.find_all('div', class_='text2')
    for u in img_tag:
        img_tag_2 = u.find_all('img')
        for k in img_tag_2:
            url_src = k.get('src')
            src_urls.append(url_src)

    src_urls = src_urls[1::2]

    r = requests.get(src_urls[0], stream=True)
    time.sleep(1)
    if r.status_code == 200:
        with open(f"images/site_3/03.png", 'wb') as f:
            r.raw.decode_content = True
            shutil.copyfileobj(r.raw, f)

        image = Image.open(f'images/site_3/03.png')
        path_to_tesseract = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
        pytesseract.tesseract_cmd = path_to_tesseract
        text = pytesseract.image_to_string(image)
        print(text[:-1])
        if text == '' or text == ' ' or text == None:
            os.remove(f'images/site_3/03.png')
            return None
        else:
            os.remove(f'images/site_3/03.png')
            return text[:-1]


def main_three():
    with open(html_file_path, encoding="utf8") as file:
        source = file.read()

    soup = BeautifulSoup(source, 'lxml')

    urls_region = []
    # ПАРСИНГ ВСЕХ ССЫЛОК НА РЕГИОНЫ
    link = soup.find_all('a')
    for i in link:
        url = i.get('href')
        urls_region.append(url)


    # МНОГОПОТОЧНОСТЬ
    with concurrent.futures.ThreadPoolExecutor() as CF:
        company_urls = CF.submit(get_company_urls_3, urls_region)
        names = [CF.submit(get_name_3, url) for url in company_urls.result()]
        phones = [CF.submit(get_phone_3, url) for url in company_urls.result()]
        emails = [CF.submit(get_emails_3, url) for url in company_urls.result()]

    names = [future.result() for future in names]
    phones = [future.result() for future in phones]
    emails = [future.result() for future in emails]

    print(names)
    print(phones)
    print(emails)


