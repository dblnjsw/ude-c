# import lxml
# from lxml import etree
import threading
# import requests
import sys
import json
import datetime


class Thread_pa0(threading.Thread):
    maxPage=14
    def __init__(self):
        threading.Thread.__init__(self)
        self.pagen=1

        self.url="https://coursecatalog.us/category/all-tutorials/page/"

        # print(self.url)
        self.headers = {}
        self.headers['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36'

    def run(self):
        while self.pagen!=self.maxPage:
            a = requests.get(self.url+str(self.pagen), headers=self.headers)
            ct = a.headers['content-type']
            a.encoding = {'encoding': 'utf-8'}

            html = etree.HTML(a.text, etree.HTMLParser())
            title = html.xpath('//h2[@class="entry-title h3"]/a/text()')
            cate = html.xpath('//span[@class="meta-category"]/a/text()')
            time = html.xpath('//span[@class="updated"]/text()')
            content = html.xpath('//div[@class="entry-content"]/p/text()')
            sname=html.xpath('//h2[@class="entry-title h3"]/a/@href')


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

            f1=open('sname.txt', 'a')
            f2=open('all.txt','a')

            for i in range(0,len(sname)):
                f1.write(sname[i][25:-1]+'\n')
            f1.close()
            print(str(self.pagen)+' finished')
            self.pagen+=1





pc=Thread_pa0()

pc.run()

# d1 = datetime.datetime(2009, 3, 23)
# d2 = datetime.datetime(2009, 10, 7)
# dt=datetime.timedelta(days=195)
# d=d1+dt
# print(type(d))
