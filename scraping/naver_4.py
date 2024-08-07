import requests
from bs4 import BeautifulSoup

header_user = {"User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36"}
base_url = "https://search.naver.com/search.naver?ssc=tab.blog.all&sm=tab_jum&query="
keyword = input("검색어를 하나만 입력하세요")

url = base_url + keyword

req = requests.get(url, header_user) # .get(https://www.naver.com)
html = req.text


soup = BeautifulSoup(html, "html.parser")

wraps = soup.select(".view_wrap")

# 클래스를 통해서 하나의 정보만 가져올떄는 select_one   
# 클래스를 통해서 해당하는 모든 정보를 가져올떄는 select
# 클래스는 " . "
for i in wraps:
    ad = i.select_one(".spblog ico_ad")  # 광고 뺴고 추출
    if not ad: # 광고가 없는건 fals
            title = i.select_one(".title_link")
            name = i.select_one(".name")
            print(f"검색 키워드 : {keyword}")
            print(f"블로그 제목 : {title.text}")
            print(f"블로그 작성자 : {name.text}")
            print()