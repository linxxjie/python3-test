import urllib.request
import urllib.parse
"""
data参数使用方法（可选参数）
"""
data = bytes(urllib.parse.urlencode({'word':'hello'}), encoding='utf-8')
response = urllib.request.urlopen('http://httpbin.org/post', data=data)
print(response.read())

"""
测试结果
b'{
    "args":{},
    "data":"",
    "files":{},
    "form":{
        "word":"hello"
        },
    "headers":{
        "Accept-Encoding":"identity",
        "Connection":"close",
        "Content-Length":"10",
        "Content-Type":"application/x-www-form-urlencoded",
        "Host":"httpbin.org",
        "User-Agent":"Python-urllib/3.6"
        },
    "json":null,
    "origin":"116.3.192.240",
    "url":"http://httpbin.org/post"
    }
"""

