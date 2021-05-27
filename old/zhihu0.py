import requests
import lxml
from lxml import etree
import sqlalchemy
import sqlite3
import os
import threading
import time
import datetime


# ans_url='https://www.zhihu.com/question/307719606'
#
# headers={}
# headers['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36'
# a=requests.get(ans_url,headers=headers)
# ct=a.headers['content-type']
# a.encoding={'encoding':'utf-8'}
#
# html=etree.HTML(a.text,etree.HTMLParser())
# result=html.xpath('//strong[@class="NumberBoard-itemValue"]/text()')
# ann=html.xpath('//h4[@class="List-headerText"]/span/text()')
# title=html.xpath('//h1[@class="QuestionHeader-title"]/text()')
# print(result)

class Thread_pa(threading.Thread):
    def __init__(self,id):
        threading.Thread.__init__(self)
        self.threadID = id
        self.qu_url = 'https://www.zhihu.com/question/' + str(id)
        self.name='q'+str(id)
        self.headers={}
        self.headers['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36'

        self.conn = sqlite3.connect("db_init.db")
        self.cursor = self.conn.cursor()

        #判断该问题id是否存在，不存在则注册
        sql2="select count(*)  from questions where id = "+str(id)
        self.cursor.execute(sql2)
        val=self.cursor.fetchall()
        if val[0][0] is 0:
            sql1="insert into questions (id) values (?)"
            sql = "create table "+self.name+" (ans_n integer , foc_n integer , bro_n integer , current_date datetime)"
            self.cursor.execute(sql)
            self.cursor.execute(sql1,(id,))
            self.conn.commit()



    def run(self):
        while 1:
            a = requests.get(self.qu_url, headers=self.headers)
            ct = a.headers['content-type']
            a.encoding = {'encoding': 'utf-8'}

            html = etree.HTML(a.text, etree.HTMLParser())
            result = html.xpath('//strong[@class="NumberBoard-itemValue"]/text()')
            ann = html.xpath('//h4[@class="List-headerText"]/span/text()')
            title = html.xpath('//h1[@class="QuestionHeader-title"]/text()')

            sql = "insert into "+self.name+" (ans_n,foc_n,bro_n,current_date) values (?,?,?,?)"
            self.cursor.execute(sql,(ann[0].replace(',',''),result[0].replace(',',''),result[1].replace(',',''),datetime.datetime.now()))
            self.conn.commit()
            print(self.name+" get!")
            time.sleep(0.5)





if not os.path.isfile('db_init.db'):
    conn = sqlite3.connect("db_init.db")
    cursor = conn.cursor()
    sql = "create table questions (id integer primary key, title nvarchar(50))"
    cursor.execute(sql)
t1=Thread_pa(377943825)
t1.run()
conn = sqlite3.connect("db_init.db")
cursor = conn.cursor()
sql="select * from questions"
cursor.execute(sql)
val=cursor.fetchall()
print(val)
time.sleep(10000)


