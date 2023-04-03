import time
from datetime import datetime
from bs4 import BeautifulSoup
import requests
import concurrent.futures
from PIL import Image
from pytesseract import pytesseract
import shutil
import os



def get_links_2(base_link):
    urls_site_2 = []
    r = requests.get(base_link)
    soup = BeautifulSoup(r.text, 'lxml')
    link = soup.findAll('table', class_='table participant-table')
    for i in link:
        url = i.find_all('a')
        for j in url:
            url2 = j.get('href')
            if url2 is None:
                pass
            else:
                urls_site_2.append(url2)
                #print(f'https://www.metal-expo.ru{url2}')
    return urls_site_2

def get_name_2(url):
    url_2 = "https://www.metal-expo.ru"
    uniq_urls = url_2 + url
    r_2 = requests.get(uniq_urls)
    soup_2 = BeautifulSoup(r_2.text, 'lxml')
    name = soup_2.find('span', {'itemprop': 'name'}).text
    print(name)

def get_phone_2(url):
    url_2 = "https://www.metal-expo.ru"
    uniq_urls = url_2 + url
    r_2 = requests.get(uniq_urls)
    soup_2 = BeautifulSoup(r_2.text, 'lxml')
    phone = soup_2.find('dd', {'itemprop': 'telephone'}).text
    #'['+datetime.now().strftime('%d-%m-%y %H:%M:%S')+']'
    print(phone)

def get_image_2(url):
    url_2 = "https://www.metal-expo.ru"
    uniq_urls = url_2 + url
    r_2 = requests.get(uniq_urls)
    soup_2 = BeautifulSoup(r_2.text, 'lxml')
    name = soup_2.find_all('dd')
    src_image = []
    for l in name:
        imagelnk = l.find_all('img')
        for y in imagelnk:
            done_src = y.get('src')
            src_image.append(done_src)
            #print(done_src)

    for h in range(len(src_image)):
        time.sleep(3)
        download_url = url_2 + src_image[h]
        r = requests.get(download_url, stream=True)
        if r.status_code == 200:
            with open(f"images/site_2/{h}.jpg", 'wb') as f:
                r.raw.decode_content = True
                shutil.copyfileobj(r.raw, f)
            try:
                image = Image.open(f'images/site_2/{h}.jpg')
                path_to_tesseract = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
                pytesseract.tesseract_cmd = path_to_tesseract
                text = pytesseract.image_to_string(image)
                # печать текста построчно
                print(text[:-1])
            except FileNotFoundError:
                pass

            try:
                os.remove(f'images/site_2/{h}.jpg')
            except FileNotFoundError:
                pass


def main_two():
    base_link = 'https://www.metal-expo.ru/ru/exhibition/136/participants'
    urls_site_2 = get_links_2(base_link)

    # МНОГОПОТОЧНОСТЬ
    with concurrent.futures.ThreadPoolExecutor() as cf:
        futures = []
        for url in urls_site_2:
            futures.append(cf.submit(get_name_2, url))
            futures.append(cf.submit(get_phone_2, url))
            futures.append(cf.submit(get_image_2, url))

        for ft in concurrent.futures.as_completed(futures):
            try:
                result = ft.result()
            except Exception as e:
                print(e)