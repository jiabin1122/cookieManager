# -*- coding:utf-8 -*-
import yaml

def cookies_builder():
    with open("./account.yaml", "r") as f :
        inf = yaml.load(f)
        for key, value in inf.items():
            if key == "url" :
                url = value
            else:
                account = value
        print url
        print account
        return url,account

class Config(object):
    def __init__(self,path=None):
        self.path = path or './account.yaml'

    @property
    def url(self):
        with open("./account.yaml", "r") as f :
            inf = yaml.load(f)
            for key, value in inf.items():
                if key == "url" :
                    url = value
            return url

    @property
    def account(self):
        account =  list()
        with open("./account.yaml", "r") as f :
            inf = yaml.load(f)
            for key, value in inf.items():
                if key == "account" :
                    account = value
            return account

if __name__ == "__main__":
    cookies_builder()
