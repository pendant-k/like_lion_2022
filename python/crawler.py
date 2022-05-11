# Internet 데이터 가져오기
# 실검 삭제 -> 네이버 영화 정보 가져오기
import requests
from bs4 import BeautifulSoup
from datetime import datetime


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}

response = requests.get(
    'https://movie.naver.com/movie/sdb/rank/rmovie.naver', headers=headers)


# 문자열 데이터를 적절하게 정리해줌
soup = BeautifulSoup(response.text, 'html.parser')
titles = soup.findAll('div', 'tit3')
file = open('nmovie.html', 'w')
file.write(response.text)
file.close()

rank = 1
result_file = open('result.txt', 'w')

# 평점순 영화 출력하기
print('실시간 네이버 영화 순위입니다.')
print(datetime.today().strftime("기준일자:  %Y %m %d\n"))
for title in titles:
    result_file.write(str(rank)+"위:"+title.get_text()+"\n")
    print(f'{rank}위: {title.get_text()}')
    rank += 1
