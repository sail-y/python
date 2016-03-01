__author__ = 'xiaomai'

import os

print(os.name)

print(os.uname())

print(os.environ.get('PATH'))

# 查看当前目录的绝对路径:
print(os.path.abspath('.'))
# 在某个目录下创建一个新目录，首先把新目录的完整路径表示出来:
path = os.path.join('/Users/xiaomai', 'testdir')
# 然后创建一个目录
os.mkdir(path)

os.rmdir(path)

with open('t.txt','w') as f:
    f.write('123')
os.rename('t.txt', 't.py')
os.remove('t.py')

dirs = [x for x in os.listdir('.') if os.path.isdir(x)]