import requests
data = {
    'name': 'balabala',
    'age': '22'
}
response = requests.get('http://httpbin.org/get', params=data)
print(response.text)
print(response.json())
print(type(response.json()))

'''
抓取知乎
'''
import re
headers = {
    'User-Agent': 'Mozilla/5.0(Machintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML,like Cecko)'
                  'Chrome/52.0.2743.116 Safari/537.36'
}
r = requests.get('https://www.zhihu.com/explore',headers=headers)
pattern = re.compile('explore-feed.*?question_link.*?>(.*?)</a>', re.S)
titles = re.findall(pattern, r.text)
print(titles)

# 抓取github图标
r_icon = requests.get('https://github.com/favicon.ico')
with open('favicon.ico', 'wb') as f:
    f.write(r_icon.content)

