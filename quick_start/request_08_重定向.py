import requests

# 默认情况下，除了 HEAD, Requests 会自动处理所有重定向。
res = requests.get("http://github.com")
# Response.history 是一个 Response 对象的列表，为了完成请求而创建了这些对象。这个对象列表按照从最老到最近的请求进行排序
print(res.history)

# 禁止重定向
res = requests.get("http://github.com", allow_redirects=False)
print(res.status_code)
print(res.history)

# 给 HEAD 开启重定向
res = requests.head("http://github.com", allow_redirects=True)
print(res.history)