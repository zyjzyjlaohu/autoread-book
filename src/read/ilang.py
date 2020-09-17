#!/usr/bin/python
#vim: set fileencoding:utf-8
#coding:utf-8
import os
import sys
word = "这儿再说一点，我们知道如果要判别两个人是谁，训练的时候肯定是要给两个人的照片分类的，比如A标记为0，B标记为1。此模型也是如此来训练的，在load_face.py中的load_dataset函数里有一行代码就是如此，代码如下："
#print(word)
reload(sys)
sys.setdefaultencoding('utf-8')
cmd = "ilang "+word
os.system(cmd)
