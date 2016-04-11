# -*- coding: utf-8 -*-
'''
Created on 2016年4月5日

@author: Moss
'''
import urllib2
import cookielib
url = "http://www.baidu.com"

print '测试第1种方法'
response1 = urllib2.urlopen(url)
innerHTML=response1.read()
print '状态码：'+str(response1.getcode())
print '网页内容长度：'+str(len(innerHTML))

print '测试第2种方法'
request = urllib2.Request(url)
request.add_header("user_agent","Mozilla/5.0")
response2 = urllib2.urlopen(request)
print '状态码：'+str(response2.getcode())
print '网页内容长度：'+str(len(response2.read()))

print '测试第3种方法'
cj = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
urllib2.install_opener(opener)
response3 = urllib2.urlopen(url)
print '状态码：'+str(response3.getcode())
print '网页内容长度：'+str(len(response3.read()))
print cj

print '网页内容：'+str(innerHTML)