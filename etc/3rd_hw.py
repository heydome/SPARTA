import requests
from bs4 import BeautifulSoup

from pymongo import MongoClient           # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)
client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsparta                      # 'dbsparta'라는 이름의 db를 만듭니다.

# URL을 읽어서 HTML를 받아오고,
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://www.genie.co.kr/chart/top200?ditc=D&ymd=20200403&hh=23&rtm=N&pg=1',headers=headers)

# HTML을 BeautifulSoup이라는 라이브러리를 활용해 검색하기 용이한 상태로 만듦
soup = BeautifulSoup(data.text, 'html.parser')

# select를 이용해서, tr들을 불러오기
songs = soup.select('#body-content > div.newest-list > div > table > tbody > tr')
#body-content > div.newest-list > div > table > tbody > tr:nth-child(1) > td.number
# songs (tr들) 의 반복문을 돌리기
#body-content > div.newest-list > div > table > tbody > tr:nth-child(1) > td.info > a.title.ellipsis
#body-content > div.newest-list > div > table > tbody > tr:nth-child(1) > td.info > a.artist.ellipsis
for song in songs:
    # song 안에 a 가 있으면,
    a_tag = song.select_one('td.info > a.title.ellipsis')
    if a_tag is not None:
        rank = song.select_one('td.number').text[0:3].strip()
        title = a_tag.text.strip()                                    
        name = song.select_one('a.artist.ellipsis').text                # td 태그 사이의 텍스트를 가져오기
        db.songs.insert({'rank':rank,'name':name,'title':title})
        
        # print(rank,title,name)
    print_song = list(db.songs.find())
# print(print_song)
for p_song in print_song:
    print(p_song['rank'],p_song['title'],p_song['name'])