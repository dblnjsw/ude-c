import lxml
from lxml import etree
import time
import threading
import requests
import sys

class Thread_pa(threading.Thread):
    def __init__(self,key):
        threading.Thread.__init__(self)
        self.url=key

        # print(self.url)
        self.headers = {}
        self.headers['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36'

    def run(self):
        a = requests.get(self.url, headers=self.headers)
        ct = a.headers['content-type']
        a.encoding = {'encoding': 'utf-8'}

        html = etree.HTML(a.text, etree.HTMLParser())
        timer = html.xpath('//span[@class="timer"]/text()')
        while timer!="0":
            print(timer)
            time.sleep(1)
            timer = html.xpath('//span[@class="timer"]/text()')

        url0 = html.xpath('//a[@class="btn btn-success btn-lg get-link disabled"]/@href')

        print(url0)


pc=Thread_pa(sys.argv[1])
pc.run()