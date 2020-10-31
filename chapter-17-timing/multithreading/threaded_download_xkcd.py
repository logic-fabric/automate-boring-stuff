"""Scripts that downloads the oldest strips of https://xkcd.com.
A version of this script use one thread and, the other, multithreading.
"""

import threading
import time
import os

import bs4
import requests


BASE_URL = 'https://xkcd.com'
DOWNLOAD_FOLDER = 'xkcd_strips'


def create_folder_for_downloaded_strips(folder=DOWNLOAD_FOLDER):
    if folder not in os.listdir('.'):
        os.makedirs(f'./{folder}')

def get_page_url(page_id):
    return f'{BASE_URL}/{page_id}/'

def get_page(url):
    response = requests.get(url)
    response.raise_for_status()

    return response

def get_page_soup(response):
    soup = bs4.BeautifulSoup(response.text, 'html.parser')

    return soup

def get_strip_url(soup):
    css_selector = '#comic > img'
    strip_img = soup.select(css_selector)
    if strip_img:
        strip_url = strip_img[0].attrs['src']
        return f'https:{strip_url}'
    
    return None

def download_strip(strip_url, count, folder=DOWNLOAD_FOLDER):
    response = requests.get(strip_url)
    response.raise_for_status()

    with open(f'./{folder}/strip-{count}.png', 'wb') as f:
        for chunk in response.iter_content(100000):
            f.write(chunk)

def get_strip(strip_id, folder):
    page_url = get_page_url(strip_id)
    response = get_page(page_url)
    soup = get_page_soup(response)

    strip_url = get_strip_url(soup)
    download_strip(strip_url, strip_id, folder=folder)

def download_xkcd_with_one_thread(strips_quantity, folder):
    create_folder_for_downloaded_strips(folder)

    for strip_id in range(1, strips_quantity + 1):
        get_strip(strip_id, folder)

def download_xkcd_with_multiple_threads(strips_quantity, folder):
    create_folder_for_downloaded_strips(folder)

    for strip_id in range(1, strips_quantity + 1):
        strip_thread = threading.Thread(
            target=get_strip, 
            args=[strip_id, folder]
        )
        strip_thread.start()


if __name__ == '__main__':
    STRIPS_QUANTITY = 20

    print("--- Download XKCD strips with one thread ---")
    start = time.time()
    download_xkcd_with_one_thread(STRIPS_QUANTITY, folder=f'{DOWNLOAD_FOLDER}_one_thread')
    end = time.time()
    print(f"Strips downloaded in {round(end - start, 2)} seconds with one thread.\n")

    print("--- Download XKCD strips with multiple threads ---")
    start = time.time()
    download_xkcd_with_multiple_threads(STRIPS_QUANTITY, folder=f'{DOWNLOAD_FOLDER}_multiple_threads')
    end = time.time()
    print(f"Strips downloaded in {round(end - start, 2)} seconds with multiple threads.\n")
