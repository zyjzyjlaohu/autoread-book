#!/usr/bin/python
#vim: set fileencoding:utf-8
#coding:utf-8
import Tkinter as tk
import cv2
import os
import sys
import PIL
from PIL import Image
import pytesseract
import multiprocessing
import time

OK_VALUE=0




on_hit = False
def A():
	global on_hit
	global OK_VALUE
	try:
	  f =open("denggo.jpeg",'r')
	  f.close()
	except IOError:
	  f = open("denggo.jpeg",'w')
	  f.close()	

	def hit_me():
	    global on_hit
	    global OK_VALUE
	    #OK_VALUE = 0 

	    if on_hit == False:
	    	on_hit = True
		var.set('ok')
		OK_VALUE=1
		#录像
		#拍照
		capture = cv2.VideoCapture(0)
		#拍照
		while(True):
			    # 获取一帧
			    ret, frame = capture.read()
			    
			    cv2.imshow('Demo', frame)
			    if OK_VALUE==1:
				cv2.imwrite("denggo.jpeg", frame)
				capture.release() #释放摄像头
				cv2.destroyAllWindows()#删除建立的全部窗口
				time.sleep(3.5)
				#识别denggo.jpeg转化为文字
				text=pytesseract.image_to_string(Image.open('denggo.jpeg'),lang='chi_sim')
				print(text)
				word='"'+text+'"'

				#文字转音频
				#word = raw_input('输入想输出的音频')
				#print(word)
				reload(sys)
				sys.setdefaultencoding('utf-8')
				cmd = "ilang "+word
				os.system(cmd)
				break

		#print(ok_value)
	    else:
		on_hit = False
		var.set('')
		OK_VALUE=0
		#print(ok_value)

	#GUI
	window = tk.Tk()
	window.title('相机设置')
	window.geometry('200x100')
	var = tk.StringVar()
	l = tk.Label(window,textvariable = var,bg = 'green',font = ('Arial',12),width = 15,height = 2)  #textvarible是变量
	l.pack()
	on_hit = False
	b = tk.Button(window,text = '开启朗读',width = 15,height = 2,command = hit_me)
	b.pack()



	window.mainloop()



	

if __name__ == '__main__':
    func_list = [A]
    pool = multiprocessing.Pool(4)
    for func in func_list:
        pool.apply_async(func)
    pool.close()
    pool.join()
    
	
	
	
	
