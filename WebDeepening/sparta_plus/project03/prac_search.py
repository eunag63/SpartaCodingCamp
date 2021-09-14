from bs4 import BeautifulSoup
from selenium import webdriver
from time import sleep


driver = webdriver.Chrome('./chromedriver')

url = "https://search.naver.com/search.naver?where=image&sm=tab_jum&query=%EC%95%84%EC%9D%B4%EC%9C%A0"
driver.get(url)
# 1000픽셀 내리기
sleep(10)
driver.execute_script("window.scrollTo(0, 1000)")
# 맨 밑까지 내리기
sleep(1)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
sleep(10)

req = driver.page_source
driver.quit()

soup = BeautifulSoup(req, 'html.parser')
images = soup.select(".tile_item._item ._image._listImage")
print(len(images))

for image in images:
    src = image["src"]
    print(src)