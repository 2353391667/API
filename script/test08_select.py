from KTDX.api.course import CourseAPI
from KTDX.api.login import LoginAPI

class TestSelect:

    def setup_method(self):
        self.login = LoginAPI()
        self.select = CourseAPI()
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

    def test01_select_true(self):
        select_data = "?name=测试开发课程01"
        res_s = self.select.select_course(test_data=select_data,token=self.token)
        print(res_s.json())
        # 断言状态码
        assert 200 == res_s.status_code
        # 断言包含字符串
        assert "测试开发" in res_s.text
        # 断言返回code是否一致
        assert 200 == res_s.json().get("code")

    def test02_select_false(self):
        select_data = "?name=Feiyang231"
        res_s = self.select.select_course(test_data=select_data, token=None)
        print(res_s.json())
        # 断言状态码
        assert 200 == res_s.status_code
        # 断言包含字符串
        assert "失败" in res_s.text
        # 断言返回code是否一致
        assert 401 == res_s.json().get("code")



