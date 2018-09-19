# -*- coding: utf-8 -*-
"""
    model: sogou_image_url get

"""
# 导入模块
import requests
import os
import re
import urllib.parse
val = {}
try:
    word = input('请输入搜索关键词 : ')
    val['query'] = word
    word = urllib.parse.urlencode(val)
except Exception as e:
    word = 'query=hua'
headers = {'Accept': '*/*',
           'Accept-Language': 'zh-CN,en;q=0.8',
           'Cache-Control': 'max-age=0',
           'User-Agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36",
           'Connection': 'keep-alive',
           'Referer': 'http://www.baidu.com/'}
base_url = "http://pic.sogou.com/pics?{}&w=05009900&p=40030500&_asf=pic.sogou.com&_ast=1537249444&sc=index&sut=2123&sst0=1537249444305".format(word)
response = requests.get(base_url, headers)
content = response.content.decode("utf-8", "ignore")
os.chdir(r'/home/coding/workspace/PyWeb') # TODO: 此处路径请自行修改
f = open('http.txt', 'a', encoding='utf-8')
res = re.findall('"pic_url":"http[s]?://[^,]*\.[jpg]{3}|[png]{3}?",$', content)

# TODO: 部分失败，存在安全检测

for i in res:
    f.write(i[11:]+'\n')
f.close()
input('press enter to exit : ')