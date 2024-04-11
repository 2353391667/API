# 获取图形验证码

# 导包
import requests

#发送请求
resqonse = requests.get(url="http://kdtx-test.itheima.net/api/captchaImage")

# 查看返回接口
print(resqonse.status_code)    # 查看返回状态码
print(resqonse.text)    # 查看返回数据的文本


