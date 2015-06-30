#!/usr/bin/env python
#coding:utf-8
#Generating a dictionary
#使用方法：python *.py 6 6 Six_nums_dict.txt
#其中第一个参数为最短长度，第二个参数为最长长度，第三个参数为存储路径（存储文件）

import sys
import string
import itertools

def get_strings():
	chars=string.printable[10:36]
	strings=[]
	for i in xrange(min,max+1):
		strings.append((itertools.product(chars,repeat=i),))
	return itertools.chain(*strings)

def make_dict():
	f = open(file,'a')
	for x in list_str:
		for y in x:
			f.write("".join(y))
			f.write('\n')
	f.close()
	print 'Done'

while True:
	if len(sys.argv)==4:
		try:
			min = int(sys.argv[1])
			max = int(sys.argv[2])
		except:
			print "wrong"
			sys.exit(0)
		if min <= max:
			list_str= get_strings()
			file=sys.argv[3]
			make_dict()
			sys.exit(0)
