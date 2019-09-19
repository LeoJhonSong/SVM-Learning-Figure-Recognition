# -*- coding: utf-8 -*-  
  
from PIL import Image,ImageEnhance  
from PIL import *  
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
  
  
def cutPictures(img):  
    im = imgTransfer(img)  
    pics = segment(im) 
    img = os.path.splitext(os.path.basename(img))
    img = img[0]
    for pic,i in zip(pics,range(1,5)):
        pic.save('D:/Desktop/智能嵌入式设计/number_recognizing/test/%s.%d.jpeg'%(img,i),'jpeg') 
  
  
# 读取某文件夹下的所有图片的基名  
import os  
def getAllImages(folder):  
    assert os.path.exists(folder)  
    assert os.path.isdir(folder)  
    imageList = os.listdir(folder)   
    return imageList  
  
  
if __name__ == '__main__':  
  
    files_name =  getAllImages(u'D:/Desktop/智能嵌入式设计/number_recognizing/pics')  
      
    for i in files_name: 
        name = 'D:/Desktop/智能嵌入式设计/number_recognizing/pics/' + i  
        cutPictures(name)
