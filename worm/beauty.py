# -*- coding:utf-8 -*-
__author__ = 'xiaomai'

import urllib2
import re
import os
import urllib

# ----------- 处理页面上的各种标签 -----------
class HTMLTool:
    # 用非 贪婪模式 匹配 \t 或者 \n 或者 空格 或者 超链接 或者 图片
    BgnCharToNoneRex = re.compile("(\t|\n| |<a.*?>|<img.*?>)")

    # 用非 贪婪模式 匹配 任意<>标签
    EndCharToNoneRex = re.compile("<.*?>")

    # 用非 贪婪模式 匹配 任意<p>标签
    BgnPartRex = re.compile("<p.*?>")
    CharToNewLineRex = re.compile("(<br/>|</p>|<tr>|<div>|</div>)")
    CharToNextTabRex = re.compile("<td>")

    # 将一些html的符号实体转变为原始符号
    replaceTab = [("<", "<"), (">", ">"), ("&", "&"), ("&", "\""), (" ", " ")]

    def replace_char(self, x):
        x = self.BgnCharToNoneRex.sub("", x)
        x = self.BgnPartRex.sub("\n    ", x)
        x = self.CharToNewLineRex.sub("\n", x)
        x = self.CharToNextTabRex.sub("\t", x)
        x = self.EndCharToNoneRex.sub("", x)

        for t in self.replaceTab:
            x = x.replace(t[0], t[1])
        return x


class Beauty(object):
    def __init__(self):
        self.page_index = 1
        self.base_url = 'http://www.meizitu.com/a/list_1_'
        self.tool = HTMLTool()

    def get_page(self, page):
        try:
            url = self.base_url + str(page) + '.html'
            print u'正在加载页面....', url
            response = urllib2.urlopen(url)
            text = response.read().decode('gbk', 'ignore')
            # 正则匹配，匹配其中的图片
            html = re.search(r'<li class="wp-item".*</li>', text, re.S)
            urls = re.findall(r'<a .*?><img src="(.*?)" alt="(.*?)"></a>', html.group(), re.I)
            url_list = []
            for i in urls:
                url = i[0].strip()
                url_list.append(url)
            return urls
        except urllib2.URLError, e:
            if hasattr(e, 'reason'):
                print u"连接失败,错误原因", e.reason
                return None

    def get_beauty(self):
        for i in range(2, 79):
            images = self.get_page(i)
            print u"发现本页共有", len(images), u"张照片"
            for image in images:
                image_url = image[0]
                filename = image[1]
                self.save_img(image_url, filename)

    def save_img(self, image_url, filename):
        filename = self.tool.replace_char(filename) + '.' + image_url.split('.')[-1]
        print u'正在保存', filename
        print image_url
        if not os.path.exists('h'):
            os.makedirs('h')
        urllib.urlretrieve(image_url, 'h/' + filename)


beauty = Beauty()

print beauty.get_beauty()


