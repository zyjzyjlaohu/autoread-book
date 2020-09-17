#!/usr/bin/python
#vim: set fileencoding:utf-8
#coding:utf-8
import cv2
capture = cv2.VideoCapture(0)
#拍照
while(True):
    # 获取一帧
    ret, frame = capture.read()
    # 将这帧转换为灰度图
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('frame', gray)
    if cv2.waitKey(1) == ord('q'):
        cv2.imwrite("youtemp.png", frame)
        capture.release() #释放摄像头
        cv2.destroyAllWindows()#删除建立的全部窗口
        break
