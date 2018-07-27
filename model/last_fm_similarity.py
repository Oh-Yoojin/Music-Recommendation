
import pandas as pd
from bs4 import BeautifulSoup as bsoup
import requests

data = pd.read_csv(r"C:\Users\User\Desktop\music\data\lyrics\project\total_lyric.csv",encoding='cp949')

song_info = [['Title','Singer']]


def get_url(artist,title):
    base_url = ('http://ws.audioscrobbler.com/2.0/?method=track.getsimilar&artist={}&track={}&api_key={"get_lastfm_key"}')
    return_url = base_url.format(artist,title)
    return return_url

def get_html(url):
    page_html = requests.get(url).text
    return page_html

song=song_info['Title'].tolist()
singer=song_info['Singer'].tolist()


def similarity_song(info):
    song_li = []
    simi_song = []
    for i in range(len(info)):
        url = get_url(singer[i],song[i])
        html = get_html(url)
        song_li.append(info.values[i][:2].tolist())
        soup = bsoup(html, 'html.parser')
        simi_song_str = soup.find_all('name')[:20]
        simi_song.append(simi_song_str)
    return song_li,simi_song

song_li, simi_song = similarity_song(song_info)


song_li = []
simi_song = []
for i in range(len(song_info)):
    url = get_url(singer[i],song[i])
    html = get_html(url)
    song_li.append(song_info.values[i][:2].tolist())
    soup = bsoup(html, 'html.parser')
    simi_song_str = soup.find_all('name')[:20]
    simi_song.append(simi_song_str)


song_simi_list = []
for song in simi_song:
    song_simi_list.append([str(name) for name in song])


last_fm_list = pd.DataFrame(song_simi_list)
last_fm_list.columns = ['title','artist','title2','artist2','title3','artist3','title4','artist4','title5','artist5','title6','artist6','title7','artist7','title8','artist8','title9','artist9','title10','artist10']

my_song_list = pd.DataFrame(song_li)
my_song_list.columns = ['original_title','original_artist']

similarity_data=pd.concat((my_song_list,last_fm_list),axis=1)
