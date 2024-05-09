# 用数据驱动
import pytest

from KTDX.api.login import LoginAPI

# 测试数据
login_data = [
    ("admin", "HM_2023_test", 200, "成功", 200),
    ("", "HM_2023_test", 200, "错误", 500),
    ("Feiyang231", "HM_2023_test", 200, "错误", 500),
]


class TestLoginAPI:

    def setup_method(self):
        # 实例化类对象
        self.login_api = LoginAPI()
        # 获取验证码
        response = self.login_api.gei_verify_code()
        self.uuid = response.json().get("uuid")

    def teardown_method(self):
        pass

    @pytest.mark.parametrize("username, password, status,msg,code", login_data)
    def test_login_01(self, username, password, status, msg, code):
        login_data = {
            "username": username,
            "password": password,
            "code": 2,
            "uuid": self.uuid
        }
        res_l = self.login_api.login(json_data=login_data)
        # 断言返回状态码为200
        assert status == res_l.status_code
        # 断言返回数据包含“成功”
        assert msg in res_l.text
        # 断言返回的json数据中code值
        assert code == res_l.json().get("code")
