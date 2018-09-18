"""
    model: image_download

"""
import os
import requests
import time


def get_file():
    os.chdir(r'C:\Users\admin\Desktop\python\img')
    f = open('../http.txt', 'r')
    num = 0
    headers = {'Accept': '*/*',
               'Accept-Language': 'zh-CN,en;q=0.8',
               'Cache-Control': 'max-age=0',
               'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36',
               'Connection': 'keep-alive',
               'Referer': 'http://www.baidu.com/'
               }
    for i in f.readlines():
        application = i[-4:-1]
        res = requests.get(i, headers)
        content = res.content
        path_content = time.time()
        img = open('%d%s.%s' % (num, path_content, application), 'wb+')
        img.write(content)
        img.close()
        print('download : %s' % i)
        num += 1
    f = open('../http.txt', 'w+')
    f.close()
