import lxml
from lxml import etree
import threading
import requests




class Thread_pa0(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.pagen=2
        self.url="https://coursecatalog.us/category/all-tutorials/page/"

        # print(self.url)
        self.headers = {}
        self.headers['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36'

    def run(self):
        bad_url=[]
        while self.pagen!=85:
            a = requests.get(self.url+str(self.pagen), headers=self.headers)
            ct = a.headers['content-type']
            a.encoding = {'encoding': 'utf-8'}

            html = etree.HTML(a.text, etree.HTMLParser())
            im=html.xpath('//img[@class="attachment-herald-lay-b1 size-herald-lay-b1 wp-post-image"]/@src')
            sname=html.xpath('//h2[@class="entry-title h3"]/a/@href')

            for i in range(0,len(sname)):

                try:
                    pic = requests.get(im[i], headers=self.headers)
                    with open('./img/%s.jpg' % sname[i][25:-1], 'wb') as f:
                        f.write(pic.content)
                        f.flush()
                except Exception as e:
                    print(Exception, ':', e)
                    bad_url.append(im)
            print(str(self.pagen))
            self.pagen+=1

        print(bad_url)


# os.mkdir('./img')

pc=Thread_pa0()

pc.run()