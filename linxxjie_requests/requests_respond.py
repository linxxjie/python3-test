import requests
r = requests.get('http://www.jianshu.com')
# 状态码
print(type(r.status_code), r.status_code)
# 响应头
print(type(r.headers), r.headers)
print(type(r.cookies), r.cookies)
print(type(r.url), r.url)
# 请求历史
print(type(r.history), r.history)