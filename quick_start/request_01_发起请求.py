import requests

""" 发送请求 """
# 返回Response对象
res = requests.get("https://www.baidu.com")
print(res)

# post请求，并传递参数
res = requests.post("http://httpbin.org/post", data={"key": "value"})
print(res)

# put请求
res = requests.put("http://httpbin.org/put", data={"key": "value"})
print(res)

# delete请求
res = requests.delete("http://httpbin.org/delete")
print(res)

""" url传参 """
par = {"key1": "value1", "keys": "value2"}
res = requests.get("http://httpbin.org/get", params=par)
# 查看请求的url
print(res.url)  # http://httpbin.org/get?key1=value1&keys=value2

par = {"key1": "value1", "key2": ["value2", "value3"]}
res = requests.get("http://httpbin.org/get", params=par)
print(res.url)  # http://httpbin.org/get?key1=value1&key2=value2&key2=value3