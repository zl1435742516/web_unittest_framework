#!/user/bin/env python
# encoding: utf-8
'''

  @姓名:zl
  @file: users_object.py
  @time: 2022/3/28 18:58
  @desc:
 '''
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from time import sleep

class UserPage:
    def __init__(self,driver):
        self.log_elem = By.LINK_TEXT, '日志'
        self.new_log_elem = By.LINK_TEXT, '新建日志'
        self.headline_elem = By.NAME, 'blog_title'
        self.class_Selection_elem = By.XPATH, '//table[@class="form_table"]//table//option[1]'
        self.add_the_classification_elem = By.LINK_TEXT, '添加分类'
        self.new_sort_name_elem = By.CSS_SELECTOR, '#new_sort_name'
        self.ensure_elem = By.XPATH, '//table[@class="form_table"]//table//input[2]'
        self.classification_of_log_elem = By.LINK_TEXT, '日志分类'
        self.compile_elem = By.CLASS_NAME, 'log_edit_link'
        self.Fill_in_the_box_elem =By.CLASS_NAME,'small-text'
        self.delete_classify_elem = By.XPATH,'/html[1]/body[1]/table[1]/tbody[1]/tr[4]/td[2]/div[1]/a[2]'
        self.save_elem = By.XPATH,'//td[@class="td_b"]//input[1]'
        self.tag_elem = By.NAME, 'tag'
        self.content_elem = By.ID, 'KINDEDITORBODY'
        self.confirm_elem = By.XPATH, '//tr[8]//td[1]//input[1]'
        self.photo_album_elem=By.CLASS_NAME,'app_album'
        self.new_album_elem=By.LINK_TEXT,'新建相册'
        self.album_name_elem=By.NAME,'album_name'
        self.album_description_elem=By.ID,'album_information'
        self.establish_elem=By.NAME,'action'
        self.upload_photo_album_elem = By.LINK_TEXT,'上传相片'
        self.choose_an_album=By.ID,'album_name'
        self.choose_an_album_elem = By.XPATH,'//option[contains(text(),"10")]'
        self.switch_to_upload_elem = By.LINK_TEXT,'切换上传方式'
        self.select_file_elem = By.XPATH,'/html[1]/body[1]/form[1]/table[2]/tbody[1]/tr[1]/td[1]/input[1]'
        self.uploading_elem = By.NAME,'submit'
        self.confirms_elem = By.NAME,'action'
        self.group_elem = By.LINK_TEXT,'群组'
        self.create_a_group_elem = By.LINK_TEXT,'创建群组'
        self.name_of_the_group_elem = By.NAME,'group_name'
        self.group_to_introduce_elem = By.NAME,'group_resume'
        self.group_tag_elem = By.NAME,'tag'
        self.group_category_elem = By.NAME,'group_type_id'
        self.group_rests_elem = By.XPATH,'//select[@id="group_type"]//option[2]'
        self.group_found_elem = By.ID,'UploadButton'
        self.group_search_elem = By.LINK_TEXT,'搜索群组'
        self.group_name_elem = By.NAME,'group_name'
        self.group_label_elem = By.NAME,'tag'
        self.group_category_lookup_elem = By.NAME,'group_type_id'
        self.group_look_other_elem = By.XPATH, '//option[2]'
        self.group_find_elem = By.NAME,'submit'
        self.mylog_elem = By.LINK_TEXT, '我的日志'
        self.driver=driver
        self.ascertain_elem=By.CSS_SELECTOR,'#_ButtonCancel_0'
        self.creator_elem = By.XPATH,'//dd[4]//span[1]'
        self.return_elem = By.LINK_TEXT,'返回上一级'
        self.cancel_elem = By.XPATH,'//input[3]'
        self.look_group_elem = By.CLASS_NAME,'active'
        self.edit_photo_elem = By.XPATH,'/html[1]/body[1]/div[4]/dl[1]/dd[6]/a[1]'
        self.upload_photos_elem = By.XPATH,'/html[1]/body[1]/form[1]/table[1]/tbody[1]/tr[2]/th[1]'



    def click_log(self):
        # self.driver.find_element(*self.user_elem).clear()
        self.driver.find_element(*self.log_elem).click()

    def click_new_log(self):
        self.driver.switch_to.frame('frame_content')
        self.driver.find_element(*self.new_log_elem).click()

    def input_new_headline(self, headline):
        self.driver.find_element(*self.headline_elem).send_keys(headline)

    def click_new_Selection(self):
        self.driver.find_element(*self.class_Selection_elem).click()

    def click_classification(self, newname):
        self.driver.find_element(*self.add_the_classification_elem).click()
        self.driver.find_element(*self.new_sort_name_elem).send_keys(newname)
        self.driver.find_element(*self.ensure_elem).click()
        self.driver.switch_to.default_content()

    def click_classification_2(self, newname):
        self.driver.find_element(*self.add_the_classification_elem).click()
        self.driver.find_element(*self.new_sort_name_elem).send_keys(newname)
        self.driver.find_element(*self.ensure_elem).click()
        sleep(1)
        self.driver.switch_to.default_content()
        self.driver.find_element(*self.ascertain_elem).click()



    def input_newclassify(self,newclassify):
        self.driver.find_element(*self.classification_of_log_elem).click()
        self.driver.find_element(*self.compile_elem).click()
        self.driver.find_element(*self.Fill_in_the_box_elem).clear()
        self.driver.find_element(*self.Fill_in_the_box_elem).send_keys(newclassify)
        self.driver.find_element(*self.save_elem).click()

    def click_delete_classify(self):
        self.driver.find_element(*self.delete_classify_elem).click()
        alert_window = self.driver.switch_to.alert
        sleep(1)
        alert_window.dismiss()
        self.driver.switch_to.default_content()

    def input_tag(self,tag):
        self.driver.find_element(*self.tag_elem).send_keys(tag)

    def input_new_content(self, content):
        self.driver.switch_to.frame('KINDEDITORIFRAME')
        self.driver.find_element(*self.content_elem).send_keys(content)

    def click_confirm(self):
        sleep(1)
        self.driver.switch_to.default_content()
        js = 'var q=document.documentElement.scrollTop=1000'
        self.driver.execute_script(js)
        self.driver.switch_to.frame('frame_content')
        self.driver.find_element(*self.confirm_elem).click()
        sleep(1)
        self.driver.switch_to.default_content()
        js = "var q=document.documentElement.scrollTop=0"
        self.driver.execute_script(js)

    def click_confirm_2(self):
        sleep(1)
        self.driver.switch_to.default_content()
        js = 'var q=document.documentElement.scrollTop=1000'
        self.driver.execute_script(js)
        self.driver.switch_to.frame('frame_content')
        self.driver.find_element(*self.confirm_elem).click()
        self.driver.switch_to.default_content()
        js = 'var q=document.documentElement.scrollTop=1000'
        self.driver.execute_script(js)
        self.driver.find_element(*self.ascertain_elem).click()
        sleep(1)
        self.driver.switch_to.default_content()
        js = "var q=document.documentElement.scrollTop=0"
        self.driver.execute_script(js)

    def click_photo_album(self):
        self.driver.find_element(*self.photo_album_elem).click()

    def click_new_album(self):
        self.driver.switch_to.frame('frame_content')
        self.driver.find_element(*self.new_album_elem).click()

    def input_album_name(self, album_name):
        self.driver.find_element(*self.album_name_elem).send_keys(album_name)

    def input_album_description(self,album_description):
        self.driver.find_element(*self.album_description_elem).send_keys(album_description)

    def click_establish(self):
        self.driver.find_element(*self.establish_elem).click()
        self.driver.switch_to.default_content()

    def click_establish_2(self):
        self.driver.find_element(*self.establish_elem).click()
        self.driver.switch_to.default_content()
        self.driver.find_element(*self.ascertain_elem).click()

    def input_verify_password_frame(self):
        self.driver.find_element(*self.class_Selection_elem).click()

    def click_upload_photo_album(self):
        self.driver.switch_to.frame('frame_content')
        self.driver.find_element(*self.upload_photo_album_elem).click()

    def click_choose_an(self):
        self.driver.find_element(*self.choose_an_album).click()

    def click_choose_an_album(self):
        self.driver.find_element(*self.choose_an_album_elem).click()

    def click_switch_to(self):
        self.driver.find_element(*self.switch_to_upload_elem).click()

    def input_select_file(self,path):
        self.driver.find_element(*self.select_file_elem).send_keys(path)
        self.driver.find_element(*self.uploading_elem).click()
        self.driver.find_element(*self.confirms_elem).click()
        self.driver.switch_to.default_content()

    def input_select_file_2(self,path):
        self.driver.find_element(*self.select_file_elem).send_keys(path)
        self.driver.find_element(*self.uploading_elem).click()
        self.driver.switch_to.default_content()


    def click_group(self):
        self.driver.find_element(*self.group_elem).click()

    def click_create_group(self):
        self.driver.switch_to.frame('frame_content')
        self.driver.find_element(*self.create_a_group_elem).click()

    def input_name_of_the_group(self,groupname):
        self.driver.find_element(*self.name_of_the_group_elem).send_keys(groupname)

    def input_group_to_introduce(self,groupintroduce):
        self.driver.find_element(*self.group_to_introduce_elem).send_keys(groupintroduce)

    def input_group_tag(self,grouptag):
        self.driver.find_element(*self.group_tag_elem).send_keys(grouptag)

    def click_group_category(self):
        self.driver.find_element(*self.group_category_elem).click()
        self.driver.find_element(*self.group_rests_elem).click()

    def click_group_found(self):
        self.driver.find_element(*self.group_found_elem).click()
        self.driver.switch_to.default_content()




    def click_group_search(self):
        self.driver.switch_to.frame('frame_content')
        self.driver.find_element(*self.group_search_elem).click()

    def input_group_name(self,lookupname):
        self.driver.find_element(*self.group_name_elem).send_keys(lookupname)

    def input_group_label(self,lookuptag):
        self.driver.find_element(*self.group_label_elem).send_keys(lookuptag)

    def click_group_category_lookup(self):
        self.driver.find_element(*self.group_category_lookup_elem).click()
        self.driver.find_element(*self.group_look_other_elem).click()
        self.driver.find_element(*self.group_find_elem).click()
        self.driver.switch_to.default_content()

    def click_group_category_lookup_2(self):
        self.driver.find_element(*self.group_find_elem).click()
        self.driver.switch_to.default_content()

    def get_log_text(self):
        return self.driver.find_element(*self.mylog_elem).text

    def get_return_text(self):
        return self.driver.find_element(*self.return_elem).text

    def get_classification_text(self):
        return self.driver.find_element(*self.classification_of_log_elem).text

    def get_cancel_text(self):
        return self.driver.find_element(*self.cancel_elem).text

    def get_compile_text(self):
        return self.driver.find_element(*self.compile_elem).text

    def get_enter_text(self):
        return self.driver.find_element(*self.creator_elem).text

    def get_group_search_text(self):
        return self.driver.find_element(*self.group_search_elem).text

    def get_look_group_text(self):
        return self.driver.find_element(*self.look_group_elem).text

    def get_switch_to_text(self):
        return self.driver.find_element(*self.switch_to_upload_elem).text

    def get_edit_photo_text(self):
        return self.driver.find_element(*self.edit_photo_elem).text

    def get_album_name_text(self):
        return self.driver.find_element(*self.album_name_elem).text

    def get_upload_photos_text(self):
        return self.driver.find_element(*self.upload_photos_elem).text