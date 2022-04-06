#!/user/bin/env python
# encoding: utf-8
'''

  @姓名:zl
  @file: test_login.py
  @time: 2022/3/28 18:56
  @desc:
 '''
import unittest
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from time import sleep
from objects.login_object import LoginPage
from config.config import driver_path,url,sheetname
from data.data import Datas
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from log.log import logger

class TestLogin(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print('打开浏览器')
        e = Service(executable_path=driver_path)
        cls.driver = webdriver.Edge(service=e)
        cls.driver.maximize_window()
        cls.driver.get(url)
        cls.loginpage=LoginPage(cls.driver)

    @classmethod
    def tearDownClass(cls):
        print('关闭浏览器')
        sleep(1)
        cls.driver.quit()

    @classmethod
    def setUp(self):
        print('登陆系统')

    @classmethod
    def tearDown(self):
        print('退出系统')


    def test_1(self):
        '''
        验证成功登陆的测试用例
        '''
        value_list=Datas().read_excel(sheetname[0])
        username=value_list[0][0]
        password=value_list[0][1]
        self.loginpage.input_username(username)
        self.loginpage.input_password(password)
        self.loginpage.click_login()
        sleep(1)
        try:
            self.assertIn("个人首页-聚易社区", self.driver.title)
            sleep(1)
            self.loginpage.logout()
            print("第一个测试用例成功登陆")
            logger.info("验证成功登陆的测试用例执行Passed")
        except:
            print("第一个测试用例登陆失败，未进入正确的页面")
            logger.info("登陆失败，未进入正确的页面用例执行Failed")




    def test_2(self):
        '''
        验证错误的密码登陆失败的测试用例
        '''
        value_list = Datas().read_excel(sheetname[0])
        username = value_list[1][0]
        password = value_list[1][1]
        self.loginpage.input_username(username)
        self.loginpage.input_password(password)
        self.loginpage.click_login()
        sleep(1)
        try:
            self.assertEqual("忘记密码？", self.loginpage.get_link_text())
            sleep(1)
            self.loginpage.logout()
            print("第二个测试用例验证失败")
            logger.info("验证错误的密码登陆失败的测试用例执行Passed")
        except:
            print("第二个测试用例验证成功")
            logger.info("验证错误的密码登陆失败的测试用例执行Failed")



    def test_3(self):
        '''
        验证不存在的用户登陆失败的测试用例
        '''
        value_list = Datas().read_excel(sheetname[0])
        username = value_list[2][0]
        password = value_list[2][1]
        self.loginpage.input_username(username)
        self.loginpage.input_password(password)
        self.loginpage.click_login()
        sleep(1)
        try:
            self.assertEqual("忘记密码？", self.loginpage.get_link_text())
            sleep(1)
            self.loginpage.logout()
            print("第三个测试用例验证失败")
            logger.info("验证存在的用户登陆失败的测试用例执行Passed")
        except:
            print("第三个测试用例验证成功")
            logger.info("验证存在的用户登陆失败的测试用例执行Failed")
        sleep(1)

    def test_4(self):
        '''
        验证密码为空格的登陆失败的测试用例
        '''
        value_list = Datas().read_excel(sheetname[0])
        username = value_list[3][0]
        password = value_list[3][1]
        self.loginpage.input_username(username)
        self.loginpage.input_password(password)
        self.loginpage.click_login()
        sleep(1)
        try:
            self.assertEqual("忘记密码？", self.loginpage.get_link_text())
            sleep(1)
            self.loginpage.logout()
            print("第六个测试用例验证失败")
            logger.info("验证密码为空格的登陆失败的测试用例执行Passed")
        except:
            print("第六个测试用例验证成功")
            logger.info("验证密码为空格的登陆失败的测试用例执行Failed")


    def test_5(self):
        '''
        验证用户为空格的登陆失败的测试用例
        '''
        value_list = Datas().read_excel(sheetname[0])
        username = value_list[4][0]
        password = value_list[4][1]
        self.loginpage.input_username(username)
        self.loginpage.input_password(password)
        self.loginpage.click_login()
        sleep(1)
        try:
            self.assertEqual("忘记密码？", self.loginpage.get_link_text())
            sleep(1)
            self.loginpage.logout()
            print("第七个测试用例验证失败")
            logger.info("验证用户为空格的登陆失败的测试用例执行Passed")
        except:
            print("第七个测试用例验证成功")
            logger.info("验证用户为空格的登陆失败的测试用例执行Failed")

if __name__=='__main__':
    unittest.main()
