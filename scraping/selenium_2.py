from selenium import webdriver
from bs4 import BeautifulSoup
import time
import requests

#driver = webdriver.Chrome()
url = 'https://section.cafe.naver.com/ca-fe/home'

# driver.get(url)
# time.sleep(3)

# html = driver.page_source

req = requests.get(url)
html = req.text
print(html)


