# 存放被测试项目基本信息，如URL地址等
# 导包
import os

# 设置环境变量
BASE_URL = "http://kdtx-test.itheima.net"

# 获取项目的根目录
BASE_PATH = os.path.dirname(__file__)
print(BASE_PATH)