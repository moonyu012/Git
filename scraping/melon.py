import requests
from bs4 import BeautifulSoup

# 멜론차트 100 스크래핑
#[순위]
# 제목 : 정보
# 가수 : 정보
# 앨범 : 정보
header_user = {"User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36"}
base_url = "https://www.melon.com/chart/index.htm"

req = requests.get(base_url,headers = header_user)
html = req.text

soup = BeautifulSoup(html,"html.parser")

# wraps = soup.select(".lst50") + soup.select(".lst100")


for wrap in soup.select('tr[data-song-no]'):
    rank = wrap.select_one(".rank").text  # 순위
    title = wrap.select_one(".ellipsis.rank01 a").text  # 제목
    artist = wrap.select_one(".ellipsis.rank02").text  # 가수
    album = wrap.select_one(".ellipsis.rank03").text  # 앨범
    
    print(f"[{rank}]")
    print(f"제목 : {title}")
    print(f"가수 : {artist}")
    print(f"앨범 : {album}")
    print()