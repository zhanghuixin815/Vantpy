# -*- coding:utf-8 -*-

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from utils.config import Config
from utils.logger import Logger

logger = Logger(logger="BrowserDriver").getlog()

class BrowserDriver(object):
    path = './drivers/'#这是获取相对路径的方法
    chrome_driver_path = path + 'chromedriver.exe'

    def __init__(self,driver):
        self.driver = driver
        self.c = Config()

    def openbrowser(self,driver):
        browser = self.c.get("brwserType").get("browserName")
        logger.info("选择的浏览器为: %s 浏览器" % browser)
        url = self.c.get('ptahUrl').get('URL')
        logger.info("打开的URL为: %s" % url)
        chrome_options = Options()
        chrome_options.add_argument('--no-sandbox')  # 解决DevToolsActivePort文件不存在的报错
        chrome_options.add_argument('--start-maximized')  # 指定浏览器分辨率
        chrome_options.add_argument('--disable-gpu')  # 谷歌文档提到需要加上这个属性来规避bug
        chrome_options.add_argument('--hide-scrollbars')  # 隐藏滚动条, 应对一些特殊页面
        # chrome_options.add_argument('--headless')  # 浏览器不提供可视化页面. linux下如果系统不支持可视化不加这条会启动失败
        chrome_options.add_argument('--disable-extensions')
        chrome_options.add_argument('lang=zh_CN.UTF-8')
        chrome_options.binary_location = 'D:/Program Files (x86)/Google/Chrome/Application/chrome.exe'
        driver = webdriver.Chrome(options=chrome_options,executable_path=self.c.driver_ptah())
        logger.info("启动谷歌浏览器")
        driver.get(url)
        logger.info("打开URL: %s" % url)
        driver.maximize_window()
        logger.info("全屏当前窗口")
        driver.implicitly_wait(5)
        logger.info("设置5秒隐式等待时间")
        return driver

    def quit_browser(self):
        logger.info("关闭浏览器")
        self.driver.quit()

