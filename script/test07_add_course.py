import pytest

from KTDX.api.course import CourseAPI
from KTDX.api.login import LoginAPI
import json


def add_data(json_file):
    # 定义外围数据结构
    course_data = []
    with open(json_file, "r", encoding="UTF-8") as f:
        f_data = json.load(f)
        for add_vulse in f_data:
            name = add_vulse.get("name")
            subject = add_vulse.get("subject")
            price = add_vulse.get("price")
            applicableperson = add_vulse.get("applicableperson")
            info = add_vulse.get("info")
            status = add_vulse.get("status")
            msg = add_vulse.get("mag")
            code = add_vulse.get("code")
            course_data.append((name, subject, price, applicableperson, info, status, msg, code))
    return course_data


# 创建类
class TestAddCourseAPI:

    # 前置条件
    def setup_method(self):
        # 实例化类
        self.add_course = CourseAPI()
        self.login = LoginAPI()
        # 获取验证码
        res_v = self.login.gei_verify_code()
        uuid = res_v.json().get('uuid')
        # 登录
        login_data = {
            "username": "admin",
            "password": "HM_2023_test",
            "code": 2,
            "uuid": uuid
        }
        res_l = self.login.login(json_data=login_data)
        # 获取登录的token
        self.token = res_l.json().get('token')

    def down_method(self):
        pass

    # 添加成功
    @pytest.mark.parametrize(("name,subject,price,applicableperson,info,status,msg,code"),add_data("../data/course.json"))
    def test01_add_course(self, name, subject, price, applicableperson, info, status, msg, code):
        add_data = {
            "name": name,
            "subject": subject,
            "price": price,
            "applicableperson": applicableperson,
            "info": info
        }
        res_add_true = self.add_course.add_course(test_data=add_data, token=self.token)
        print(res_add_true.status_code)
        # 断言返回的状态码
        assert status == res_add_true.status_code
        # 断言是否包含
        assert '成功' in res_add_true.text
        # 断言code是否返回200
        assert code == res_add_true.json().get("code")

    # 添加失败（未登录）
    def test02_add_course(self):
        add_data = {
            "name": "测试开发提升课01",
            "subject": "6",
            "price": 899,
            "applicableperson": "2",
            "info": "测试开发提升课01"
        }
        res_add_false = self.add_course.add_course(test_data=add_data, token=None)
        # 断言返回的状态码
        assert 200 == res_add_false.status_code
        # 断言是否包含
        assert "失败" in res_add_false.text
        # 断言code是否返回200
        assert 401 == res_add_false.json().get("code")
