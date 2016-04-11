# coding:utf8
class UrlManager(object):
    def __init__(self):
        # 存放未爬取的url
        self.new_urls=set()
        # 存取已爬取的url
        self.old_urls=set()
        
    # 添加一个新的url
    def add_new_url(self, url):
        # 判断新的url是否为空
        if url is None:
            return
        # 判断是否是全新的url，即是否在new_urls或者old_urls中
        if url not in self.new_urls and url not in self.old_urls:
            self.new_urls.add(url)
    
    # 添加批量新的url
    def add_new_urls(self, urls):
        if urls is None or len(urls)==0:
            return
        for url in urls:
            self.add_new_url(url)
            
    # 判断管理器中是否有新的待爬取的url
    def has_new_url(self):
        return len(self.new_urls) !=0

    # 从管理中获取一个新的url
    def get_new_url(self):
        new_url = self.new_urls.pop()
        self.old_urls.add(new_url)
        return new_url
    
    
    
    

    
    
    
    
    



