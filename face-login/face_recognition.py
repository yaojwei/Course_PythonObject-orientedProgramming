import cv2
import os
import numpy as np
import uuid

# 检测人脸
def detect_face(img):
    #将测试图像转换为灰度图像，因为opencv人脸检测器需要灰度图像
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    #加载OpenCV人脸检测分类器Haar
    face_cascade = cv2.CascadeClassifier('./haarcascade_frontalface_default.xml')
    
    #检测多尺度图像，返回值是一张脸部区域信息的列表（x,y,宽,高）
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=5)
    
    # 如果未检测到面部，则返回原始图像
    if (len(faces) == 0):
        return None, None
 
    #目前假设只有一张脸，xy为左上角坐标，wh为矩形的宽高

    (x, y, w, h) = faces[0]
    #返回图像的正面部分
    return gray[y:y + w, x:x + h], faces[0]

# 1. 加载训练样本

# 获取训练样本目录
data_path = "training_data"
dirs = os.listdir(data_path)

faces = []   #保存脸部
labels = []  #保存标签

# 遍历样本目录
for dir_name in dirs:

    # 为了方便， 把不同人的目录命名为0 1...
    if not dir_name.isdigit():
        continue

    label = int(dir_name)

    # 建立包含当前人物人物图像的目录路径
    dir_path = data_path + "/" + dir_name
    # 获取给定人物目录内的图像名称
    images_names = os.listdir(dir_path)

    # 遍历每张人物图像并检测脸部， 将脸部信息添加到faces
    for image_name in images_names:
        # 如果不是.jpg就过滤掉
        if not image_name.endswith(".jpg") :
                continue
        # 拼接图像路径
        image_path = dir_path + "/" + image_name
        # 读取图像
        image = cv2.imread(image_path)
        print("========>>>正在训练"+image_path)
        #检测人脸
        face, rect = detect_face(image)

        # 过滤掉没有检测到人脸的图片
        if face is not None:
            faces.append(face)
            labels.append(label)


# 2.创建LBPH识别器并开始训练
face_recognizer = cv2.face.LBPHFaceRecognizer_create()
face_recognizer.train(faces, np.array(labels))

# 表示人名与目录名的对应
subjects = ["XuanBin", "LinZhiling"]

# 3.加载测试图像并预测
def rec(rec_img):
    # img = rec_img.copy()
    #检测人脸
    face,rect = detect_face(rec_img)
    #预测人脸
    label = face_recognizer.predict(face)
    return label,rect

#根据给定的（x，y）坐标和宽度高度在图像上绘制矩形
def draw_rectangle(img, rect):
    (x, y, w, h) = rect
    cv2.rectangle(img, (x, y), (x + w, y + h), (130, 57, 53), 5)
# 根据给定的（x，y）坐标标识出人名
def draw_text(img, text, x, y):
    cv2.putText(img, text, (x, y), cv2.FONT_HERSHEY_COMPLEX, 3, (130, 57, 53), 5)


