#coding:utf-8

import cv2
from PIL import Image
 
def CatchUsbVideo(window_name, camera_idx):
    cv2.namedWindow(window_name)

    cam = cv2.VideoCapture(camera_idx)                
    
    #告诉OpenCV使用人脸识别分类器
    detector = cv2.CascadeClassifier("../haarcascade_frontalface_default.xml")
    
    #识别出人脸后要画的边框的颜色，RGB格式
    color = (0, 255, 0)
        
    while cam.isOpened():
        ok, img = cam.read() #读取一帧数据
        if not ok:            
            break  
 
        #将当前帧转换成灰度图像
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)    
        faces = detector.detectMultiScale(gray, 1.2, 5)
        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x + w, y + h), color, 2)
            #sampleNum = sampleNum + 1
            #cv2.imwrite("dataSet/user." + str(Id) + '.' + str(sampleNum) + ".jpg", gray[y:y + h, x:x + w])  
            #cv2.imshow('frame', img)
             
        '''        
        #人脸检测，1.2和2分别为图片缩放比例和需要检测的有效点数
        faces = detector.detectMultiScale(gray, 1.2, 5)
        faceRects = classfier.detectMultiScale(grey, scaleFactor = 1.2, minNeighbors = 3, minSize = (32, 32))
        if len(faceRects) > 0:            #大于0则检测到人脸                                   
            for faceRect in faceRects:  #单独框出每一张人脸
                x, y, w, h = faceRect        
                cv2.rectangle(frame, (x - 10, y - 10), (x + w + 10, y + h + 10), color, 2)
        '''
                        
        #显示图像
        cv2.imshow(window_name, img)
        c = cv2.waitKey(10)
        
        if c & 0xFF == ord('q'):
            break        
  
    cam.release()
    cv2.destroyAllWindows() 

CatchUsbVideo('myface', 0)
