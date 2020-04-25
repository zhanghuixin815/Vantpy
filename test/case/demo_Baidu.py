# -*- coding: utf-8 -*-
import sys
sys.path.append('../')
from test.page.BaiduPage import BaiduPage
from test.case.case_modle import *


class BaiduCase(model):

    def test_baidu1(self):
        baidu = BaiduPage(self.driver)
        baidu.input_baidu_text('selenium')
        baidu.click_baidu_btn()
        baidu.get_screent_img("baidu")
        try:
            self.assertIn('selenium',self.driver.title())
            print('test pass')
        except Exception as e:
            print('test fail',format(e))
