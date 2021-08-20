import requests

""" 上传文件 """
url = "http://httpbin.org/post"
files = {"file": open("request_02_响应内容.txt", "rb")}
res = requests.post(url, files=files)
print(res.text)

# 显式的设置文件名，文件类型，请求头     -----------> 没成功
url = "http://httpbin.org/post"
files = {"file": ("request.txt", open("request_02_响应内容.txt", "rb"), "text/plain", {"self_header": "mi"})}
res = requests.post(url, files=files)
print(res.text)
