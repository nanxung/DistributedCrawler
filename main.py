#!/usr/bin/python3
#coding:utf8
import re
from parser import parser
from download import download
class main(object):
    def __init__(self):
        self.url=''
    
    def output(self):
        page=download(self.url)
        parser(page)
    

if __name__=='__main__':
    url=input('请输入网址：')
    m=main()
    m.url=url
    m.output()