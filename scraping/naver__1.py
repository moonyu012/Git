import requests
from bs4 import BeautifulSoup

url = "https://www.naver.com"

req = requests.get(url) # .get(https://www.naver.com)
# print(req) # 200 성공

html = req.text
# print(html)

soup = BeautifulSoup(html, "html.parser")

query = soup.select_one(".search_input_box") # . 클래스를 뜻함
# print(query)