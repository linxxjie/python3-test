import requests
requests.get('http://httpbin.org/cookies/set/number/123456789')
r = requests.get('http://httpbin.org/cookies')

# {"cookies":{}}
print(r.text)

s = requests.session()
s.get('http://httpbin.org/cookies/set/number/123456789')
r_session = s.get('http://httpbin.org/cookies')

# {"cookies":{"number":"123456789"}}
print(r_session.text)
