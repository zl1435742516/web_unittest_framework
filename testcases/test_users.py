#!/user/bin/env python
# encoding: utf-8
'''

  @姓名:zl
  @file: test_users.py
  @time: 2022/3/28 18:57
  @desc:
 '''
import unittest
from objects.users_object import UserPage
import unittest
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from time import sleep
from objects.login_object import LoginPage
from config.config import driver_path,url,sheetname
from data.data import Datas
from log.log import logger
from selenium.webdriver.common.by import By

class TestLogin(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print('打开浏览器')
        e = Service(executable_path=driver_path)
        cls.driver = webdriver.Edge(service=e)
        cls.driver.maximize_window()
        cls.driver.get(url)
        cls.userpage = UserPage(cls.driver)
        cls.loginpage = LoginPage(cls.driver)

    @classmethod
    def tearDownClass(cls):
        print('关闭浏览器')
        cls.driver.quit()

    @classmethod
    def setUp(self):
        print('登陆系统')
        value_list = Datas().read_excel(sheetname[0])
        username = value_list[0][0]
        password = value_list[0][1]
        self.loginpage.input_username(username)
        self.loginpage.input_password(password)
        self.loginpage.click_login()
        sleep(1)

    @classmethod
    def tearDown(self):
        print('退出系统')
        sleep(3)
        self.loginpage.logout()


    def test_create_log_1(self):
        '''
        验证创建日志成功的测试用例
        '''
        print('执行第一个测试用例')
        self.userpage.click_log()
        sleep(1)
        self.userpage.click_new_log()
        self.userpage.input_new_headline('2')
        self.userpage.click_new_Selection()
        self.userpage.input_tag('9')
        self.userpage.input_new_content('张淋')
        self.userpage.click_confirm()
        sleep(1)
        try:
            self.assertIn(self.userpage.get_log_text(),'我的日志' )
            sleep(1)
            print("第一个测试用例创建失败")
            logger.info("验证创建日志成功的测试用例执行Passed")
        except:
            print("第一个测试用例成功创建")
            logger.info("验证创创建日志成功的测试用例执行Failed")



    def test_create_log_2(self):
        '''
        验证必填项未填的创建日志失败的测试用例
        '''
        print('执行第二个测试用例')
        self.userpage.click_log()
        sleep(1)
        self.userpage.click_new_log()
        self.userpage.input_new_headline('')
        self.userpage.click_new_Selection()
        self.userpage.input_tag('10')
        self.userpage.input_new_content('张淋')
        self.userpage.click_confirm_2()
        sleep(1)
        try:
            self.assertEqual('返回上一级', self.userpage.get_return_text())
            sleep(1)
            self.loginpage.logout()
            print("第一个测试用例成功创建")
            logger.info("验证必填项未填的创建日志失败的测试用例执行Passed")
        except:
            print("第一个测试用例创建失败")
            logger.info("验证必填项未填的创建日志失败的测试用例执行Failed")



    def test_classify_1(self):
        '''
        验证创建分类成功的测试用例
        '''
        print('执行第三个测试用例')
        self.userpage.click_log()
        sleep(1)
        self.userpage.click_new_log()
        self.userpage.click_classification(3)
        try:
            self.assertEqual('日志分类', self.userpage.get_classification_text())
            sleep(1)

            print("第一个测试用例创建失败")
            logger.info("验证创建分类成功的测试用例执行Passed")
        except:
            print("第一个测试用例创建成功")
            logger.info("验证创建分类失败的测试用例执行Failed")


    def test_classify_2(self):
        '''
        验证创建分类为空失败的测试用例
        '''
        print('执行第四个测试用例')
        self.userpage.click_log()
        sleep(1)
        self.userpage.click_new_log()
        self.userpage.click_classification_2('')
        try:
            self.assertEqual('取消', self.userpage.get_cancel_text())
            sleep(1)
            self.loginpage.logout()
            print("第二个测试用例创建失败")
            logger.info("验证创建分类为空失败的测试用例执行Passed")
        except:
            print("第二个测试用例创建成功")
            logger.info("验证创建分类为空失败的测试用例执行Failed")

    def test_edit_category_1(self):
        '''
        验证编辑分类成功的测试用例
        '''
        print('执行第五个测试用例')
        self.userpage.click_log()
        sleep(1)
        self.userpage.click_new_log()
        self.userpage.input_newclassify(4)
        self.userpage.click_delete_classify()
        sleep(1)
        try:
            self.assertEqual('取消', self.userpage.get_cancel_text())
            sleep(1)
            self.loginpage.logout()
            print("第一个测试用例编辑成功")
            logger.info("验证编辑分类成功的测试用例执行Passed")
        except:
            print("第一个测试用例编辑失败")
            logger.info("验证编辑分类成功的测试用例执行Failed")


    def test_edit_category_2(self):
        '''
        验证编辑分类为空失败的测试用例
        '''
        print('执行第六个测试用例')
        self.userpage.click_log()
        sleep(1)
        self.userpage.click_new_log()
        self.userpage.input_newclassify('')
        self.userpage.click_delete_classify()
        sleep(1)
        try:
            self.assertEqual('编辑', self.userpage.get_compile_text())
            sleep(1)
            self.loginpage.logout()
            print("第一个测试用例编辑失败")
            logger.info("验证编辑分类成功的测试用例执行Passed")
        except:
            print("第一个测试用例编辑成功")
            logger.info("验证编辑分类成功的测试用例执行Failed")

    def test_creat_photo_1(self):
        '''
        验证创建相册成功的测试用例
        '''
        print('执行第七个测试用例')
        self.userpage.click_photo_album()
        sleep(1)
        self.userpage.click_new_album()
        self.userpage.input_album_name('10')
        self.userpage.input_album_description('2')
        self.userpage.click_establish()
        try:
            self.assertEqual('切换上传方式', self.userpage.get_switch_to_text())
            sleep(1)
            self.loginpage.logout()
            print("第一个测试用例创建相册失败")
            logger.info("验证创建相册成功的测试用例执行Passed")
        except:
            print("第一个测试用例创建相册成功")
            logger.info("验证创建相册成功的测试用例执行Failed")

    def test_creat_photo_2(self):
        '''
        验证未填必填项创建相册成失败的测试用例
        '''
        print('执行第八个测试用例')
        self.userpage.click_photo_album()
        sleep(1)
        self.userpage.click_new_album()
        self.userpage.input_album_name('')
        self.userpage.input_album_description('2')
        self.userpage.click_establish_2()
        try:
            self.assertEqual('相册名称：', self.userpage.get_album_name_text())
            sleep(1)
            self.loginpage.logout()
            print("第一个测试用例创建相册成功")
            logger.info("验证创建相册成功的测试用例执行Passed")
        except:
            print("第一个测试用例创建相册失败")
            logger.info("验证创建相册成功的测试用例执行Failed")




    def test_upload_photos_1(self):
        '''
        验证上传相册成功的测试用例
        '''
        print('执行第九个测试用例')
        self.userpage.click_photo_album()
        self.userpage.click_upload_photo_album()
        self.userpage.click_choose_an()
        self.userpage.click_choose_an_album()
        self.userpage.click_switch_to()
        self.userpage.input_select_file(r'E:\桌面\test.png')
        try:
            self.assertEqual('编辑相册', self.userpage.get_edit_photo_text())
            sleep(1)
            self.loginpage.logout()
            print("第一个测试用例创建相册失败")
            logger.info("验证创建相册成功的测试用例执行Passed")
        except:
            print("第一个测试用例创建相册成功")
            logger.info("验证创建相册成功的测试用例执行Failed")


    def test_upload_photos_2(self):
        '''
        验证上传其他格式文件失败的测试用例
        '''
        print('执行第十个测试用例')
        self.userpage.click_photo_album()
        self.userpage.click_upload_photo_album()
        self.userpage.click_choose_an()
        self.userpage.click_choose_an_album()
        self.userpage.click_switch_to()
        self.userpage.input_select_file_2(r'E:\桌面\test.pdf')
        try:
            self.assertEqual('上传相片：', self.userpage.get_upload_photos_text())
            sleep(1)
            self.loginpage.logout()
            print("第一个测试用例上传其他格式文件成功")
            logger.info("验证上传其他格式文件失败的测试用例执行Passed")
        except:
            print("第一个测试用例上传其他格式文件失败")
            logger.info("验证创建相册成功的测试成功用例执行Failed")


    def test_create_group_1(self):
        '''
        验证创建群组成功的测试用例
        '''
        print('执行第十一个测试用例')
        self.userpage.click_group()
        self.userpage.click_create_group()
        self.userpage.input_name_of_the_group(8)
        self.userpage.input_group_to_introduce('1')
        self.userpage.input_group_tag('9')
        sleep(1)
        self.userpage.click_group_category()
        sleep(1)
        self.userpage.click_group_found()
        try:
            self.assertEqual('创建者', self.userpage.get_enter_text())
            sleep(1)
            self.loginpage.logout()
            print("第一个测试用例创建失败")
            logger.info("验证创建群组成功的测试用例执行Passed")
        except:
            print("第一个测试用例创建成功")
            logger.info("验证创建群组失败的测试用例执行Failed")

    def test_create_group_2(self):
        '''
        验证未填必填项创建群组失败的测试用例
        '''
        print('执行第十二个测试用例')
        self.userpage.click_group()
        self.userpage.click_create_group()
        self.userpage.input_name_of_the_group(' ')
        self.userpage.input_group_to_introduce('1')
        self.userpage.input_group_tag('9')
        sleep(1)
        self.userpage.click_group_category()
        sleep(1)
        self.userpage.click_group_found()
        try:
            alert_dialog = self.driver.driver.switch_to.alert
            content=alert_dialog.text
            alert_dialog.accept()
            self.assertIn('请认真填写每个选项',content)
            print("第二个测试用例验证失败")
            logger.info("验证未填必填项创建群组失败的测试用例执行Passed")
        except:
            print("第二个测试用例验证成功")
            logger.info("验证未填必填项创建群组失败的测试用例执行Failed")

    def test_group_search_1(self):
        '''
        验证搜索群组成功的测试用例
        '''
        print('执行第十三个测试用例')
        self.userpage.click_group()
        self.userpage.click_group_search()
        self.userpage.input_group_name('1')
        self.userpage.input_group_label('1')
        self.userpage.click_group_category_lookup()
        try:
            self.assertEqual('搜索群组', self.userpage.get_group_search_text())
            sleep(1)
            self.loginpage.logout()
            print("第一个测试用例搜索失败")
            logger.info("验证搜索群组成功的测试用例执行Passed")
        except:
            print("第一个测试用例成功搜索")
            logger.info("验证搜索群组失败的测试用例执行Failed")

    def test_group_search_2(self):
        '''
        验证搜索项为空的搜索群组失败的测试用例
        '''
        print('执行第十四个测试用例')
        self.userpage.click_group()
        self.userpage.click_group_search()
        self.userpage.input_group_name('')
        self.userpage.input_group_label('')
        self.userpage.click_group_category_lookup_2()
        try:
            self.assertEqual('查找群组', self.userpage.get_look_group_text())
            sleep(1)
            self.loginpage.logout()
            print("第二个测试用例搜索失败")
            logger.info("验证成功创建日志的测试用例执行Passed")
        except:
            print("第二个测试用例搜索成功")
            logger.info("验证创建日志失败的测试用例执行Failed")






    # def test_3(self):
    #     print('执行第三个测试用例')
