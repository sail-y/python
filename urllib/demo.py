__author__ = 'xiaomai'

import urllib
import urllib2

# POST
values = {"username": "1016903103@qq.com", "password": "XXXX"}

data = urllib.urlencode(values)
url = "https://passport.csdn.net/account/login?from=http://my.csdn.net/my/mycsdn"
request = urllib2.Request(url, data)
response = urllib2.urlopen(request)
print response.read()

# GET

values = {}
values['username'] = "1016903103@qq.com"
values['password'] = "XXXX"
data = urllib.urlencode(values)
url = "http://passport.csdn.net/account/login"
geturl = url + "?" + data
request = urllib2.Request(geturl)
response = urllib2.urlopen(request)
print response.read()
