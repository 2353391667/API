from KTDX.api.course import CourseAPI
from KTDX.api.login import LoginAPI


class TestUpdate:

    def setup_method(self):
        # 初始化类对象
        self.course = CourseAPI()
        self.login = LoginAPI()
        # 获取验证码
        res_v = self.login.gei_verify_code()
        uuid = res_v.json().get("uuid")
        # 登录
        login_data = {
            "username": "admin",
            "password": "HM_2023_test",
            "code": 2,
            "uuid": uuid
        }
        res_l = self.login.login(json_data=login_data)
        self.token = res_l.json().get("token")

    def down_method(self):
        pass

    def test01_update_course(self):
        add_data = {
            "id":"93",
            "name": "测试开发提升课01",
            "subject": "6",
            "price": 899,
            "applicableperson": "2",
            "info": "测试开发提升课01"
        }
        res_up = self.course.add_course(test_data=add_data, token=self.token)
        print(res_up.json())
        # 断言接口的状态码
        assert 200 == res_up.status_code
        # 断言包含字符串
        assert "成功" in res_up.text
        # 断言code
        assert 200 == res_up.json().get("code")

    def test02_update_course(self):
        add_data = {
            "id":"93",
            "name": "测试开发提升课01",
            "subject": "6",
            "price": 899,
            "applicableperson": "2",
            "info": "测试开发提升课01"
        }
        res_up = self.course.add_course(test_data=add_data, token=None)
        print(res_up.json())
        # 断言接口的状态码
        assert 200 == res_up.status_code
        # 断言包含字符串
        assert "认证失败" in res_up.text
        # 断言code
        assert 401 == res_up.json().get("code")
