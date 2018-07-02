import requests
import re
def get_one_page(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.text
    return None

def main():
    url = 'http://maoyan.com/board/4'
    html = get_one_page(url)
    parse_one_page(html)

def parse_one_page(html):
    pattern = re.compile(
        '<dd>'
        '.*?board-index.*?>(.*?)</i>'
        '.*?data-src="(.*?)"'
        '.*?name.*?a.*?>(.*?)</a>'
        '.*?star.*?>(.*?)</p>'
        '.*?releasetime.*?>(.*?)</p>'
        '.*?integer.*?>(.*?)</i>.*?fraction.*?>(.*?)</i>'
        '.*?</dd>', re.S
    )
    items = re.findall(pattern, html)
    print(items)

main()