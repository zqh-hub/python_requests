import requests

""" 复杂post """
# 传递表单数据
data = {"key1": "value1", "key2": "value2"}
res = requests.post("http://httpbin.org/post", data=data)
print(res.text)

# 一个key多个值时
data = {"key1": ("value2", "value2")}
res = requests.post("http://httpbin.org/post", data=data)
print(res.text)

# json个格式
url = "https://api.github.com/some/endpoint"
data = {"some": "data"}
res = requests.post(url, json=data)
print(res.text)

import json

url = "https://api.github.com/some/endpoint"
data = {"some": "data"}
res = requests.post(url, json=json.dumps(data))
print(res.text)
