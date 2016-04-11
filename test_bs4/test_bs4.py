# -*- coding: utf-8 -*-
import bs4
from bs4 import BeautifulSoup
import re

html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

soup = BeautifulSoup(html_doc, 'html.parser', from_encoding='utf8') 

print '获取所有的链接'

links = soup.find_all('a')
for link in links:
    print '-节点名称:  ',link.name,'   -节点herf属性:  ',link['href'],'   -节点文字:  ',link.getText()

print '******'
print '只获取lacie'
link_node = soup.find('a', href="http://example.com/lacie")
print '-节点名称:  ',link_node.name,'   -节点herf属性:  ',link_node['href'],'   -节点文字:  ',link_node.getText()

print '******'
print '正字表达式-模糊匹配-包含ill'
link_node = soup.find('a', href=re.compile(r"ill"))
print '-节点名称:  ',link_node.name,'   -节点herf属性:  ',link_node['href'],'   -节点文字:  ',link_node.getText()

print '******'
print '获取p段落'
p_node = soup.find('p', class_="title")
print("class_='title'，因为class是关键字")
print '-节点名称:  ',p_node.name,'   -节点文字:  ',p_node.getText()







