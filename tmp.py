# -*- coding: utf-8 -*-
# @Time    : 2018/4/8 下午9:33
# @Author  : wonderstone
# @FileName: tmp.py
# @Software: PyCharm
# @Ref     :

import urllib.request
import os, re
from bs4 import BeautifulSoup

# URL = "http://www.86kongqi.com/city/beijing.html"
# page = urllib.request.urlopen(URL)
# soup = BeautifulSoup(page)
# page.close()
#
# tables = soup.findAll('table')
#
# pass



from urllib import request

# URL = 'https://api.waqi.info/feed/here/?token=10b942c7d7a778b33de56a1a1f0d4d6b041eec27'
URL = 'https://api.waqi.info/feed/geo:39.954592;116.468117/?token=10b942c7d7a778b33de56a1a1f0d4d6b041eec27'

page = request.urlopen(URL)

data = page.read()
datastr = data.decode()
print(datastr)
pass