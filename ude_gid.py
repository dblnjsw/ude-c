from selenium import webdriver
import time
import lxml
from lxml import etree
import threading
import requests
import re
import json
import linecache

max_line=158
start_id=831

def get_gid(g):
    wd.get(g)
    e=wd.find_element_by_class_name('btn-success')
    timer = wd.find_element_by_id('timer')
    while timer.text!='0':
        time.sleep(1)
    google_id=e.get_attribute('href')
    while google_id=='javascript: void(0)':
        time.sleep(0.5)
        google_id = e.get_attribute('href')
    return google_id
# 创建 WebDriver 对象，指明使用chrome浏览器驱动
wd = webdriver.Chrome()

f = open("sname.txt")               # 返回一个文件对象
fg = open("gid.txt","a")               # 返回一个文件对象
line = f.readline()               # 调用文件的 readline()方法
url='https://coursecatalog.us/'
id=start_id
headers = {}
headers['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36'
line=linecache.getline('sname.txt', start_id-id).strip()
while id!=start_id+max_line:
    print(url+line)


    a = requests.get(url+line[:-1], headers=headers)
    a.encoding = {'encoding': 'utf-8'}

    html = etree.HTML(a.text, etree.HTMLParser())

    # udemyURL
    patt='https://www.udemy.com/course/(.*?)/'
    s=re.search(patt,a.text)
    uid="/"
    if s:
        uid=s.group(1)

    gurl = html.xpath('//a[@class="mks_button mks_button_large squared"]/@href')
    gid=get_gid(gurl[0])
    dict = {'id': str(id), 'sname': line[:-1],'uid':uid, 'gid': gid}
    str0 = json.dumps(dict)
    with open("gid.txt","a") as fg:
        fg.write(str0+"\n")


    # try:
    #     print(uurl)
    # except:
    #     print(uurl)
    # # print(url0)
    print(id)
    id+=1
    line = linecache.getline('sname.txt', start_id+start_id-id).strip()
fg.close()
f.close()



