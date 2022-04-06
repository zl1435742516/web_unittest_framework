#!/user/bin/env python
# encoding: utf-8
'''

  @姓名:zl
  @file: run.py
  @time: 2022/3/28 18:53
  @desc:
 '''
from BeautifulReport import BeautifulReport
import unittest
from config.config import cases_path,report_path

cases = unittest.defaultTestLoader.discover(start_dir= cases_path,\
                                          pattern='test*.py')
result = BeautifulReport(cases)
result.report(description='登录的测试报告', filename='第一轮测试结果',
              report_dir=report_path)
