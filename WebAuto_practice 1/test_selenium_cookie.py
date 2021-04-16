import json
import time
import pytest
from selenium import webdriver


@pytest.fixture()
def weWork_open():
    """
    打开企业微信登录界面
    """
    driver = webdriver.Chrome()
    driver.get("https://work.weixin.qq.com/wework_admin/frame")
    yield driver

class Test_webWework:

        def test_cookie_login(self, weWork_open):
            self.driver = weWork_open

            # cookie注入
            with open('cookie.text') as fp:
                cookies = json.loads(fp.read())
                for i in cookies:
                    self.driver.add_cookie(i)
            self.driver.refresh()

            # 验证：点击通讯录
            try:
                self.driver.find_element_by_link_text('通讯录').click()
                time.sleep(5)
                self.driver.quit()
            except:
                print("Failed!!!")