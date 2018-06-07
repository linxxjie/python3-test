'''
打开一个不存在的网页
第一个except输出结果：
Not Found
404
Server: nginx
Date: Thu, 07 Jun 2018 14:04:24 GMT
Content-Type: text/html; charset=UTF-8
Transfer-Encoding: chunked
Connection: close
Vary: Accept-Encoding
X-Powered-By: PHP/7.0.18

第二个except结果：
ot Found

'''
from urllib import request, error
try:
    response = request.urlopen('http://www.balabala.com/index.html')
except error.HTTPError as e:
    print(e.reason, e.code, e.headers, sep='\n')
except error.URLError as e:
    print(e.reason)
else:
    print('Request Successfully')


'''
reason属性返回的不一定是字符串，也可能是一个对象
运行结果：
<class 'socket.timeout'>
Time Out

'''
import socket
import urllib.request
import urllib.error

try:
    response = urllib.request.urlopen('http://www.baidu.com', timeout=0.01)
except urllib.error.URLError as e:
    print(type(e.reason))
    if isinstance(e.reason, socket.timeout):
        print('Time Out')
