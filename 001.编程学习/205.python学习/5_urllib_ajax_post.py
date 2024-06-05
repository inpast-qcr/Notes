# -*- coding: utf-8 -*-
# @Time : 2022/7/19 16:50
# @Author : 祁传睿
# @File : 5_urllib_ajax_post.py
# @Software: PyCharm

# 第1页
# http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=keyword
# cname:
# pid:
# keyword: 合肥
# pageIndex: 1
# pageSize: 10
#
# 第2页
# http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=keyword
# cname:
# pid:
# keyword: 合肥
# pageIndex: 2
# pageSize: 10

import urllib.request
import urllib.parse

def create_request(page):
    base_url = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=keyword'
    data = {
        'cname': '',
        'pid': '',
        'keyword': '合肥',
        'pageIndex': page,
        'pageSize': 10,
    }
    data = urllib.parse.urlencode(data).encode('utf-8')
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
    }
    request = urllib.request.Request(url=base_url, data=data ,headers=headers)
    return request

def get_content(request):
    response = urllib.request.urlopen(request)
    content = response.read().decode('utf-8')
    return content

def down_load(page,content):
    with open ('kfc_' + str(page) +'json','w',encoding='utf-8') as fp:
        fp.write(content)

if __name__ == '__main__':
    start_page = int(input('输入起始页码：'))
    end_page = int(input('输入结束页码：'))
    for page in range(start_page,end_page+1):
        request = create_request(page)
        content = get_content(request)
        down_load(page,content)
