# -*- coding: utf-8 -*-  
""" 
最后一步，对于要测试的验证码处理，然后进行预测，输出结果 
"""  
  
from PIL import Image 
from PIL import *
import numpy as np 
import os  
import warnings
import time 
from sklearn.svm import SVC
from sklearn import cross_validation as cs  
from sklearn.externals import joblib   
  
# 图片切割，每个验证码切4份，宽40，高81  
def segment(im):  
    x = 12
    y = 0
    w = 40  
    h = 81  
    im_new = []  
  
    for i in range(4):  
        im1 = im.crop((x+w*i,y,x+w*(i+1),h))  
        im_new.append(im1)  
    return im_new  
  
  
# 图片预处理，二值化，图片增强  
def imgTransfer(f_name):  
    im = Image.open(f_name)  
    im = im.filter(ImageFilter.MedianFilter())  
    #enhancer = ImageEnhance.Contrast(im)  
    #im = enhancer.enhancer(1)  
    im = im.convert('L')  
  
    return im   
  
def cutPictures2(img):  
    im = imgTransfer(img)  
    pics = segment(im) 
    img = os.path.splitext(os.path.basename(img))
    img = img[0]
    for pic,i in zip(pics,range(1,5)):  
        pic.save(u'D:/Desktop/智能嵌入式设计/number_recognizing/test_picture/%s.%d.jpeg'%(img,i),'jpeg')  
  
# 特征提取，获取图像二值化数学值  
def getBinaryPix(im):  
    im = Image.open(im)  
    img = np.array(im)  
    rows,cols = img.shape  
    for i in range(rows):  
        for j in range(cols):  
            if (img[i,j]<= 240):  
                img[i,j] = 0  
            else:  
                img[i,j] = 1  
    img_new = []
    sum = 0
    for i in range(rows):  
        for j in range(cols):
            sum = sum + img[i,j]
        img_new.append(sum)
        sum = 0
    sum = 0
    for j in range(cols):  
        for i in range(rows):
            sum = sum + img[i,j]
        img_new.append(sum)
        sum = 0
#    for i in range(121):
#        img_new[i] = str(i)+':'+str(img_new[i])
    binpix = np.array(img_new)
     
    return binpix  

def load_data():   
    dataset = np.loadtxt(u'D:/Desktop/智能嵌入式设计/number_recognizing/traindata.txt',delimiter=',')  
    return dataset
  
# 交叉验证  
def cross_validation():  
    dataset = load_data()  
    row,col = dataset.shape  
    X = dataset[:,:col-1]  
    Y = dataset[:,-1]  
    clf = SVC(kernel='rbf',C=1000)  
    clf.fit(X,Y)  
    scores = cs.cross_val_score(clf,X,Y,cv=5)  
    print ("Accuracy: %0.2f (+- %0.2f)" % (scores.mean(),scores.std()))  
      
    return clf 

def load_Predict(name):  
#  
#    cutPictures2(name)      #切割图片  
      
#    dirs = u'D:/Desktop/智能嵌入式设计/number_recognizing/test_picture/'
    dirs = u'D:/Desktop/智能嵌入式设计/第二讲 计算机视觉/test_pics/'
    fs = os.listdir(dirs)    # 获取图片名称  
    clf = cross_validation()    
    predictValue = []
      
    for fname in fs:  
        fn = dirs + fname  
        binpix = getBinaryPix(fn)
        binpix = binpix.reshape(1, -1)         
        predictValue.append(clf.predict(binpix))  
          
    predictValue = [str(int(i)) for i in predictValue]  
    print ("the picture number is :" ,"".join(predictValue))  
                 
name = u'D:/Desktop/智能嵌入式设计/number_recognizing/1861.jpg'
name = u'D:/Desktop/智能嵌入式设计/number_recognizing/2833.jpg'
load_Predict(name)
