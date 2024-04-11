# 导包
from KTDX.api.login import LoginAPI
from KTDX.api.course import CourseAPI
from KTDX.api.contract import ContractAPI
import requests


my_token = None
# 创建测试类
class TestContractBusiness:
    # 定义一个token对象

    def setup_method(self):
        # 实例化类对象
        self.login_api = LoginAPI()
        self.course = CourseAPI()
        self.contract = ContractAPI()

    def teardown_method(self):
        pass

    def test01_login_success(self):
        global my_token
        # 获取验证码
        res_v = self.login_api.gei_verify_code()
        print(res_v.status_code)
        print(res_v.json())
        # 获取UUID的数据
        re = res_v.json().get("uuid")

        # 登录
        login_data = {
            "username": "admin",
            "password": "HM_2023_test",
            "code": 2,
            "uuid": re
        }
        res_l = self.login_api.login(login_data)
        print(res_l.status_code)
        print(res_l.json())
        my_token = res_l.json().get("token")

    # 新增课程用例
    def test02_add_course(self):
        add_course_data = {
            "name": "测试开发提升课01",
            "subject": "6",
            "price": 899,
            "applicableperson": "2",
            "info": "测试开发提升课01"
        }
        cou = self.course.add_course(test_data=add_course_data, token=my_token)
        print(cou.status_code)
        print(cou.json())

    # 上传合同用例
    def test03_upload_contract(self):
        f = open("../data/abc.pdf", "rb")
        add_file = self.contract.upload_contract(test_data=f, token=my_token)
        print(add_file.status_code)
        print(add_file.json())

    # 新增合同
    def test04_add_contract(self):
        add_contract_data = {
            "name": "测试888",
            "phone": "13612345678",
            "contraNo": "Feiyang002",
            "subject": "6",
            "courseId": "12777",
            "chamnnel": "0",
            "activityId": 77,
            "fileName": "{{fileName}}"
        }
        add_contract = self.contract.add_contract(test_data=add_contract_data, token=my_token)
        print(add_contract.status_code)
        print(add_contract.json())

