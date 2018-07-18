
import pandas as pd
from bs4 import BeautifulSoup as bsoup
import requests
from urllib.parse import quote
import random
import time

################################################################
# song information data from melon

data = pd.read_csv(r"C:\Users\User\Desktop\music\song_info.csv",encoding='cp949',names=['song','singer'])

data = data.dropna(axis=0)

################################################################
# scrap lyrics using song information

def get_url(song_info):
    base_url = ('https://www.azlyrics.com/lyrics/{}.html'.format(song_info))
    return_url = base_url.format(song_info)
    return return_url

def get_html(url):
    fakeHeader = {'User-Agent':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8'}
    page_html = requests.get(url, headers=fakeHeader).text
    return page_html


def get_lyrics(index):
    i = 2
    lyrics_list=[]
    for i in range(len(F_data)):

        url = get_url(F_data[i])

        if i%11==0:
            time.sleep(random.randint(10,30))

            html = get_html(url)
            soup = bsoup(html, 'html.parser')

            if soup.find("div", class_="col-xs-12 col-lg-8 text-center") == None:
                pass
            else:
                lyrics = soup.find("div", class_="col-xs-12 col-lg-8 text-center").find_all('div')[4:7]
                lyrics_list.append(lyrics)
    return lyrics_list


song_data = [str(data['singer'][i])+'/'+str(data['song'][i]) for i in range(len(data))]

F_data = [song_data[i].lower() for i in range(1,len(song_data))]

lyrics_list = get_lyrics(F_data)

a = pd.DataFrame(lyrics_list)

a.to_csv('lyrics_data.csv')
