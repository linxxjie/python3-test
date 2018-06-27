import requests

r = requests.get('https://www.baidu.com')
print(r.cookies)
for key, value in r.cookies.items():
    print(key + '=' + value)

print('------------------------------------------')

headers = {
    'Cookie': 'your cookies',
    'Host':'www.zhihu.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, '
                  'like Gecko) Chrome/67.0.3396.99 Safari/537.36'

}

r = requests.get('https://www.zhihu.com', headers=headers)
print(r.text)
