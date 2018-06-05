import urllib.request

'''
urllib 基本用法
'''
response = urllib.request.urlopen('https://www.python.org')
# 得到返回的网页内容
print(response.read().decode('utf-8'))
# 响应的类型  <class 'http.client.HTTPResponse'>
print(type(response))
# 响应的状态码
print(response.status)
# 响应头信息
print(response.getheaders())
# 获取响应头中的server值 nginx
print(response.getheader('Server'))
