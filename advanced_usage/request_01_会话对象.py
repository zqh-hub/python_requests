import requests

s = requests.Session()
# 会话对象让你能够跨请求保持某些参数。它也会在同一个 Session 实例发出的所有请求之间保持 cookie
s.get("http://httpbin.org/cookies/set/sessioncookie/123456789")
res = s.get("http://httpbin.org/cookies")
print(res.text)

# 提供缼省数据
s = requests.Session()
s.auth = ("user", "pass")
s.headers.update({"x-test": "true"})
res = s.get("http://httpbin.org/headers", headers={"x-test_02": "true"})
print(res.text)  # 请求头包含x-test和x-test_02

# 即使使用了session，方法级别的参数也不会跨请求保持
s = requests.Session()
res = s.get("http://httpbin.org/cookies", cookies={"example": "value"})
print(res.text)  # {"cookies": {"example": "value"}

res = s.get("http://httpbin.org/cookies")
print(res.text)  # {"cookies": {}} 参数并没保持
