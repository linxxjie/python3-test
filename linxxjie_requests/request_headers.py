import requests
header = {
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/67.0.3396.87 Mobile Safari/537.36'
}
r = requests.get("https://www.zhihu.com/explore", headers=header)
print(r.text)