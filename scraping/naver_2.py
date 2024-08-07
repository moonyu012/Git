import requests
from bs4 import BeautifulSoup

header_user = {"User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36"}
url = "https://www.naver.com"

req = requests.get(url, header_user) # .get(https://www.naver.com)
# print(req.raise_for_status) # 200 성공

html = req.text
# print(html)

soup = BeautifulSoup(html, "html.parser")

query = soup.select_one(".search_input_box") 