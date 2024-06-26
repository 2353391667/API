# 上传合同

# 导包
import requests

import KTDX.config as config


# 创建类
class ContractAPI:

    def __init__(self):
        # 课程添加接口
        # self.url_contract = "http://kdtx-test.itheima.net/api/common/upload"
        self.url_contract = f"{config.BASE_URL}/api/common/upload"
        # self.url_add_contract = "http://kdtx-test.itheima.net/api/contract"
        self.url_add_contract = f"{config.BASE_URL}/api/contract"

    # 上传合同请求
    def upload_contract(self, test_data, token):
        return requests.post(url=self.url_contract, files={"file": test_data}, headers={"Authorization": token})

    # 修改合同
    def add_contract(self, test_data, token):
        return requests.post(url=self.url_add_contract, json=test_data, headers={"Authorization": token})
