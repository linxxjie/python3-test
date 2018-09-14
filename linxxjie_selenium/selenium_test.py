from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import time
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 基本操作
def basic_operation(browser):
    # 请求网页
    browser.get('https://www.taobao.com')
    # 单个查找
    input = browser.find_element(By.ID, 'q')
    # 多个查找
    lis = browser.find_elements(By.CSS_SELECTOR, '.service-bd li')
    # 节点交互
    input.send_keys('iphone')
    time.sleep(1)
    input.clear()
    input.send_keys('iPad')
    button = browser.find_element_by_class_name('btn-search')
    button.click()

# 动作链
def action_chain(browser):
    url = 'http://www.runoob.com/try/try.php?filename=jqueryui-api-droppable'
    browser.get(url)
    browser.switch_to_frame('iframeResult')
    source = browser.find_element_by_css_selector('#draggable')
    target = browser.find_element_by_css_selector('#droppable')
    actions = ActionChains(browser)
    actions.drag_and_drop(source, target)
    actions.perform()

# 执行JavaScript
def action_javascript(browser):
    browser.get('https://www.zhihu.com/explore')
    browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')
    browser.execute_script('alert("To Bottom")')

# 获取节点信息
def get_node_message(browser):
    url = 'https://www.zhihu.com/explore'
    browser.get(url)
    input = browser.find_element_by_class_name('zu-top-add-question')
    print(input.text)
    # 节点在页面的相对位置
    print(input.location)
    # 获取标签名
    print(input.tag_name)
    # 获取节点的宽高
    print(input.size)

# 切换frame
def switchover_frame(browser):
    url = 'http://www.runoob.com/try/try.php?filename=jqueryui-api-droppable'
    browser.get(url)
    # 切换到子 Frame 里面
    browser.switch_to.frame('iframeResult')
    try:
        logo = browser.find_element_by_name('logo')
    except NoSuchElementException:
        print('NO LOGO')
    # 切回父级Frame
    browser.switch_to.parent_frame()
    logo = browser.find_element_by_class_name('logo')
    print(logo)
    print(logo.text)

# 隐式等待
def delay_waite_implicitly(browser):
    browser.implicitly_wait(10)
    browser.get('https://www.zhihu.com/explore')
    input = browser.find_element_by_class_name('zu-top-add-question')
    print(input)

# 显式等待
def delay_waite_explicit(browser):
    browser.get('https://www.taobao.com/')
    # 最长等待时间
    wait = WebDriverWait(browser, 10)
    # 等待条件 presence_of_element_located 节点出现
    input = wait.until(EC.presence_of_element_located((By.ID, 'q')))
    button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.btn-search')))
    print(input, button)

# 前进后退
def forward_and_back(browser):
    browser.get('https://www.baidu.com/')
    browser.get('https://www.taobao.com/')
    browser.get('https://www.zhihu.com/')
    browser.back()
    time.sleep(1)
    browser.forward()
    browser.close()

# Cookies
def cookies_operation(browser):
    browser.get('https://www.zhihu.com/explore')
    print(browser.get_cookies())
    browser.add_cookie({
        'name': 'name',
        'domain': 'www.zhihu.com',
        'value': 'germey'
    })
    print(browser.get_cookies())
    browser.delete_all_cookies()
    print(browser.get_cookies())

# 选项卡管理
def tab_management(browser):
    browser.get('https://www.baidu.com')
    browser.execute_script('window.open()')
    print(browser.window_handles)
    browser.switch_to_window(browser.window_handles[1])
    browser.get('https://www.taobao.com')
    time.sleep(1)
    browser.switch_to_window(browser.window_handles[0])
    browser.get('https://python.org')

# 异常处理
def exception_dispose(browser):
    try:
        browser.get('https://www.baidu.com')
    except TimeoutException:
        print('Time Out')
    try:
        browser.find_element_by_id('htllo')
    except NoSuchElementException:
        print('No Element')
    finally:
        browser.close()

if __name__ == '__main__':
    # 声明浏览器对象
    browser = webdriver.Chrome()
    exception_dispose(browser)