from urllib.robotparser import RobotFileParser
rp = RobotFileParser()
# 可以直接写url: rp = RobotFileParser('http://www.jianshu.com/robots.txt')
rp.set_url('http://www.jianshu.com/robots.txt')
# 读取robots.txt文件并进行分析，注意，这个方法执行一个读取和分析操作，如果不调用这个方法，接下来的判断都会为false
rp.read()
# 使用can_fetch方法判断网页是否可以被抓取
print(rp.can_fetch('*', 'http://www.jianshu.com/p/b67554025d7d'))
print(rp.can_fetch('*', 'http://www.jianshu.com/search?q=python&page=1&type=collections'))
# 使用parse()方法执行读取和分析。
from urllib.robotparser import RobotFileParser
from urllib.request import urlopen
rp_parse = RobotFileParser()
rp_parse.parse(urlopen('http://www.baidu.com/robots.txt').read().decode('utf-8').split('\n'))
print(rp_parse.can_fetch('*', 'http://www.jianshu.com/p/b67554025d7d'))
print(rp_parse.can_fetch('*', 'http://www.jianshu.com/search?q=python&page=1&type=collections'))
