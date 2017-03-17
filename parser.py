#!/usr/bin/python3
#coding:utf8

import re
from urldata import urldata
def parser(page):
    parsers=re.compile(u'<a href="(.*?)">*?',re.S)
    l=list()
    l=re.findall(parsers,page)
    u=urldata()
    for i in l:
        u.setdata(i)
