# 接口封装
# requests.请求方法(yrl , data=None , json=None , headers=None , files=None)


# 导包
import requests
import KTDX.config as config


# 创建类
class LoginAPI:

    def __init__(self):
        # self.url_verify = "http://kdtx-test.itheima.net/api/captchaImage"
        self.url_verify = f"{config.BASE_URL}/api/captchaImage"
        # self.url_login = "http://kdtx-test.itheima.net/api/login"
        self.url_login = f"{config.BASE_URL}/api/login"
        # self.url_course = "http://kdtx-test.itheima.net/api/clues/course"
        self.url_course = f"{config.BASE_URL}/api/clues/course"

    # 获取验证码
    def gei_verify_code(self):
        return requests.get(url=self.url_verify)

    # 登录接口
    def login(self, json_data):
        return requests.post(url=self.url_login, json=json_data)

    # 查看课程接口
    def course(self,):
        return requests.post(url=self.url_course,)
