# 课程模块的封装

# 导包
import requests


# 创建类
class CourseAPI:

    def __init__(self):
        # 课程添加接口
        self.url_course = "http://kdtx-test.itheima.net/api/clues/course"

    # 添加课程请求
    def add_course(self, test_data, token):
        return requests.post(url=self.url_course, json=test_data, headers={"Authorization": token})
