# coding:utf8
from bs4 import BeautifulSoup
import re
import urlparse

class HtmlParser(object):

    def _get_new_urls(self, page_url, soup):
        new_urls = set()
        links = soup.find_all('a',href=re.compile(r"/view/\d+\.htm"))
        for link in links:
            new_url = link['href']
            new_full_url = urlparse.urljoin(page_url, new_url)
            new_urls.add(new_full_url)
        return new_urls

    def _get_new_data(self, page_url, soup):
        res_data = {}
        # url
        res_data['url'] = page_url
        # 网页中的相应部分
        '''
        <dd class="lemmaWgt-lemmaTitle-title">
            <h1>Python</h1>
            <a href="javascript:;" class="edit-lemma cmn-btn-hover-blue cmn-btn-28 j-edit-link" style="display: inline-block;"><em class="cmn-icon wiki-lemma-icons wiki-lemma-icons_edit-lemma"></em>编辑</a>
            <a class="lock-lemma" target="_blank" href="/view/10812319.htm" title="锁定"><em class="cmn-icon wiki-lemma-icons wiki-lemma-icons_lock-lemma"></em>锁定</a>
        </dd>
        '''
        # 获取标题
        title_node = soup.find("dd", class_="lemmaWgt-lemmaTitle-title").find("h1")
        res_data['title']=title_node.getText()
        # 获取简介
        # para
        summary_node = soup.find("div", class_="para")
        res_data['summary']=summary_node.getText()
        return res_data
        
    def parse(self ,page_url, html_cont):
        if page_url is None or html_cont is None:
            print("something wrong in htmlparse.py")
            return
        # 创建bs对象
        soup = BeautifulSoup(html_cont, 'html.parser', from_encoding='utf-8')
        new_urls = self._get_new_urls(page_url, soup)
        #print ("new_urls:%s"%new_urls)
        new_data = self._get_new_data(page_url, soup)
        #print ("new_data:%s"%new_data)
        return new_urls, new_data
    
    



