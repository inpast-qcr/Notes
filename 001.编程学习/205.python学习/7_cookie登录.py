# -*- coding: utf-8 -*-
# @Time : 2022/7/22 16:20
# @Author : 祁传睿
# @File : 7_cookie登录.py
# @Software: PyCharm

import urllib.request

url = "https://weibo.cn/6626609124/info"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
    'cookie':'_T_WM=716f45e43e42838604b56e9f5250de27;ALF=1659777151;SCF=Ai-0V0k2jU7dDKHieD-RPATAFEU54aT1PgTN6K9cRqtqOw_3c4uki75bobw_R9t0wgN4FRAK_tc9U-xZqna2cXc.;SSOLoginState=1658478110;SUB=_2A25P3i5ODeRhGeBI6VQX8CfNyTiIHXVtILIGrDV6PUJbktANLWemkW1NRoEABghlT6bAOTQrMucSZCRijThhEtqZ;SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WhF_vxvwuo-eT1UOdyn5vBi5NHD95QcSozcSo54eKzXWs4DqcjMi--NiK.Xi-2Ri--ciKnRi-zNSoqESoq71K2ES5tt;',
}
request = urllib.request.Request(url=url, headers=headers)
response = urllib.request.urlopen(request)
content = response.read().decode('utf-8')
# 个人信息页面是‘utf-8’但报错是因为反爬跳转登录页面是'gb2312'
# content = response.read().decode('utf-8')
# UnicodeDecodeError: 'utf-8' codec can't decode byte 0xb5 in position 672: invalid start byte
# print(content)

with open('weibo.html','w',encoding='utf-8') as fp:
    fp.write(content)