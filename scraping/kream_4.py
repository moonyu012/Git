from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options

#클래스, 아이디, css_selector를 이용하고자 할때 사용
from selenium.webdriver.common.by import By

# 키보드로 입력할 수 있는 기능 제공
from selenium.webdriver.common.keys import Keys
import time


header_user = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36"

options = Options()
options.add_argument(f"User-Agent={header_user}")
options.add_experimental_option("detach", True)
#크롬 브라우저 상단에 노출되는 자동화된 정보를 삭제하는 기능
options.add_experimental_option("excludeSwitches", ["enable-logging"])

driver = webdriver.Chrome()

url = "https://kream.co.kr/"
driver.get(url)
time.sleep(1)

driver.find_element(By.CSS_SELECTOR,".search_btn_box").click() # 위치를 찾아서 클릭해라
time.sleep(1)

driver.find_element(By.CSS_SELECTOR,".input_search.show_placeholder_on_focus").send_keys("슈프림")
time.sleep(1)

driver.find_element(By.CSS_SELECTOR,".input_search.show_placeholder_on_focus").send_keys(Keys.ENTER)
time.sleep(1)

for i in range(10):
    driver.find_element(By.TAG_NAME, "body").send_keys(Keys.PAGE_DOWN)
    time.sleep(0.5)

html = driver.page_source
soup = BeautifulSoup(html, "html.parser")
#item_inner
items = soup.select(".item_inner")

product_list = []

for i in items:
    product_name = i.select_one(".translated_name").text
    if "후드" in product_name:
        category = "상의"
        product_brand = i.select_one(".product_info_brand.brand").text
        product_name_hood = i.select_one(".translated_name").text
        product_price = i.select_one(".amount").text

        print(category, product_brand ,product_name_hood , product_price) 

driver.quit()