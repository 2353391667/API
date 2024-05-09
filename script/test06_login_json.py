import json
import pytest
from KTDX.api.login import LoginAPI
import KTDX.config as config


# json数据驱动
def build_data(json_file):
    # 定义外层数据结构框架
    case_data = []
    # 打开JSON文件
    with open(json_file, "r", encoding="UTF-8") as f:
        # 读取json文件中的数据
        json_data = json.load(f)
        for case in json_data:
            username = case.get("username")
            password = case.get("password")
            status = case.get("status")
            msg = case.get("msg")
            code = case.get("code")
            # 添加数据
            case_data.append((username, password, status, msg, code))
        # 返回数据
    return case_data


class TestLoginAPI:

    @pytest.fixture(autouse=True)
    def fun(self):
        self.login_api = LoginAPI()
        # 获取验证码
        response = self.login_api.gei_verify_code()
        self.uuid = response.json().get("uuid")

    # def setup_method(self):
        # 实例化类对象
        self.login_api = LoginAPI()
        # 获取验证码
        response = self.login_api.gei_verify_code()
        self.uuid = response.json().get("uuid")

    # def teardown_method(self):
        pass

    @pytest.mark.parametrize("username, password, status,msg,code",
                             build_data(json_file=f"{config.BASE_PATH}\\data\\login.json"))
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


if __name__ == '__main__':
    pytest.main()
