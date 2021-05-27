import lxml
from lxml import etree
import threading
import requests
import sys
import json

class Thread_pa(threading.Thread):
    def __init__(self,key):
        threading.Thread.__init__(self)
        self.key=key
        self.url="https://coursecatalog.us/?s="+self.key

        # print(self.url)
        self.headers = {}
        self.headers['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36'

    def run(self):
        a = requests.get(self.url, headers=self.headers)
        ct = a.headers['content-type']
        a.encoding = {'encoding': 'utf-8'}

        html = etree.HTML(a.text, etree.HTMLParser())
        title = html.xpath('//h2[@class="entry-title h3"]/a/text()')
        cate = html.xpath('//span[@class="meta-category"]/a/text()')
        time = html.xpath('//span[@class="updated"]/text()')
        content = html.xpath('//div[@class="entry-content"]/p/text()')

        #分类cate处理
        str0 = 'All Tutorials'
        category=[]
        for i in range(0,len(cate)-1):
            if (cate[i+1]=='All Tutorials'):
                category.append(str0)
                str0 = 'All Tutorials'
            else:
                str0 = str0+'-'+cate[i+1]
        if(len(category)!=len(title)):
            category.append('All Tutorials')

        # f1=open('spring+hibernate'+'.txt', 'w')

        for i in range(0,len(title)):
            dict={'name':title[i].replace("\u2013","-"),'category':category[i],'upload_date':time[i],'describe':content[i].replace("\u2013","-")}
            str = json.dumps(dict)
            print(str)
            # f1.write(str+'\n')
        # f1.close()



pc=Thread_pa(sys.argv[1])

pc.run()