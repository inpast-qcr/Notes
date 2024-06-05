# -*- coding: utf-8 -*-
# @Time : 2022/7/18 18:51
# @Author : 祁传睿
# @File : 3_urllib_postget.py
# @Software: PyCharm

import urllib.request
import urllib.parse
import json

# 将中文转为Unicode
def get_quote():
    # https://www.baidu.com/s?wd=%E9%9B%AA%E5%B1%B1
    url = 'https://www.baidu.com/s?wd='    # https有UA反爬
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
    }
    # 将中文转为Unicode
    name = urllib.parse.quote('雪山')
    print(name)
    url = url + name
    request = urllib.request.Request(url=url,headers=headers)    # 参数顺序，不能直接写url，self, url, data=None, headers={}
    response = urllib.request.urlopen(request)
    content = response.read().decode('utf-8')
    print(content)


# 有多个参数使用
def get_urlencode():
    # https://www.baidu.com/s?wd=雪山&user=inpast
    url = 'https://www.baidu.com/s?wd='
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
    }
    data = {
        'wd':'雪山',
        'user':'inpast'
    }
    name = urllib.parse.urlencode(data)
    url = url + name
    request = urllib.request.Request(url=url, headers=headers)
    response = urllib.request.urlopen(request)
    content = response.read().decode('utf-8')
    print(content)

# 简单翻译
def post_baidutrans():
    url = 'https://fanyi.baidu.com/sug'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
    }
    data = {
        'kw':'book'
    }
    # post请求参数必须编码，参数放在请求对象定制的参数中
    data = urllib.parse.urlencode(data).encode('utf-8')
    # 模拟请求响应
    request = urllib.request.Request(url=url,data=data, headers=headers)
    response = urllib.request.urlopen(request)
    content = response.read().decode('utf-8')
    # 将字节json转换为Unicode
    obj = json.loads(content)
    print(obj)

# 详细翻译
def post_baidutranslate():
    url = 'https://fanyi.baidu.com/v2transapi?from=en&to=zh'
    # 反爬cookie 主要获取request.headers中的cookie
    # 在headers中，遇到Accept-Encoding: gzip一定要注释，其他内容要不要无所谓
    headers = {
        # 'Accept': '*/*',
        # 'Accept-Encoding': ' gzip, deflate, br',
        # 'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
        # 'Acs-Token': '1658127608905_1658195320735_D2R/T3UAQMk4Lig4mAJiJYPFtvJ+f52gfBX6tc5k1s0/EZ+4JUpDsOypBp5c7f+/DX6loYaCyx/9FLfLCaJO6FCWaaacLHS9wrwzECEOkrlak/tuJoGtnmmCbyclGEjHPiOJ3qUWADRwX1c90hBhzpl6HbiKOGHeCz2y6BQRH54IQpVfYOaB16WzskyF55WYVHxY5e+nPyP1+6aXQxPh1iyfPjJhDIC+ITDuqQ/PgykdlPuv/uUfLQvJZ77se0CpSbVZ8jp553z8T9JSmsN67+bGayro3V7SVrZEo+JYtrQ=',
        # 'Connection': 'keep-alive',
        # 'Content-Length': '136',
        # 'Content-Type': ' application/x-www-form-urlencoded; charset=UTF-8',
        # 'Host': ' fanyi.baidu.com',
        # 'Origin': 'https://fanyi.baidu.com',
        # 'sec-ch-ua': ' ".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
        # 'sec-ch-ua-mobile': ' ?0',
        # 'sec-ch-ua-platform': ' "Windows"',
        # 'Sec-Fetch-Dest': ' empty',
        # 'Sec-Fetch-Mode': ' cors',
        # 'Sec-Fetch-Site': ' same-origin',

        # 'X-Requested-With': ' XMLHttpRequest',    Ajax判断条件
        # 'Referer': 'https://fanyi.baidu.com/',    做图片防盗链，判断当前路径是否是上一个路径进来的
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
        'cookie':'__yjs_duid=1_5995fd657325dae07f7de9c6fb0761131641261401822;av1_switch_v3=0;BA_HECTOR=ala42101808480al2k25rci41hd9rs517;BAIDUID=76284EEF4A180CF1220C79D7460BE6BF:FG=1;BAIDUID_BFESS=CD9694EEAB1B8BE6C18E03F87ECF10A4:FG=1;BDUSS=DA1bjBPcFBWRWJybVI5alZjZTlLYTVSQTJRMmdORnhwRn51aGJhWjBKcnhyc3BpRVFBQUFBJCQAAAAAABAAAAEAAADfFz77uf3IpbXEMjAxNsuuxr8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAPEho2LxIaNiN;BDUSS_BFESS=DA1bjBPcFBWRWJybVI5alZjZTlLYTVSQTJRMmdORnhwRn51aGJhWjBKcnhyc3BpRVFBQUFBJCQAAAAAABAAAAEAAADfFz77uf3IpbXEMjAxNsuuxr8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAPEho2LxIaNiN;BIDUPSID=76284EEF4A180CF12B3A9B0AF98700D8;H_WISE_SIDS=107317_110085_179345_180636_188741_194519_196426_197471_197711_199572_204917_208721_209202_209518_209568_210298_210321_210969_212296_212740_212797_212869_213044_213079_213158_213307_213352_214109_214130_214137_214142_214190_214790_215730_216047_216211_216451_216517_216618_216838_216883_216942_217167_217185_217868_218020_218350_218359_218445_218457_218538_218548_218566_218598_219244_219249_219252_219329_219363_219452_219548_219563_219667_219672_219712_219733_219737_219742_219816_219819_219845_219907_219943_219946_220067_220071_220279_220302_220334_220663_221107_221116_221118_221121_221143_221381_221382_8000076_8000122_8000139_8000149_8000161_8000169_8000180_8000184_8000186;H_WISE_SIDS_BFESS=107317_110085_179345_180636_188741_194519_196426_197471_197711_199572_204917_208721_209202_209518_209568_210298_210321_210969_212296_212740_212797_212869_213044_213079_213158_213307_213352_214109_214130_214137_214142_214190_214790_215730_216047_216211_216451_216517_216618_216838_216883_216942_217167_217185_217868_218020_218350_218359_218445_218457_218538_218548_218566_218598_219244_219249_219252_219329_219363_219452_219548_219563_219667_219672_219712_219733_219737_219742_219816_219819_219845_219907_219943_219946_220067_220071_220279_220302_220334_220663_221107_221116_221118_221121_221143_221381_221382_8000076_8000122_8000139_8000149_8000161_8000169_8000180_8000184_8000186;MCITY=-%3A;PSTM=1627270904;RT="z=1&dm=baidu.com&si=cv9sqr7a9kf&ss=l5qky0pi&sl=3&tt=3l3&bcn=https%3A%2F%2Ffclog.baidu.com%2Flog%2Fweirwood%3Ftype%3Dperf&ld=3mxr&ul=j1se&hd=j1t9";SE_LAUNCH=5%3A27635664_0%3A27635664;ZFY=iwu3b8SQtjLCQP1a8DdiM0:AWSGf1U09S0UBfM:AVL8OE:C;APPGUIDE_10_0_2=1;FANYI_WORD_SWITCH=1;HISTORY_SWITCH=1;REALTIME_TRANS_SWITCH=1;SOUND_PREFER_SWITCH=1;SOUND_SPD_SWITCH=1;'
    }

    data = {
        'from':'en',
        'to':'zh',
        'query':'spider',
        'transtype':'realtime',
        'simple_means_flag':'3',
        'sign':'63766.268839',
        'token':'fe39bdfc7aefe7c521046b09cb4f3a9d',
        'domain':'common',
    }
    # post请求参数必须编码，参数放在请求对象定制的参数中
    data = urllib.parse.urlencode(data).encode('utf-8')
    # 模拟请求响应
    request = urllib.request.Request(url=url,data=data, headers=headers)
    response = urllib.request.urlopen(request)
    content = response.read().decode('utf-8')
    # 将字节json转换为Unicode
    obj = json.loads(content)
    print(obj)

post_baidutranslate()

