from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pyquery import PyQuery as pq
import pymongo

# 数据库连接信息
MONGO_URL = 'localhost'
MONGO_DB = 'taobao'
MONGO_COLLECTION = 'products'
client = pymongo.MongoClient(MONGO_URL)
db = client[MONGO_DB]
collection = db.products

# 使用Chrome的headless模式
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
browser = webdriver.Chrome(chrome_options=chrome_options)
# browser = webdriver.Chrome()

# 使用显式等待
wait = WebDriverWait(browser, 10)


def get_pages(keyword, page):
    print('正在爬第', page, '页')
    try:
        url = 'https://s.taobao.com/search?q=' + keyword
        browser.get(url)
        if page > 1:
            input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#mainsrp-pager div.form input.J_Input')))
            button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#mainsrp-pager div.form span.J_Submit')))
            input.clear()
            input.send_keys(page)
            button.click()
        wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, '#mainsrp-pager ul.items li.active'), str(page)))
        get_goods_msg()
    except Exception:
        get_pages(keyword, page)

# 获取商品信息
def get_goods_msg():
    html = browser.page_source
    doc = pq(html)
    items = doc.find('#mainsrp-itemlist .items .J_MouserOnverReq').items()
    for item in items:
        product = {
            'image': item.find('.pic .img').attr('data-src'),
            'price': item.find('.price').text(),
            'deal':  item.find('.deal-cnt').text(),
            'title': item.find('.title').text(),
            'shop': item.find('.shop').text(),
            'location': item.find('.location').text()
        }
        print(product)
        save_to_mongo(product)

# 保存到 MongoDB
def save_to_mongo(result):
    try:
        if db[MONGO_COLLECTION].insert(result):
            print('保存成功')
    except Exception:
        print('保存失败')


if __name__ == '__main__':
    MAX_PAGE = 100
    keyword = input('请输入商品名称：')
    for i in range(1, MAX_PAGE + 1):
        get_pages(keyword, i)


