#!/usr/bin/env python
# coding=utf-8

from urllib2 import urlopen
from bs4 import BeautifulSoup

amazon = "https://www.amazon.cn/gp/feature.html/ref=sa_menu_kindle_l3_f126758?ie=UTF8&docId=126758"

def getInfo(URL):
    html = urlopen(URL)
    data = html.read()
    soup = BeautifulSoup(data,"lxml")
    dicounts = soup.findAll(attrs={"class": "gridProductContainer"})

