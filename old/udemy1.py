import lxml
from lxml import etree
import threading
import requests
import sys

class Thread_pa(threading.Thread):
    def __init__(self,key):
        threading.Thread.__init__(self)
        self.key=key
        self.url="https://coursecatalog.us/"+self.key

        # print(self.url)
        self.headers = {}
        self.headers['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36'

    def run(self):
        a = requests.get(self.url, headers=self.headers)
        ct = a.headers['content-type']
        a.encoding = {'encoding': 'utf-8'}

        html = etree.HTML(a.text, etree.HTMLParser())
        url0 = html.xpath('//a[@class="mks_button mks_button_large squared"]/@href')

        print(url0)


pc=Thread_pa(sys.argv[1])
pc.run()