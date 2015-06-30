#!/usr/bin/env python
#coding:utf-8

import sys
import os
import urllib
import time


Api = 'http://pandavip.www.net.cn/check/check_ac1.cgi?domain='
Prefix = ''
Suffix = ['.com']
Dictionarys = os.listdir("Dictionarys")
Output = "FindDomainLog.txt"

if Dictionarys[0].find(".") >= 0:#删除掉系统隐藏文件
    del Dictionarys[0]


print "Open Dictionary."
for ASuffix in Suffix:
    for Dictionary in Dictionarys:
        Thisline = 0 #防止程序中间出错，定时记录进度
        Dictionary = os.path.join("Dictionarys",Dictionary)
        print Dictionary
        dict = open(Dictionary,"r")
        for x in dict.readlines():
            x = x.strip()
            Thisline += 1
            url = ''.join([Api,Prefix,x,ASuffix])
            data = urllib.urlopen(url).read()
            if data.find('exists')>0:
                print ''.join([Prefix,x,ASuffix,' is a bed domain name.'])
                time.sleep(2)
                continue
            if data.find('available')>0:
                log = open(Output, "a")
                log.write(''.join([Prefix,x,ASuffix,"  字典行数：",str(Thisline),
                    "  字典名称:",Dictionary,"  发现时间",
                    time.strftime('%Y-%m-%d %H:%M:%S --%x--%X', time.localtime())]))
                log.write("\n")
                log.close()
                print ''.join([Prefix,x,ASuffix,' is a gooooooooooooooooooooood domain name.'])
                continue
            print 'error! error! error! error! error! error! error! error! '
            print '\a' * 10
