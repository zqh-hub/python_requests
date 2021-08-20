import requests

""" 发送cookie """
url = "http://httpbin.org/cookies"
cs = {"cookie_example_01": "test_01", "cookie_example_02": "test_02"}
res = requests.get(url, cookies=cs)
print(res.text)
""" 访问 """
print(res.cookies['example_cookie_name'])

""" cookie jar """
requests.cookies.RequestsCookiesJar()
