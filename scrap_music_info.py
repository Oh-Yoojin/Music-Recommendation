#CSS Selector##########################################################
######## genre:pop melon song, singer list#####
#Final##########################

import pandas as pd
from bs4 import BeautifulSoup as bsoup
import requests
from urllib.parse import quote
import random
import time
import re


def get_url(start_song):
    base_url = ('http://www.melon.com/genre/song_listPaging.htm?startIndex={}&pageSize=50&gnrCode=GN0900&dtlGnrCode=GN0901&orderBy=POP&steadyYn=N'.format(start_song))
    return_url = base_url.format(start_song)
    return return_url

def get_html(url):
    page_html = requests.get(url).text
    return page_html


start_song = [str(x) for x in range(10000,50000,50)]


def get_song(index):
    song_list = []
    for x in index:
        url = get_url(x)
        html = get_html(url)
        soup = bsoup(html, 'html.parser')
        song = soup.select('.wrap_song_info')
        song_list += [x.text for x in song]
    return song_list


def song_detail(song_list):
    song_info = []
    for i in range(len(song_list)): #len(song_list)
        if i%2 ==0:
            song = str(song_list[i]).split('\n')[2]
            singer_bf= str(song_list[i]).split('\n')[5].split(',')
            if(len(singer_bf )) >2:
                singer = singer_bf[0]
            else:
                singer = singer_bf[0][:int(len(singer_bf[0])/2)]
            info_list = [song, singer]
            song_info.append(info_list)
    return song_info

get_song(start_song)
song_detail(song_list)



song_info=pd.DataFrame(song_info)
song_info.to_csv('song_info.csv')


##########genre:rock/metal##############################################


def get_url(start_song):
    base_url = ('http://www.melon.com/genre/song_listPaging.htm?startIndex={}&pageSize=50&gnrCode=GN1000&dtlGnrCode=GN1001&orderBy=POP&steadyYn=N'.format(start_song))
    return_url = base_url.format(start_song)
    return return_url


def get_html(url):
    page_html = requests.get(url).text
    return page_html


start_song = [str(x) for x in range(1,10000,50)]


song_list = []
for x in start_song:
    url = get_url(x)
    html = get_html(url)
    soup = bsoup(html, 'html.parser')
    song = soup.select('.wrap_song_info')
    song_list += [x.text for x in song]



song_info = []
for i in range(len(song_list)): #len(song_list)
    if i%2 ==0:
        song = str(song_list[i]).split('\n')[2]
        singer_bf= str(song_list[i]).split('\n')[5].split(',')
        if(len(singer_bf )) >2:
            singer = singer_bf[0]
        else:
            singer = singer_bf[0][:int(len(singer_bf[0])/2)]
        info_list = [song, singer]
        song_info.append(info_list)



song_info=pd.DataFrame(song_info)
song_info.to_csv('rock_info.csv')

import os
os.getcwd()


##########genre:electronica##############################################


def get_url(start_song):
    base_url = ('http://www.melon.com/genre/song_listPaging.htm?startIndex={}&pageSize=50&gnrCode=GN1100&dtlGnrCode=GN1101&orderBy=POP&steadyYn=N'.format(start_song))
    return_url = base_url.format(start_song)
    return return_url


def get_html(url):
    page_html = requests.get(url).text
    return page_html


start_song = [str(x) for x in range(1,10000,50)]



song_list = []
for x in start_song:
    url = get_url(x)
    time.sleep(random.randint(1,10))
    html = get_html(url)
    soup = bsoup(html, 'html.parser')
    song = soup.select('.wrap_song_info')
    song_list += [x.text for x in song]




song_info = []
for i in range(len(song_list)): #len(song_list)
    if i%2 ==0:
        song = str(song_list[i]).split('\n')[2]
        singer_bf= str(song_list[i]).split('\n')[5].split(',')
        if(len(singer_bf )) >2:
            singer = singer_bf[0]
        else:
            singer = singer_bf[0][:int(len(singer_bf[0])/2)]
        info_list = [song, singer]
        song_info.append(info_list)




song_info=pd.DataFrame(song_info)
song_info.to_csv('elec_info.csv')



##########genre:R&B/Soul##############################################


def get_url(start_song):
    base_url = ('http://www.melon.com/genre/song_listPaging.htm?startIndex={}&pageSize=50&gnrCode=GN1300&dtlGnrCode=GN1301&orderBy=POP&steadyYn=N'.format(start_song))
    return_url = base_url.format(start_song)
    return return_url


def get_html(url):
    page_html = requests.get(url).text
    return page_html


start_song = [str(x) for x in range(1,10000,50)]



song_list = []
for x in start_song:
    url = get_url(x)
    time.sleep(random.randint(1,10))
    html = get_html(url)
    soup = bsoup(html, 'html.parser')
    song = soup.select('.wrap_song_info')
    song_list += [x.text for x in song]



song_info = []
for i in range(len(song_list)): #len(song_list)
    if i%2 ==0:
        song = str(song_list[i]).split('\n')[2]
        singer_bf= str(song_list[i]).split('\n')[5].split(',')
        if(len(singer_bf )) >2:
            singer = singer_bf[0]
        else:
            singer = singer_bf[0][:int(len(singer_bf[0])/2)]
        info_list = [song, singer]
        song_info.append(info_list)




song_info=pd.DataFrame(song_info)
song_info.to_csv('RandB_info.csv')


##########genre:Fork/blus##############################################


def get_url(start_song):
    base_url = ('http://www.melon.com/genre/song_listPaging.htm?startIndex={}&pageSize=50&gnrCode=GN1300&dtlGnrCode=GN1301&orderBy=POP&steadyYn=N'.format(start_song))
    return_url = base_url.format(start_song)
    return return_url


def get_html(url):
    page_html = requests.get(url).text
    return page_html


start_song = [str(x) for x in range(1,10000,50)]



song_list = []
for x in start_song:
    url = get_url(x)
    time.sleep(random.randint(1,10))
    html = get_html(url)
    soup = bsoup(html, 'html.parser')
    song = soup.select('.wrap_song_info')
    song_list += [x.text for x in song]



song_info = []
for i in range(len(song_list)): #len(song_list)
    if i%2 ==0:
        song = str(song_list[i]).split('\n')[2]
        singer_bf= str(song_list[i]).split('\n')[5].split(',')
        if(len(singer_bf )) >2:
            singer = singer_bf[0]
        else:
            singer = singer_bf[0][:int(len(singer_bf[0])/2)]
        info_list = [song, singer]
        song_info.append(info_list)




song_info=pd.DataFrame(song_info)
song_info.to_csv('Fork_info.csv')



##########genre:rap##############################################


def get_url(start_song):
    base_url = ('http://www.melon.com/genre/song_listPaging.htm?startIndex={}&pageSize=50&gnrCode=GN1200&dtlGnrCode=GN1201&orderBy=POP&steadyYn=N'.format(start_song))
    return_url = base_url.format(start_song)
    return return_url


def get_html(url):
    page_html = requests.get(url).text
    return page_html


start_song = [str(x) for x in range(1,10000,50)]



song_list = []
for x in start_song:
    url = get_url(x)
    time.sleep(random.randint(1,10))
    html = get_html(url)
    soup = bsoup(html, 'html.parser')
    song = soup.select('.wrap_song_info')
    song_list += [x.text for x in song]



song_info = []
for i in range(len(song_list)): #len(song_list)
    if i%2 ==0:
        song = str(song_list[i]).split('\n')[2]
        singer_bf= str(song_list[i]).split('\n')[5].split(',')
        if(len(singer_bf )) >2:
            singer = singer_bf[0]
        else:
            singer = singer_bf[0][:int(len(singer_bf[0])/2)]
        info_list = [song, singer]
        song_info.append(info_list)


song_info=pd.DataFrame(song_info)
song_info.to_csv('rap_info.csv')
