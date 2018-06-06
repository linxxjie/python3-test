import http.cookiejar,urllib.request
"""
获取网站cookies
输出结果：
BAIDUID=2204A1725FD284FF082FCA7DDDD182AE:FG=1
BIDUPSID=2204A1725FD284FF082FCA7DDDD182AE
H_PS_PSSID=1443_21088_20927
PSTM=1528295757
BDSVRTM=0
BD_HOME=0
"""
cookie = http.cookiejar.CookieJar()
handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)
response = opener.open('http://www.baidu.com')
for item in cookie:
    print(item.name+'='+item.value)

'''
将cookies输出成文件格式
保存成mozill浏览器的cookies格式
输出结果：cookies.txt
'''
filename = 'cookies.txt'
cookie = http.cookiejar.MozillaCookieJar(filename)
handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)
response = opener.open('http://www.baidu.com')
cookie.save(ignore_discard=True,ignore_expires=True)

'''
保存成LWP格式的cookies文件
输出结果：lwp.txt
'''
filename = 'lwp.txt'
cookie = http.cookiejar.LWPCookieJar(filename)
handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)
response = opener.open('http://www.baidu.com')
cookie.save(ignore_expires=True, ignore_discard=True)

'''
读取利用cookies文件
运行结果：百度网页的源代码
'''
cookie = http.cookiejar.LWPCookieJar()
cookie.load('lwp.txt', ignore_discard=True, ignore_expires=True)
handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)
response = opener.open('http://www.baidu.com')
print(response.read().decode('utf-8'))