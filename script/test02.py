# 登录

# 导包
import requests

# 发送请求
url = "http://kdtx-test.itheima.net/api/login"
headers_data = {
    "Content-Type": "application/json"
}

json1 = {
    "username": "admin",
    "password": "HM_2023_test",
    "code": 2,
    "uuid": "712b4dd0b86a4114abce53df1a536bfd"
}

resqonse = requests.post(url=url, headers=headers_data, json=json1)

# 查看返回结果
print(resqonse.status_code)
print(resqonse.json())