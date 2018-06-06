from urllib import request, parse
'''
class.urllib.request.Request(url, data=None, headers={}, 
                       origin_req_host=None, unverifiable=False, method=None)
1、url 用于请求URL为必传参数，其他都是可选参数
2、data必须传bytes(字节流)类型的
3、headers：请求头
4、origin_req_host：请求方的host名称或者ip地址
5、unverifiable：表示这个请求是否是无法验证的，默认为false，意思就是用户没有足够的权限
    来选择接收这个请求的结果
6、method：是一个字符串，用来指定请求使用的方法。
'''
url = 'http://httpbin.org/post'
headers = {
    'User-Agent': 'Mozilla/4.0(compatible;MSIE 5.5;Windows NT)',
    'Host': 'httpbin.org'
}
dict = {
    'name': 'Suaan'
}
data = bytes(parse.urlencode(dict),encoding='utf-8')
req = request.Request(url=url, data=data, headers=headers, method='POST')
response = request.urlopen(req)
print(response.read().decode('utf-8'))

'''
返回结果：

{
    "args":{},
    "data":"",
    "files":{},
    "form":{
        "name":"Suaan"
        },
    "headers":{
        "Accept-Encoding":"identity",
        "Connection":"close",
        "Content-Length":"10",
        "Content-Type":"application/x-www-form-urlencoded",
        "Host":"httpbin.org",
        "User-Agent":"Mozilla/4.0(compatible;MSIE 5.5;Windows NT)"},
        "json":null,
        "origin":"113.235.123.238",
        "url":"http://httpbin.org/post"
        }
'''