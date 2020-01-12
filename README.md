# Course_PythonObject-orientedProgramming
这里存放的是课程《面向对象程序设计(Python)》的相关练习 ε=ε=ε=ε=ε=ε=┌(;￣◇￣)┘

# MAKE A PORTRAIT
## 简介
通过读取名人传记，得到词云图画像的程序
## 英文版
### 传记
Steve Jobs A Biography
### module
wordcloud模块  
matplotlib.pyplot模块  
imageio.imread模块  
### 效果图
![图片读取失败](https://github.com/yaojwei/Course_PythonObject-orientedProgramming/blob/master/Make%20a%20portrait/Steve%20jobs.png)  
## 中文版
### 传记
95本中外科学家发明家传记  
### module
wordcloud模块  
matplotlib.pyplot模块  
imageio.imread模块  
os模块  
jieba模块  
### 效果图
![图片读取失败](https://github.com/yaojwei/Course_PythonObject-orientedProgramming/blob/master/Make%20a%20portrait/Scientists%20and%20inventors.png)  
  

# FACE-LOGIN
## 简介
这是一个简单的人脸登录系统。通过摄像头采集人脸图像，判断是否允许登录  
## 关键技术
使用OpenCV人脸检测分类器Haar检测人脸  
使用LBPH识别器训练已知数据集及预测未知图片  
使用tkinter完成GUI  
## 运行环境
python: 3.7.4  
opencv-python： 4.1.2.30  
numpy：1.17.4  
## 效果图
### 1、【登录界面】  
![图片读取失败](pic/image001.jpg)  
### 2、【test】  
#### 1）用户不存在  
![图片读取失败](pic/image002.jpg)  
#### 2）未识别到人脸  
![图片读取失败](pic/image003.jpg)  
#### 3）登录成功  
![图片读取失败](pic/image004.jpg)  
### 3、【退出】  
![图片读取失败](pic/image005.jpg)  
## 训练集
将不同用户的正脸照片放在training_data/的不同的目录下，目录依次以0、1、2...命名  
不同用户对应的名字存储在face_recognition.py中  

73 # 表示人名与目录名的对应  
74 subjects = ["XuanBin", "LinZhiling"]  
