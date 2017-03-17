#!/usr/bin/python3
import requests
import re

class main(object):
    def __init__(self):
        self.zz='<span class="title">(.*?)</span>' #单引号里面的是正则表达式
        self.url='http://daily.zhihu.com/' #网址
        self.req=requests.Session()
        self.headers={
            'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
'Accept-Encoding':'gzip, deflate, sdch',
'Accept-Language':'en-US,en;q=0.8',
'Cache-Control':'max-age=0',
'Connection':'keep-alive',
'Host':'daily.zhihu.com',
'Upgrade-Insecure-Requests':'1',
'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36'
        }
    def htmlparse(self):
        html=self.req.get(url=self.url,headers=self.headers)
        #print(html.text)
        pattern=re.compile(u'%s' %self.zz,re.S) 
        l=list()
        l=re.findall(pattern,html.text)
        for i in l:
            print(i)


if __name__=='__main__':
    m=main()
    m.htmlparse()