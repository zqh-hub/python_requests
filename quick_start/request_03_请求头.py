import requests

""" 定制请求头 """
url = "https://api.github.com/some/endpoint"
header = {"user-agent": "Chrome"}
res = requests.get(url, headers=header, verify=False)
print(res)
"""
注意: 定制 header 的优先级低于某些特定的信息源，例如：
    如果在 .netrc 中设置了用户认证信息，使用 headers= 设置的授权就不会生效。而如果设置了 auth= 参数，``.netrc`` 的设置就无效了。
    如果被重定向到别的主机，授权 header 就会被删除。
    代理授权 header 会被 URL 中提供的代理身份覆盖掉。
    在我们能判断内容长度的情况下，header 的 Content-Length 会被改写
"""
