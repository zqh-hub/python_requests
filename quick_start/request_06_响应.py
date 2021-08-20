import requests

""" 响应状态码 """
res = requests.get("http://httpbin.org/get")
print(res.status_code)

# 内置的状态码查询对象
code = res.status_code == requests.codes.ok
print(code)

# 抛出异常
res = requests.get("http://httpbin.org/status/404")
# res.raise_for_status()

""" 响应头 """
print(res.headers)
print(res.headers["date"])
