import requests

""" 响应内容 """
res = requests.get("https://api.github.com/events", verify=False)
print(res.text)

""" 解码 """
# Requests 会自动解码来自服务器的内容。大多数 unicode 字符集都能被无缝地解码
print(res.encoding)  # 查看使用的编码：utf-8
res.encoding = "ISO-8859-1"  # 指定编码，这样res.text时，就会使用指定的编码进行解码

""" 二进制响应内容 """
res = requests.get("https://api.github.com/events", verify=False)
print(res.content)
# Requests 会自动为你解码 gzip 和 deflate 传输编码的响应数据

""" json响应内容 """
res = requests.get("https://api.github.com/events", verify=False)
print(res.json())
# 注意，成功调用json()并不意味着响应成功，有时响应失败也会返回一个json，要检查请求是否成功，使用
print(res.raise_for_status())  # None,无错时返回None,有错时返回HttpError
print(res.status_code)  # 200

""" 原始响应内容 """
res = requests.get("https://api.github.com/events", verify=False)
print(res.raw)
print(res.raw.read(20))

# 保存到文件
with open("request_02_响应内容.txt", "wb") as f:
    for i in res.iter_content(1024):
        f.write(i)
