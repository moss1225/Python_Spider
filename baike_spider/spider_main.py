# coding:utf8
from baike_spider import html_downloader, url_manager, html_parser, html_output

#进行初始化
class SpiderMain(object):
    def __init__(self):
        self.urls = url_manager.UrlManager()
        self.downloader= html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.outputer = html_output.HtmlOutputer()
        
    def craw(self, root_url):
        #添加
        self.urls.add_new_url(root_url)
        #获取的第几个url
        count = 1
        while self.urls.has_new_url():
            #获取新url
            new_url = self.urls.get_new_url()
            print("craw %d:%s"%(count,new_url))
            #下载url
            html_cont = self.downloader.download(new_url)
            #获取页面中的多个url，和数据
            new_urls, new_data=self.parser.parse(new_url, html_cont)
            #将新的Url添加到Url管理器
            self.urls.add_new_urls(new_urls)
            #收集数据
            self.outputer.collect_data(new_data)
            if count == 10:
                break
            count = count + 1
        
        self.outputer.output_html()
            

#主函数
if __name__ == "__main__":
    root_url="http://baike.baidu.com/view/21087.htm"
    obj_spider = SpiderMain()
    obj_spider.craw(root_url)
    #crew方法抓取url
    
    
    
    
    
    
    
    
    
    
    
    
    
    