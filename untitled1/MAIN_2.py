# coding: utf8
import urllib.request as urllib2
import urllib.parse as urllib
import base64
import sys
import ast
import time
import csv
import sqlite3
conn = sqlite3.connect('example.db')


f = open('data_set.txt', 'a+')
z = open('text.txt','r')
tk=z.read()
z.close()
#f.write(str('id')+','+'meta1'+','+'meta2'+','+'meta3'+','+'meta4'+','+'meta5'+','+'meta6'+','+'vector'+"\r\n")
acc_token=tk
vector_info="/vectors/?random"
rez="/results/"
#request = u
url="https://slot-ml.ptsecurity.com/api/v1/users/"
urllib2.Request(url+acc_token+vector_info)


#print type(urllib2.urlopen(req).read())


def timer():
    while 1:
        try:
            data={}
            req = urllib2.Request(url+acc_token+vector_info)
            aa=ast.literal_eval(urllib2.urlopen(req).read())
            if "Mozilla\/" in aa['vector']:
                data['vector']=aa['id']
                data['class']="1"
                data1 = urllib.urlencode(data)
            #Mozilla\/
                req = urllib2.Request(url+acc_token+rez, data1)
                response = urllib2.urlopen(req)
                result = response.read()
                bb=ast.literal_eval(result)
                if bb["message"]=="class was stored successfully":
                    blue_ten="1"
                else:
                    blue_ten="0"
                f.write(str(aa['vector'])+"\r\n")
                print (str(aa['id']))
                return('red')
         
        except:
            f.write('0'+"\r\n")
            return('green')
    time.sleep(0.01)

timer()


  
