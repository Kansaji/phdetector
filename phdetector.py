import cv2   
import numpy as np

#capturing video through webcam
cap=cv2.VideoCapture('../resources/7.jpg')

while(1):
        _, img = cap.read()
            
        #converting frame(img i.e BGR) to HSV (hue-saturation-value)

        hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

        #defining the Range of red color ph 4
        red_lower=np.array([0, 100, 20],np.uint8)
        red_upper=np.array([14, 255, 255],np.uint8)

        #defining the Range of orange color ph 5
        orange_lower=np.array([15, 150, 20],np.uint8)
        orange_upper=np.array([24, 255, 255],np.uint8)
        
        #defining the Range of yellow color ph 6
        yellow_lower=np.array([25, 50, 20],np.uint8)
        yellow_upper=np.array([30, 255, 255],np.uint8)

        #defining the Range of green color ph7
        green_lower=np.array([45,50,20],np.uint8)
        green_upper=np.array([75,255,255],np.uint8)

        #defining the Range of dark green color ph 8
        darkgreen_lower=np.array([76,50,150],np.uint8)
        darkgreen_upper=np.array([90,255,255],np.uint8)
        
        #defining the Range of blue color ph 9
        blue_lower=np.array([95,50,20],np.uint8)
        blue_upper=np.array([135,255,255],np.uint8)
        
        #defining the Range of violet color ph 10
        violet_lower=np.array([136,50,20],np.uint8)
        violet_upper=np.array([155,255,255],np.uint8)

      

        #finding the range in the image
        red=cv2.inRange(hsv,red_lower,red_upper)
        orange=cv2.inRange(hsv,orange_lower,orange_upper)
        yellow=cv2.inRange(hsv,yellow_lower,yellow_upper)
        green=cv2.inRange(hsv,green_lower,green_upper)
        darkgreen=cv2.inRange(hsv,darkgreen_lower,darkgreen_upper)
        blue=cv2.inRange(hsv,blue_lower,blue_upper)
        violet=cv2.inRange(hsv,violet_lower,violet_upper)
     
        
        #Morphological transformation, Dilation         
        kernal = np.ones((5 ,5), "uint8")

        red=cv2.dilate(red,kernal)
        orange=cv2.dilate(orange,kernal)

        yellow=cv2.dilate(yellow,kernal)
        #res1=cv2.bitwise_and(img, img, mask = yellow) 

        green=cv2.dilate(green,kernal)
        #res2=cv2.bitwise_and(img, img, mask = green)

        darkgreen=cv2.dilate(darkgreen,kernal)
        #res3=cv2.bitwise_and(img, img, mask = blue)

        blue=cv2.dilate(blue,kernal)

        violet=cv2.dilate(violet,kernal)
        
   
        #Tracking the red Color
        (contours,hierarchy)=cv2.findContours(red,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
        for pic, contour in enumerate(contours):
                area = cv2.contourArea(contour)
                if(area>10000):
                        M = cv2.moments(contour)
                        cx = int(M["m10"]/M["m00"])
                        cy = int(M["m01"]/M["m00"])
                        cv2.circle(img,(cx,cy),7,(255,255,255),-1)
                        x,y,w,h = cv2.boundingRect(contour)     
                        cv2.putText(img,"pH 4",(cx+5,cy),cv2.FONT_HERSHEY_SIMPLEX, 1.0, (255,255,255))  
          
        #Tracking the orange Color
        (contours,hierarchy)=cv2.findContours(orange,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
        for pic, contour in enumerate(contours):
                area = cv2.contourArea(contour)
                if(area>10000):
                        M = cv2.moments(contour)
                        cx = int(M["m10"]/M["m00"])
                        cy = int(M["m01"]/M["m00"])
                        cv2.circle(img,(cx,cy),7,(255,255,255),-1)
                        x,y,w,h = cv2.boundingRect(contour)     
                        cv2.putText(img,"pH 5",(cx+5,cy),cv2.FONT_HERSHEY_SIMPLEX, 1.0, (255,255,255))  

        #Tracking the yellow Color
        (contours,hierarchy)=cv2.findContours(yellow,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
        for pic, contour in enumerate(contours):
                area = cv2.contourArea(contour)
                if(area>10000):
                        M = cv2.moments(contour)
                        cx = int(M["m10"]/M["m00"])
                        cy = int(M["m01"]/M["m00"])
                        cv2.circle(img,(cx,cy),7,(255,255,255),-1)
                        x,y,w,h = cv2.boundingRect(contour)     
                        cv2.putText(img,"pH 6",(cx+5,cy),cv2.FONT_HERSHEY_SIMPLEX, 1.0, (255,255,255))  

        #Tracking the green Color
        (contours,hierarchy)=cv2.findContours(green,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
        for pic, contour in enumerate(contours):
                area = cv2.contourArea(contour)
                if(area>10000):
                        M = cv2.moments(contour)
                        cx = int(M["m10"]/M["m00"])
                        cy = int(M["m01"]/M["m00"])
                        cv2.circle(img,(cx,cy),7,(255,255,255),-1)
                        x,y,w,h = cv2.boundingRect(contour)     
                        cv2.putText(img,"pH 7",(cx+5,cy),cv2.FONT_HERSHEY_SIMPLEX, 1.0, (255,255,255))  
            
        #Tracking the darkgreen Color
        (contours,hierarchy)=cv2.findContours(darkgreen,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
        for pic, contour in enumerate(contours):
                area = cv2.contourArea(contour)
                if(area>10000):
                        M = cv2.moments(contour)
                        cx = int(M["m10"]/M["m00"])
                        cy = int(M["m01"]/M["m00"])
                        cv2.circle(img,(cx,cy),7,(255,255,255),-1)
                        x,y,w,h = cv2.boundingRect(contour)     
                        cv2.putText(img,"pH 8",(cx+5,cy),cv2.FONT_HERSHEY_SIMPLEX, 1.0, (255,255,255))  

         #Tracking the blue Color
        (contours,hierarchy)=cv2.findContours(blue,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
        for pic, contour in enumerate(contours):
                area = cv2.contourArea(contour)
                if(area>10000):
                        M = cv2.moments(contour)
                        cx = int(M["m10"]/M["m00"])
                        cy = int(M["m01"]/M["m00"])
                        cv2.circle(img,(cx,cy),7,(255,255,255),-1)
                        x,y,w,h = cv2.boundingRect(contour)     
                        cv2.putText(img,"pH 9",(cx+5,cy),cv2.FONT_HERSHEY_SIMPLEX, 1.0, (255,255,255))  

         #Tracking the violet Color
        (contours,hierarchy)=cv2.findContours(violet,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
        for pic, contour in enumerate(contours):
                area = cv2.contourArea(contour)
                if(area>10000):
                        M = cv2.moments(contour)
                        cx = int(M["m10"]/M["m00"])
                        cy = int(M["m01"]/M["m00"])
                        cv2.circle(img,(cx,cy),7,(255,255,255),-1)
                        x,y,w,h = cv2.boundingRect(contour)     
                        cv2.putText(img,"pH 10",(cx+5,cy),cv2.FONT_HERSHEY_SIMPLEX, 1.0, (255,255,255))  
                  

        
       
        cv2.imshow("PH detector",img)
        
        if cv2.waitKey(10) & 0xFF == ord('q'):
                cap.release()
                cv2.destroyAllWindows()
                break  
