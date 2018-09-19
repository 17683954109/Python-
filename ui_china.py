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
    val['keywords'] = word
    word = urllib.parse.urlencode(val)
except Exception as e:
    word = 'word=python'
headers = {'Accept': '*/*',
           'Accept-Language': 'zh-CN,en;q=0.8',
           'Cache-Control': 'max-age=0',
           'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36',
           'Connection': 'keep-alive',
           'Referer': 'http://www.baidu.com/'
           }


def get_url(page, words):
    base_url = 'http://s.ui.cn/index.html?p=%d&%s&type=project' % (page, words)
    response = requests.get(base_url, headers)
    try:
        content = response.content.decode("utf-8", "ignore")
    except UnicodeDecodeError as s:
        content = response.content
    os.chdir(r'/home/coding/workspace/PyWeb') # TODO: 此处路径请自行修改
    f = open('http.txt', 'a', encoding='utf8')
    try:
        res = re.findall('data-original="http[s]?://[^\s]*\.[jpg]{3}|[png]{3}"\s$', content)
    except Exception as e:
        res = re.findall('data-original="http[s]?://[^\s]*\.[jpg]{3}|[png]{3}"\s$', str(content, "gb2312", "ignore"))
    for i in res:
        f.write(i[15:] + '\n')
    f.close()

# TODO: 失败，存在Cookie 检测

for i in range(1, 11):
    get_url(i, word)
state = input('Do You Want Download Now ? : (y/n) ')
if state.lower() == 'y':
    get_img.get_file()
else:
    print('Press Enter To Exit : ')
