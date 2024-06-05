# -*- coding: utf-8 -*-
# @Time : 2022/7/19 10:59
# @Author : 祁传睿
# @File : 4_urllib_ajax_get.py
# @Software: PyCharm

import urllib.request
import urllib.parse

# 浏览器headers出现 x-request-with 则使用 ajax

# 获取豆瓣电视剧第一页数据并保存
def doubanone():
    url = 'https://movie.douban.com/j/search_subjects?type=tv&tag=%E5%9B%BD%E4%BA%A7%E5%89%A7&sort=recommend&page_limit=20&page_start=0'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
    }
    request = urllib.request.Request(url=url,headers=headers)
    response = urllib.request.urlopen(request)
    content = response.read().decode('utf-8')
    # print(content)
    # open方法默认使用gbk，若使用汉字需要指定encoding='utf-8'
    with open('douban1.json','w',encoding='utf-8') as fp:
        fp.write(content)

#下载10页
def doubanten():
    # 下滑使用ajax
    url = 'https://movie.douban.com/j/search_subjects?type=tv&tag=%E5%9B%BD%E4%BA%A7%E5%89%A7&sort=recommend&page_limit=200&page_start=0'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
    }
    request = urllib.request.Request(url=url, headers=headers)
    response = urllib.request.urlopen(request)
    content = response.read().decode('utf-8')
    # print(content)
    # open方法默认使用gbk，若使用汉字需要指定encoding='utf-8'
    with open('douban10.json', 'w', encoding='utf-8') as fp:
        fp.write(content)



# 下载多页
def  doubandown(page):
    base_url = 'https://movie.douban.com/j/search_subjects?type=tv&tag=%E5%9B%BD%E4%BA%A7%E5%89%A7&sort=recommend&'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
    }
    data = {
        'page_limit':20,
        'page_start':(page - 1) * 20,
    }
    data = urllib.parse.urlencode(data)
    url = base_url + data
    print(url)
    request = urllib.request.Request(url=url,headers=headers)
    return request

def get_content(request):
    response = urllib.request.urlopen(request)
    content = response.read().decode('utf-8')
    return content

def downdouban(page,content):
    with open('douban_'+ str(page) + '.json', 'w', encoding='utf-8') as fp:
        fp.write(content)


# 程序入口
if __name__ == '__main__':
    start_page = int(input('输入起始页码：'))
    end_page = int(input('输入结束页码：'))
    for page in range(start_page,end_page+1):
        request = doubandown(page)
        content = get_content(request)
        downdouban(page,content)


