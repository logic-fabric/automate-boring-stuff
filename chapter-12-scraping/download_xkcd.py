"""Script that downloads all the strips of https://xkcd.com, using the link in the "< PREV" button to scrap from the home page to the previous ones.
"""

import os

import bs4
import requests


BASE_URL = 'https://xkcd.com'
DOWNLOAD_FOLDER = 'xkcd_strips'


def create_folder_for_downloaded_strips(folder=DOWNLOAD_FOLDER):
    if folder not in os.listdir('.'):
        os.makedirs(f'./{folder}')

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

def get_previous_page_id(soup):
    css_selector = '.comicNav a[rel="prev"]'
    previous_page_anchor = soup.select(css_selector)
    if previous_page_anchor:
        previous_page_id = previous_page_anchor[0].attrs['href'][1:-1]
        return int(previous_page_id)
    
    return None

def get_page_url(page_id):
    return f'{BASE_URL}/{page_id}/'


if __name__ == '__main__':
    create_folder_for_downloaded_strips()
    
    counter = 0
    strip_id = 10000
    page_url = BASE_URL

    while strip_id > 1:
        counter += 1

        response = get_page(page_url)
        soup = get_page_soup(response)

        strip_url = get_strip_url(soup)
        if strip_url is None:
            break

        download_strip(strip_url, counter)

        strip_id = get_previous_page_id(soup)
        if strip_id is None:
            break

        page_url = get_page_url(strip_id)
