# -*- coding: utf-8 -*-
# @Time : 2022/7/18 18:12
# @Author : 祁传睿
# @File : 2_urllib_请求对象的定制.py
# @Software: PyCharm

import urllib.request

# url组成
# http://www.baidu.com/s?wd=雪山
# http/https    www.baidu.com    80    s    wd=雪山    #
# 协议           主机             端口   路径  参数       锚点
# http:80    https:443

def get_webcontent():
    # User-Agent: Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Mobile Safari/537.36
    url = "https://www.baidu.com"    # https有UA反爬
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
    }
    # 请求对象的定制，urlopen不能存字典，能存请求对象
    request = urllib.request.Request(url=url,headers=headers)    # 参数顺序，不能直接写url，self, url, data=None, headers={}
    response = urllib.request.urlopen(request)
    content = response.read().decode('utf-8')
    print(content)

get_webcontent()