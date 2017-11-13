# -*- coding:utf-8 -*-
import re

url = []
account = {}

def str_format(str):
     return str.replace("\n", "").strip()


def cookies_builder():
    with open("./account.txt", "r") as f :
        for item in f.readlines():
            line = item.split(":",1)
            if line[0].find("url") != -1:
                url.append(str_format(line[1]))
            elif line[0].find("user") != -1:
                account[str_format(line[1].split(",")[0])] = str_format(line[1].split(",")[1])
        print url
        print account
        return url,account

class Config(object):
    def __init__(self,path=None):
        self.path = path or './account.txt'

    @property
    def url(self):
        url  = list()
        with open("./account.txt", "r") as f :
            for item in f.readlines():
                line = item.split(":")
                if line[0].find("url") != -1:
                    url.append(str_format(line[1]))

        return  url

    @property
    def account(self):
        account =  list()
        with open("./account.txt", "r") as f :
            for item in f.readlines():
                line = item.split(":")
                if line[0].find("user") != -1:
                    account[str_format(line[1].split(",")[0])] = str_format(line[1].split(",")[1])
        return url

if __name__ == "__main__":
    cookies_builder()