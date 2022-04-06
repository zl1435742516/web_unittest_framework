#!/user/bin/env python
# encoding: utf-8
'''

  @姓名:zl
  @file: login_object.py
  @time: 2022/3/28 18:57
  @desc:
 '''
from selenium.webdriver.common.by import By


class LoginPage:
    def __init__(self, driver):
        self.user_elem = By.NAME, 'login_email'
        self.pass_elem = By.NAME, 'login_pws'
        self.logbutton_elem = By.ID, 'loginsubm'
        self.logout_elem = By.LINK_TEXT, '退出'
        self.mypass_elem = By.LINK_TEXT, '忘记密码？'
        self.driver = driver

    def input_username(self, username):
        self.driver.find_element(*self.user_elem).clear()
        self.driver.find_element(*self.user_elem).send_keys(username)

    def input_password(self, password):
        self.driver.find_element(*self.pass_elem).clear()
        self.driver.find_element(*self.pass_elem).send_keys(password)

    def click_login(self):
        self.driver.find_element(*self.logbutton_elem).click()

    def logout(self):
        self.driver.find_element(*self.logout_elem).click()

    def get_link_text(self):
        return self.driver.find_element(*self.mypass_elem).text
