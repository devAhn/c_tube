
from __future__ import unicode_literals
# import youtube_dl
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import urllib.request
from urllib.request import urlopen
from bs4 import BeautifulSoup
import time
import os
import subprocess
from bs4 import BeautifulSoup as bs
import requests
#===================================    여기 부터는 동영상 다운로드 관련 모듈설치     ==============================================
import os
import subprocess
import pytube
from pytube import YouTube

search = (input("검색어를 입력하세요."))
search = str(search.encode('utf-8'))
search = search.replace("\\", '%').replace('x', '').upper().replace("'", "")[1:]
driver = webdriver.Chrome(r'C:\Users\sub_account\Desktop\python\chromedriver')
# url = input("검색  ")
driver.get('https://www.youtube.com/results?search_query=' + search)
# 'https://www.youtube.com/results?search_query=%EC%A0%95%EB%8F%99%EC%84%9D%EB%AA%A9%EC%82%AC%EC%84%A4%EA%B5%90/')

body = driver.find_element_by_tag_name("body")
num_of_pagedowns = 0  # 50
time.sleep(1.5)

while num_of_pagedowns:
    body.send_keys(Keys.PAGE_DOWN)
    time.sleep(1.2)
    num_of_pagedowns -= 1
    try:
        driver.find_element_by_xpath().click()
    except:
        None

html = driver.page_source

soup = BeautifulSoup(html, 'lxml')

arr_txt = list()

for sour in soup.find_all('a', href=True, title=True):
    time.sleep(0.7)
    # d = {'title' : sour['title'], 'url' : 'https://www.youtube.com' + sour['href'], 'aria' : sour.get('aria-label')}

    tmp_str_0 = sour.get('aria-label')
    print(tmp_str_0)

    d = {}

    if (tmp_str_0 != None):
        T1 = tmp_str_0.find('게시자: ');
        tmp_str_1 = tmp_str_0[T1 + 5:];
        T2 = tmp_str_1.find(' ');
        tmp_str_2 = tmp_str_1[T2:];
        pubr = tmp_str_1[0:T2];  #
        T3 = tmp_str_2.find('전');
        tmp_str_3 = tmp_str_2[T3:];
        pdate = tmp_str_2[0:T3];  #
        T4 = tmp_str_3.find('조회수 ');
        tmp_str_4 = tmp_str_3[T4:];
        run_time = tmp_str_3[1:T4];  #
        tmp_str_5 = tmp_str_4[4:-1];
        tmp_v = tmp_str_5;
        tmp_v = tmp_v.replace(",", "");
        viewer = int(tmp_v);

        d = {'title': sour['title'], 'url': 'https://www.youtube.com' + sour['href'], \
             'Pubr': pubr, 'Pdate': pdate, 'Run_time': run_time, 'Viewer': viewer}

        print('http://www.youtube.com' + sour['href'])

        arr_txt.append(d)
    time.sleep(0.5)
    response = 'https://www.youtube.com' + sour['href']
    driver.get(response)
    time.sleep(0.5)
    soup_link = BeautifulSoup(driver.page_source, 'html.parser')
    time.sleep(0.5)

    sour2 = soup_link.find_all('span', slot="date")
    print("\n영상 정보=======================================================================\n")
    x = str(sour2).find('게시일: ')
    print(str(sour2)[x:].replace('</span>', '').replace(']', ''))
    # print(sour2)

    '''r= requests.get('https://www.youtube.com' + sour['href'])

    r.text

    haha=bs(r.text,'html.parser')

'''
# 걸러내기전에 프린트하는 loop이라서 주석처리 해놨습니다.
# for a in arr_txt:
#     print(a['title'])
#     print(a['url'])
#     print(a['Pubr'])
#     print(a['Pdate'])
#     print(a['Run_time'])
#     print(a['Viewer'])
#     print()

print('end')

value1 = []
value2 = []
url = []
new_arr = []

for d in arr_txt:
    if d['Run_time'] in value1 and d['title'] in value2:
        print('중복 삭제');
    else:
        new_arr.append(d)
        value1.append(d['Run_time'])
        value2.append(d['title'])

'''ydl_opts = {
    'format': 'bestaudio/best',
    'outtmpl': 'E:\python\mp3s\%(title)s.%(ext)s',  # 여기서 원하시는 위치 설정하시면 됩니다.
    'postprocessors': [{  # 폴더가 존제하지 않으면 프로그램이 만들어줍니다.
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
}'''

'''
for a in new_arr:
    print('??')
    print(a['title'])
    print(a['url'])
    print(a['Pubr'])
    print(a['Run_time'])
    print(a['Viewer'])
'''

# with youtube_dl.YoutubeDL(ydl_opts) as ydl:
#   ydl.download(url)

# ///////////////////////////////////////////////////////////////////////////////////////////////////////////
# /////////////////////파일다운로드하는 코드////////////////////////////////////////////////
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////
# lists = []
#
# while True:
#     link = input("다운로드 받고 싶은 링크 url을 입력해주세요.:\n 더 이상 없으시면 '종료'을 입력해주세요.:   ")
#     if 'youtube.' in link:
#         lists.append(link)
#     elif '종료' in link:
#         print('파일 다운로드를 시작합니다!')
#         break
#     else:
#         print('잘못된 형식입니다. 요청에 맞게 입력해주세요.')
#
# for video_url in lists:
#     yt = YouTube(video_url)
#     print(yt.title)
#     print('다운로드 중입니다......')
#     yt.streams.first().download()
#
# print('다운로드 완료!')