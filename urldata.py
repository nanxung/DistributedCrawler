#!/usr/binpython3
#coding:utf8
import redis
import bloomfilter


class urldata(object):
    def __init__(self):
        self.r=redis.Redis(host='localhost',port=6379)

    def setdata(self,url):
        #""" 第一次运行时会显示 not exists!，之后再运行会显示 exists! """
        bf = bloomfilter.BloomFilter()
        if bf.isContains(url):   # 判断字符串是否存在
            print('exists!')
        else:
            self.r.sadd('url1',url)
            bf.insert(url)
        
# if __name__=='__main__':
#     u=urldata()
#     u.setdata()
#     l=u.r.smembers('url1')
#     print(l)
