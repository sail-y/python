# -*- coding: utf-8 -*-
__author__ = 'xiaomai'

import urllib
import urllib2
import cookielib

filename = 'cookie.txt'
# 声明一个MozillaCookieJar对象实例来保存cookie，之后写入文件
cookie = cookielib.MozillaCookieJar(filename)
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
postData = urllib.urlencode({'name': 'zfengche001', 'pwd': 'zfengche001'})
# 登陆风车车系统
loginUrl = 'http://www.zfengche.com/zfengche-admin/userController/login'
# 模拟登录，并把cookie保存到变量
try:
    result = opener.open(loginUrl, postData)

except urllib2.URLError, e:
    if hasattr(e, "code"):
        print e.code
    if hasattr(e, "reason"):
        print e.reason
print result.read()

# 保存cookie到cookie.txt中
cookie.save(ignore_discard=True, ignore_expires=True)
# 利用cookie访问另一个网址，获得城市列表
cityUrl = 'http://www.zfengche.com/zfengche-admin/city/list'

result = opener.open(cityUrl)

print result.read()
