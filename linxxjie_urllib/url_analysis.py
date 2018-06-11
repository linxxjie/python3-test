'''
解析链接
一、urlparse
输出结果：
<class 'urllib.parse.ParseResult'>
ParseResult(scheme='http', netloc='www.baidu.com', path='/index.html',
    params='user', query='id=5', fragment='comment')
解析时有特定的分隔符
://前面就是scheme，代表协议
第一个/符号前面是netloc，代表域名
后面是path，即访问路径
分号；前面是params，代表参数
问号？后面是查询条件query
#后面是锚点，用于直接定位页面内部的下拉位置
标准链接格式：
scheme://netloc/path;params?query#fragment
'''
from urllib.parse import urlparse
result = urlparse('http://www.baidu.com/index.html;user?id=5#comment')
print(type(result), result)
print('------------------------------')
'''
urlparse()方法
API：
urllib.parse.urlparse(urlstring, scheme='', allow_fragment=True)
'''
# 1、scheme：他是默认协议，假如这个链接没有带协议信息，会将这个作为默认的协议

# 输出结果：ParseResult(scheme='https',
#           netloc='', path='www.baidu.com/index.html', params='user', query='id=5', fragment='comment')
result_scheme = urlparse('www.baidu.com/index.html;user?id=5#comment', scheme='https')
print(result_scheme)
# 输出结果：ParseResult(scheme='http', netloc='www.baidu.com', path='/index.html', params='user',
#            query='id=5', fragment='comment')
result_scheme_http = urlparse('http://www.baidu.com/index.html;user?id=5#comment', scheme='https')
print(result_scheme_http)
print('--------------------------------')

# 2、allow_fragments即是否忽略fragment，如果设为False，fragment部分会被省略
# 输出结果：ParseResult(scheme='http', netloc='www.baidu.com', path='/index.html', params='user',
#            query='id=5#comment', fragment='')
result_fragment = urlparse('http://www.baidu.com/index.html;user?id=5#comment', allow_fragments=False)
print(result_fragment)
print('----------------------------------')

# 3、假设url中不包含params和query
# 输出结果：ParseResult(scheme='http', netloc='www.baidu.com',
#           path='/index.html#comment', params='', query='', fragment='')
result_test = urlparse('http://www.baidu.com/index.html#comment', allow_fragments=False)
print(result_test)
print(result_test.scheme, result_test[0], result_test.netloc, result_test[1], sep='\n')
print('**********************************')

'''
二、urlunparse()
接受的参数是一个可迭代对象，但是它的长度必须是6
输出结果：http://www.baidu.com/index.html;user?a=6#comment
'''
from urllib.parse import urlunparse
data = ['http', 'www.baidu.com', 'index.html', 'user', 'a=6', 'comment']
print(urlunparse(data))
print('***********************************')

'''
三、urlsplit()
与urlparse()类似，只是它不再包含params，只返回五个结果，上面例子中的params会合并到path中
输出结果：SplitResult(scheme='http', netloc='www.baidu.com', path='/index.html;user', query='id=5', fragment='comment')
'''
from urllib.parse import urlsplit
result_split = urlsplit('http://www.baidu.com/index.html;user?id=5#comment')
print(result_split)
print('**********************************')

'''
三、urlunsplit()
与urlunparse()类似，长度必须为5
输出结果：http://www.baidu.com/index.html?a=6#comment
'''
from urllib.parse import urlunsplit
data_unsplit = ['http', 'www.baidu.com', 'index.html', 'a=6', 'comment']
print(urlunsplit(data_unsplit))
print('*************************************')

'''
四、urljoin():
我们可以提供一个base_url（基础链接）作为第一个参数，将新的链接作为第二个参数，该方法会分析base_url的
scheme、netloc、和pach这三个内容并对新链接缺失的部分进行补充。
注：base_url中的params、query和fragment是不起作用的。
输出结果：
http://www.baidu.com/FAQ.html
https:/balabala.com/FAQ.html
https://balabala.com/index.php
'''
from urllib.parse import urljoin
print(urljoin('http://www.baidu.com', 'FAQ.html'))
print(urljoin('http://www.baidu.com', 'https:/balabala.com/FAQ.html'))
print(urljoin('http://www.baidu.com?wd=abc', 'https://balabala.com/index.php'))
print('*********************************')

'''
五、urlencode()
在构造GET请求参数时非常有用
输出结果：http://www.baidu.com?name=balabala&age=22
'''
from urllib.parse import urlencode
params = {
    'name': 'balabala',
    'age': '22'
}
base_url = 'http://www.baidu.com?'
url = base_url + urlencode(params)
print(url)
print('*************************************')

'''
六、parse_qs()
反序列化，将GET请求参数转回字典
输出结果：
{'name': ['balabala'], 'age': ['22']}
'''
from urllib.parse import parse_qs
query = 'name=balabala&age=22'
print(parse_qs(query))
print('***************************')

'''
七、parse_qsl():
用于将参数转化为元组组成的列表
输出结果：[('name', 'balabala'), ('age', '22')]
'''
from urllib.parse import parse_qsl
quert_qsl = 'name=balabala&age=22'
print(parse_qsl(quert_qsl))
print('*************************************')

'''
八、quote()
将内容转化为URL编码的格式。
输出结果：https://www.baidu.com/s?wd=%E5%A3%81%E7%BA%B8
'''
from urllib.parse import quote
keyword = '壁纸'
url = 'https://www.baidu.com/s?wd=' + quote(keyword)
print(url)
print('***********************************')

'''
九、unquote()
可以进行url解码
输出结果：https://www.baidu.com/s?wd=壁纸
'''
from urllib.parse import unquote
url = 'https://www.baidu.com/s?wd=%E5%A3%81%E7%BA%B8'
print(unquote(url))

