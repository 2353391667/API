from KTDX.api.login import LoginAPI


class TestLoginAPI:

    def setup_method(self):
        # 实例化类对象
        self.login_api = LoginAPI()
        # 获取验证码
        response = self.login_api.gei_verify_code()
        self.uuid = response.json().get("uuid")

    def teardown_method(self):
        pass

    # 登录成功
    def test_login_01(self):
        login_data = {
            "username": "admin",
            "password": "HM_2023_test",
            "code": 2,
            "uuid": self.uuid
        }
        res_l = self.login_api.login(json_data=login_data)
        print(res_l.status_code)
        print(res_l.json())
        # 断言返回状态码为200
        assert 200 == res_l.status_code
        # 断言返回数据包含“成功”
        assert "成功" in res_l.text
        # 断言返回的json数据中code值
        assert 200 == res_l.json().get("code")


    # 登录失败（账号为空）
    def test_login_02(self):
        login_data = {
            "username": "",
            "password": "HM_2023_test",
            "code": 2,
            "uuid": self.uuid
        }
        res_l = self.login_api.login(json_data=login_data)
        print(res_l.status_code)
        print(res_l.json())
        # 断言返回状态码为200
        assert 200 == res_l.status_code
        # 断言返回数据包含“成功”
        assert "错误" in res_l.text
        # 断言返回的json数据中code值
        assert 500 == res_l.json().get("code")


        # 登录失败（账号不存在）
    def test_login_03(self):
        login_data = {
                "username": "Feiyang231",
                "password": "HM_2023_test",
                "code": 2,
                "uuid": self.uuid
            }
        res_l = self.login_api.login(json_data=login_data)
        # 断言返回状态码为200
        assert 200 == res_l.status_code
        # 断言返回数据包含“成功”
        assert "错误" in res_l.text
        # 断言返回的json数据中code值
        assert 500 == res_l.json().get("code")
