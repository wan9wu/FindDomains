# FindDomains域名查找器
Find Unregistered Domains use net.cn API.
本程序用于批量查找没有被注册的域名。

#用法
需要保证电脑已安装python
在MAC下和ubuntu下测试python2.7运行正常

FindDomain.py
会根据Dictionarys目录下的字典文件逐一验证域名是非被注册。
未被注册的域名会存储在FindDomainLog.txt中。

GenDict.py
用于生成字典文件
使用方法：python GenDict.py 6 6 Six_nums_dict.txt
其中第一个参数为最短长度，第二个参数为最长长度，第三个参数为存储路径（存储文件）

