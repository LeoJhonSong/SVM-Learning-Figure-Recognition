#-*- coding:utf-8 -*-  
import requests  
  
# 文件下载，主要下载训练集  
def download_pics(pic_name):  
  
    url = 'http://smart.gzeis.edu.cn:8081/Content/AuthCode.aspx'  
    res = requests.get(url,stream=True)  
  
    with open(u'D:/Desktop/智能嵌入式设计/number_recognizing/pics/%s.jpeg'%(pic_name),'wb') as f:  
        for chunk in res.iter_content(chunk_size=1024):  
            if chunk:  
                f.write(chunk)  
                f.flush()  
        f.close()  
  
if __name__ == '__main__':  
    for i in range(1000):  
        pic_name = i+1
        download_pics(pic_name)
