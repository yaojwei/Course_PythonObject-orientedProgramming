# -*- coding: UTF-8 -*-
from tkinter import *
from tkinter import messagebox  
import cv2 
from PIL import Image, ImageTk
import os
import face_recognition


#临时变量
tempimagepath="test_data/face.jpg"

#摄像机设置
#0是代表摄像头编号，只有一个的话默认为0
capture=cv2.VideoCapture(0) 

def getframe():
    ref,frame=capture.read()
    cv2.imwrite(tempimagepath,frame)

def closecamera():
    capture.release()

#界面相关
window_width=640
window_height=480
image_width=int(window_width*0.6)
image_height=int(window_height*0.6)
imagepos_x=int(window_width*0.2)
imagepos_y=int(window_height*0.1)
butpos_x=250
butpos_y=350



top=Tk()
top.wm_title("欢迎登录")
top.geometry(str(window_width)+'x'+str(window_height))

# 右上角关闭按钮点击事件
def callbackClose():
    messagebox.showinfo(title='提示', message='欢迎下次使用')
    top.destroy()
    top.mainloop()  
    closecamera()


top.protocol("WM_DELETE_WINDOW", callbackClose)


def tkImage():
   ref,frame=capture.read()
   cvimage = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
   pilImage=Image.fromarray(cvimage)
   pilImage = pilImage.resize((image_width, image_height),Image.ANTIALIAS)
   tkImage =  ImageTk.PhotoImage(image=pilImage)
   return tkImage

# 点击登录按钮
def button1():
    ref,frame=capture.read()
    cv2.imwrite(tempimagepath,frame)
    face_img = cv2.imread("test_data/face.jpg")
    # cv2.imshow("Training on image...", face_img)
    try:
        label,rect = face_recognition.rec(face_img)
        print(label)
        if label[1] < 50 :
            face_recognition.draw_rectangle(face_img, rect)
            face_recognition.draw_text(face_img, face_recognition.subjects[label[0]], rect[0], rect[1] - 5)
            cv2.imshow("welcome", face_img)
            messagebox.showinfo(title='欢迎',message='hi    '+face_recognition.subjects[label[0]])
        else :
            messagebox.showwarning(title='警告',message='未识别到人脸或用户不存在')
    except BaseException :
        messagebox.showwarning(title='警告',message='未识别到人脸或用户不存在')
    
    
    # 用来控制识别精度(数值越低 精度越高)
    


#控件定义
canvas =Canvas(top,bg='white',width=image_width,height=image_height)#绘制画布
b=Button(top,text='登录',width=15,height=2,command=button1)

#控件位置设置
canvas.place(x=imagepos_x,y=imagepos_y)
b.place(x=butpos_x,y=butpos_y)



while(True):
    picture=tkImage()
    canvas.create_image(0,0,anchor='nw',image=picture)
    top.update()
    top.after(100)     

top.mainloop()  
closecamera()
