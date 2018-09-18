# -*- coding: utf-8 -*-
"""
    model: baidu_image_url get

"""
import requests
import os
import re
import urllib.parse
import get_img
try:
    word = input('请选择搜索关键词 ：')
    val = {}
    val['word'] = word
    word = urllib.parse.urlencode(val)
except Exception as e:
    word = 'word=python'
base_url = 'https://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fm=result&fr=&sf=1&fmq=1536037517148_R&pv=&ic=0&nc=1&z=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&%s'%(word)
response = requests.get(base_url)
try:
    content = response.content.decode("utf-8", "ignore")
except UnicodeDecodeError as e:
    content = response.content
os.chdir(r'C:\Users\Admin\Desktop\python')
f = open('http.txt', 'a', encoding='utf8')
try:
    res = re.findall('"middleURL":"http[s]://[^\s]*\.[jpg]{3}|[png]{3}",$', content)
except Exception as e:
    res = re.findall('"middleURL":"http[s]://[^\s]*\.[jpg]{3}|[png]{3}",$', str(content, "gb2312", "ignore"))

# TODO: 成功，基本无bug，分页问题需解决

for i in res:
    f.write(i[13:]+'\n')
f.close()
state = input('Do You Want Download Now ? : (y/n) ')
if state.lower() == 'y':
    get_img.get_file()
else:
    print('Press Enter To Exit : ')
