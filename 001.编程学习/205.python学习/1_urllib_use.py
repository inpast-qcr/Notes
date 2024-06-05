# -*- coding: utf-8 -*-
# @Time : 2022/7/18 17:00
# @Author : 祁传睿
# @File : 1_urllib_use.py
# @Software: PyCharm

import urllib.request

# 获取页面源码
def get_webcontent():
    url = "http://www.baidu.com"    # 定义访问地址
    response = urllib.request.urlopen(url)     # 模拟浏览器向服务器发请求，response响应
    content = response.read().decode('utf-8')   #获取响应的页面源码，read()获取字节形式二进制数据（按字读），readlines()按行读，decode()解码
    print(content)

# response.getcode()    获取状态码
# response.geturl()    获取url地址
# response.getheaders()    获取响应头


# 下载
def download_web():
    url_page = "http://www.baidu.com"
    urllib.request.urlretrieve(url_page,"baidu.html")

def download_img():
    url_img = "https://bkimg.cdn.bcebos.com/pic/c2fdfc039245d688a094dff0a6c27d1ed31b24cb?x-bce-process=image/watermark,image_d2F0ZXIvYmFpa2UxMTY=,g_7,xp_5,yp_5/format,f_auto"
    urllib.request.urlretrieve(url_img,"雪山.jpg")

def download_video():
    url_video = "https://vd3.bdstatic.com/mda-jhts54s4cnp2ps84/sc/mda-jhts54s4cnp2ps84.mp4?v_from_s=hkapp-haokan-suzhou&auth_key=1658140641-0-0-cb5a905a6f5f17a5ba5290770e47e961&bcevod_channel=searchbox_feed&pd=1&cd=0&pt=3&logid=0441394886&vid=5209729320296203214&abtest=103525_2&klogid=0441394886"
    urllib.request.urlretrieve(url_video,"雪山.mp4")


# 字典快速加引号
'''
首先选择我们的头部内容，然后
ctrl+R
出现以下对话框，先选择右上角
regex
然后在上方输入框输入
(.*): (.*)
下方输入
'$1': '$2',
没错其实就是正则拉
再点击
replace all

'''

# post请求报错
'''
errno:997   cookie失效
errno:998   sign参数错误
errno:999   post未提交from,to参数
error:1000  需要翻译的字符串为空  # 记住，这个是error，也许是百度发现自己的errno拼错了吧
'''