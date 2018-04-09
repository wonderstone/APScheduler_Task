# -*- coding: utf-8 -*-
# @Time    : 2018/4/8 下午9:33
# @Author  : wonderstone
# @FileName: tmp.py
# @Software: PyCharm
# @Ref     :

import urllib.request
import os, re
from bs4 import BeautifulSoup

URL = "http://www.86kongqi.com/city/beijing.html"
page = urllib.request.urlopen(URL)
soup = BeautifulSoup(page)
page.close()

tables = soup.findAll('table')

pass