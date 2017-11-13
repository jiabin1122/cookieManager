# coding: utf-8
__author__ = 'jiabin5'

from selenium import webdriver
from cookies_builder import cookies_builder
import json
import time


class JcloudLogin(object):
    def __init__(self, username,password):
        chromedriver = "C:\Program Files (x86)\chromedriver.exe"
        self.driver = webdriver.Chrome(chromedriver)
        self.url = "https://uc.jcloud.com/login?returnUrl=https://xdata.jcloud.com/console_page"
        self.user = username
        self.password = password

    def login(self):
        self.driver.maximize_window()
        self.driver.get(self.url)
        self.driver.implicitly_wait(10)
        self.driver.switch_to.frame("login_frame")
        self.driver.find_element_by_id("loginname").send_keys(self.user)
        self.driver.find_element_by_id("nloginpwd").send_keys(self.password)
        time.sleep(10)
        self.driver.find_element_by_id("paipaiLoginSubmit").click()
        self.driver.find_element_by_xpath("//li[1]/a/dl/dd").click()

    def get_cookies(self):
        cookies = self.driver.get_cookies()
        return cookies

    def goto(self,url):
        self.driver.get(url)
        return self

    def close(self):
        self.driver.close()


class AccountCookiesManager(object):
    def __init__(self):
        urls, accounts = cookies_builder()
        self.urls = urls
        self.accounts = accounts

    def save_cookies(self):
        for user,password in self.accounts.iteritems():
            jc_login = JcloudLogin(user,password)
            jc_login.login()
            try:
                for url in self.urls:
                    jc_login.goto(url)
                    cookies = jc_login.get_cookies()
                    self.save(user,url,cookies)
            except Exception,e:
                print  e
                jc_login.close()

    def save(self,account,url,cookies):
        data = {}
        for cookie in cookies:
            print  cookie
            name = cookie.get('name')
            value = cookie.get('value')
            data[name] = value
        url = url.split('//')[1].split('/')[0]
        with open('./cookies/{}_{}.json'.format(account,url),'w') as f:
            f.write(json.dumps(data))

if __name__ ==  '__main__':
    acm = AccountCookiesManager()
    acm.save_cookies()
