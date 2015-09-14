# -*- coding:utf-8 -*-
__author__ = 'xiaomai'

import urllib
import urllib2
import re


class Tool(object):
    # 去除img标签,7位长空格
    removeImg = re.compile('<img.*?>| {7}|')
    # 删除超链接标签
    removeAddr = re.compile('<a.*?>|</a>')
    # 把换行的标签换为\n
    replaceLine = re.compile('<tr>|<div>|</div>|</p>')
    # 将表格制表<td>替换为\t
    replaceTD = re.compile('<td>')
    # 把段落开头换为\n加空两格
    replacePara = re.compile('<p.*?>')
    # 将换行符或双换行符替换为\n
    replaceBR = re.compile('<br><br>|<br>')
    # 将其余标签剔除
    removeExtraTag = re.compile('<.*?>')

    def replace(self, x):
        # x = re.sub(self.removeImg, "", x)
        x = re.sub(self.removeAddr, "", x)
        x = re.sub(self.replaceLine, "\n", x)
        x = re.sub(self.replaceTD, "\t", x)
        x = re.sub(self.replacePara, "\n    ", x)
        x = re.sub(self.replaceBR, "\n", x)
        x = re.sub(self.removeExtraTag, "", x)
        # strip()将前后多余内容删除
        return x.strip()


class TieBaPost(object):
    def __init__(self, base_url, see_lz, floor_tag):
        self.base_url = base_url
        self.see_lz = '?see_lz=' + str(see_lz)
        self.tool = Tool()
        # 楼层标号，初始为1
        self.floor = 1
        self.default_title = u'百度贴吧'
        # 是否写入楼分隔符的标记
        self.floor_tag = floor_tag

    # 传入页码获取页面代码
    def get_page(self, page_num):
        try:
            url = self.base_url + self.see_lz + '&pn=' + str(page_num)
            request = urllib2.Request(url)
            response = urllib2.urlopen(request)
            # print response.read()
            return response.read().decode('utf-8', 'ignore')
        except urllib2.URLError, e:
            if hasattr(e, "reason"):
                print u"连接百度贴吧失败,错误原因", e.reason
                return None

    def get_title(self, index_page):
        pattern = re.compile('<h1 class="core_title_txt.*?>(.*?)</h1>', re.S)
        result = re.search(pattern, index_page)
        if result:
            return result.group(1)
        else:
            return None

    # 帖子一共有多少页
    def get_page_num(self, index_page):
        pattern = re.compile('<li class="l_reply_num.*?</span>.*?<span.*?>(.*?)</span>', re.S)
        result = re.search(pattern, index_page)
        if result:
            return result.group(1).strip()
        else:
            return None

    # 获取每一层楼的内容,传入页面内容
    def get_content(self, page):
        pattern = re.compile('<div id="post_content_.*?>(.*?)</div>', re.S)
        items = re.findall(pattern, page)
        contents = []
        for item in items:
            content = "\n" + self.tool.replace(item) + "\n"
            contents.append(content.encode('utf-8'))
        return contents

    def set_file_title(self, title):
        # 如果标题不是为None，即成功获取到标题
        if title is not None:
            self.file = open(title + ".txt", "w+")
        else:
            self.file = open(self.default_title + ".txt", "w+")

    def write_post(self, contents):
        for item in contents:
            if self.floor_tag == '1':
                floor_line = "\n" + str(
                    self.floor) + u"-----------------------------------------------------------------------------------------\n"
                self.file.write(floor_line)
            self.file.write(item)
            self.floor += 1

    def start(self):
        index_page = self.get_page(1)
        pageNum = self.get_page_num(index_page)
        title = self.get_title(index_page)
        self.set_file_title(title)
        if pageNum == None:
            print "URL已失效，请重试"
            return
        try:
            print "该帖子共有" + str(pageNum) + "页"
            for i in range(1, int(pageNum) + 1):
                print "正在写入第" + str(i) + "页数据"
                page = self.get_page(i)
                contents = self.get_content(page)
                self.write_post(contents)
        # 出现写入异常
        except IOError, e:
            print "写入异常，原因" + e.message
        finally:
            print "写入任务完成"


print u"请输入帖子代号"
base_url = u'http://tieba.baidu.com/p/' + str(raw_input(u'http://tieba.baidu.com/p/'))
tieba = TieBaPost(base_url, 1, 1)

seeLZ = raw_input("是否只获取楼主发言，是输入1，否输入0\n")
floorTag = raw_input("是否写入楼层信息，是输入1，否输入0\n")
bdtb = TieBaPost(base_url, seeLZ, floorTag)
bdtb.start()
