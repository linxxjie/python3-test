import re
content = 'Hello 1234567 World_This is a Regex Demo'
print(len(content))
# result = re.match('Hello\s\d\d\d\s\d{4}\s\w{10}', content)
result = re.match('^Hello.*Demo$',content)
print(result)
print(result.group())
print(result.span())
# 贪婪匹配
# r = re.match('^He.*(\d+).*Demo$', content)
# 非贪婪匹配(若.*?在字符串结尾可能匹配不到任何内容了)
r = re.match('^He.*?(\d+).*Demo$', content)
print(r)
print(r.group(1))
