# -*- coding: utf-8 -*-
# @Time : 2022/7/22 16:08
# @Author : 祁传睿
# @File : 6_urllib_异常.py
# @Software: PyCharm

import urllib.request
import urllib.error
# url = "https://blog.csdn.net/forever_yq/article/details/491010691"
# HTTPError：url输入内容错误
# url = "https://xuexi.cn"
# URLError：输入不存在地址
url = "https://blog.csdn.net/forever_yq/article/details/49101069"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
}
try:
    request = urllib.request.Request(url=url, headers=headers)  # 参数顺序，不能直接写url，self, url, data=None, headers={}
    response = urllib.request.urlopen(request)
    content = response.read().decode('utf-8')
    print(content)
except urllib.error.HTTPError:
    print('http 错误')
except urllib.error.URLError:
    print('url 错误')