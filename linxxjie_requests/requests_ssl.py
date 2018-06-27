import requests
# 将verify参数设置为False解决证书验证问题
r = requests.get('https://www.12306.cn', verify=False)
print(r.status_code)