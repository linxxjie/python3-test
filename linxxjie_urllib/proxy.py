from urllib.error import URLError
from urllib.request import ProxyHandler, build_opener
"""
代理
"""
proxy_handler = ProxyHandler({
    'http': 'http://127.0.0.1:9743',
    'https': 'https://127.0.0.1:9743'
})
try:
    opener = build_opener(proxy_handler)
    response = opener.open('https://baidu.com')
    print(response.read().decode('utf-8'))
except URLError as e:
    print(e.reason)