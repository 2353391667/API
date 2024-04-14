from KTDX.api.course import CourseAPI
from KTDX.api.login import LoginAPI


class TestDelete:

    # 前置条件
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

    # 删除成功
    def test01_delete(self):
        res_d = self.course.delete_course(test_data=110, token=self.token)
        print(res_d.json())
        # 断言返回状态码
        assert 200 == res_d.status_code
        assert "成功" in res_d.text
        assert 200 == res_d.json().get("code")

    def test02_delete_not_id(self):
        res_d = self.course.delete_course(test_data=6661221, token=self.token)
        print(res_d.json())
        # 断言返回状态码
        assert 200 == res_d.status_code
        assert "失败" in res_d.text
        assert 500 == res_d.json().get('code')

    def test03_delete_not_login(self):
        res_d = self.course.delete_course(test_data=6661221, token=None)
        print(res_d.json())
        # 断言返回状态码
        assert 200 == res_d.status_code
        assert "认证失败" in res_d.text
        assert 401 == res_d.json().get('code')

