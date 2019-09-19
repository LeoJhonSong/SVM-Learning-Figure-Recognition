# -*- coding: utf-8 -*-  
""" 
Created on Thu Mar 23 16:18:39 2017 
 
@author: onlyyo 
根据之前得到的验证码像素数组，以及他们的标签，用SVM对其进行模型训练 
"""  
  
from sklearn.svm import SVC  
from sklearn import grid_search  
import numpy as np    
from sklearn import cross_validation as cs  
from sklearn.externals import joblib    
import warnings  
import time  
  
  
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
  
t0 = time.time()  
cross_validation()  
#print "fit time:",round(time.time()-t0,3),"s"  
  
def searchBestParameter():  
    parameters = {'kernel':('linear','poly','rbf','sigmoid'),'C':[1,100]}  
      
    dataset = load_data()  
    row,col = dataset.shape  
    X = dataset[:,:col-1]  
    Y = dataset[:,-1]  
    svr = SVC()  
    clf = grid_search.GridSearchCV(svr,parameters)  
    clf.fit(X,Y)  
      
    print (clf.best_params_)  
      
#searchBestParameter()  
print ("fit time:",round(time.time()-t0,3))
