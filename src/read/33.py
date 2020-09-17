#encoding:utf-8
import os
import sys

word = '黄梦彩'
print(word)
reload(sys)
sys.setdefaultencoding('utf-8')
cmd = 'ilang '+word
os.system(cmd)
