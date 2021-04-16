# import json
import time
from selenium import webdriver

def is_elementExist(browser, xpath):
    """判断元素是否存在"""
    flag = True
    try:
        browser.find_element_by_xpath(xpath)
        return flag
    except:
        flag = False
        return flag


def test_reusebrowser():
    """
    实现复用浏览器
    """
    options = webdriver.ChromeOptions()
    options.debugger_address = "127.0.0.1:9222"
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(3)

    # 打开企业微信网页，第一次登录手动
    driver.get("https://work.weixin.qq.com/")
    driver.find_element_by_xpath('//*[@class="index_top_operation_loginBtn"]').click()

    # 验证成功进入登录页面，有导航栏,点击进入通讯录
    assert is_elementExist(driver, '//nav[@class="frame_nav"]')
    driver.find_element_by_link_text('通讯录').click()
    time.sleep(3)
    driver.quit()

    # 获取cookie
    # cookie = driver.get_cookies()
    # with open("cookie.text", 'w') as fp:
    #     json.dump(cookie, fp)


