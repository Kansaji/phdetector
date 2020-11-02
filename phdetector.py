import cv2   
import numpy as np
from datetime import datetime
import tkinter as tk
from tkinter import simpledialog
from tkinter import filedialog
import os


def calculate_ph(path):
        cap=cv2.VideoCapture(path)
        while(1):
                _, img = cap.read()
               
                
                minarea=1800
                fontsize=0.5
                pointersize=3
                #converting frame to HSV
                try:
                        
                        hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
                except:
                        cap.release()  
                        break
                
                #defining the Range of red color ph 4
                red_lower=np.array([175, 50, 50],np.uint8)
                red_upper=np.array([179, 255, 255],np.uint8)

                #defining the Range of orange color ph 5
                orange_lower=np.array([1.5, 50, 20],np.uint8)
                orange_upper=np.array([4, 255, 255],np.uint8)
                
                #defining the Range of yellow color ph 6
                yellow_lower=np.array([5, 50, 20],np.uint8)
                yellow_upper=np.array([30, 255, 255],np.uint8)

                #defining the Range of green color ph7
                green_lower=np.array([32,50,30],np.uint8)
                green_upper=np.array([38,255,255],np.uint8)

                #defining the Range of dark green color ph 8
                darkgreen_lower=np.array([45,50,20],np.uint8)
                darkgreen_upper=np.array([80,255,100],np.uint8)
                
                #defining the Range of blue color ph 9
                blue_lower=np.array([95,50,20],np.uint8)
                blue_upper=np.array([135,255,255],np.uint8)
                
                #defining the Range of violet color ph 10
                violet_lower=np.array([82,0,0],np.uint8)
                violet_upper=np.array([102,255,25],np.uint8)

                     
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

                red=cv2.erode(red,kernal)

                orange=cv2.erode(orange,kernal)

                yellow=cv2.erode(yellow,kernal)
               
                green=cv2.erode(green,kernal)
             
                darkgreen=cv2.erode(darkgreen,kernal)

                blue=cv2.erode(blue,kernal)

                violet=cv2.dilate(violet,kernal)
                   
                #Tracking the red Color
                (contours,hierarchy)=cv2.findContours(red,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
                for pic, contour in enumerate(contours):
                        area = cv2.contourArea(contour)
                        if(area>minarea):
                                M = cv2.moments(contour)
                                cx = int(M["m10"]/M["m00"])
                                cy = int(M["m01"]/M["m00"])
                                cv2.circle(img,(cx,cy),pointersize,(255,255,255),-1)
                                x,y,w,h = cv2.boundingRect(contour)     
                                cv2.putText(img,"pH 4",(cx+5,cy),cv2.FONT_HERSHEY_SIMPLEX, fontsize, (255,255,255))  
                  
                #Tracking the orange Color
                (contours,hierarchy)=cv2.findContours(orange,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
                for pic, contour in enumerate(contours):
                        area = cv2.contourArea(contour)
                        if(area>minarea):
                                M = cv2.moments(contour)
                                cx = int(M["m10"]/M["m00"])
                                cy = int(M["m01"]/M["m00"])
                                cv2.circle(img,(cx,cy),pointersize,(255,255,255),-1)
                                x,y,w,h = cv2.boundingRect(contour)     
                                cv2.putText(img,"pH 5",(cx+5,cy),cv2.FONT_HERSHEY_SIMPLEX, fontsize, (255,255,255))  

                #Tracking the yellow Color
                (contours,hierarchy)=cv2.findContours(yellow,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
                for pic, contour in enumerate(contours):
                        area = cv2.contourArea(contour)
                        if(area>minarea):
                                M = cv2.moments(contour)
                                cx = int(M["m10"]/M["m00"])
                                cy = int(M["m01"]/M["m00"])
                                cv2.circle(img,(cx,cy),pointersize,(255,255,255),-1)
                                x,y,w,h = cv2.boundingRect(contour)     
                                cv2.putText(img,"pH 6",(cx+5,cy),cv2.FONT_HERSHEY_SIMPLEX, fontsize, (255,255,255))  

                #Tracking the green Color
                (contours,hierarchy)=cv2.findContours(green,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
                for pic, contour in enumerate(contours):
                        area = cv2.contourArea(contour)
                        if(area>minarea):
                                M = cv2.moments(contour)
                                cx = int(M["m10"]/M["m00"])
                                cy = int(M["m01"]/M["m00"])
                                cv2.circle(img,(cx,cy),pointersize,(255,255,255),-1)
                                x,y,w,h = cv2.boundingRect(contour)     
                                cv2.putText(img,"pH 7",(cx+5,cy),cv2.FONT_HERSHEY_SIMPLEX, fontsize, (255,255,255))  
                    
                #Tracking the darkgreen Color
                (contours,hierarchy)=cv2.findContours(darkgreen,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
                for pic, contour in enumerate(contours):
                        area = cv2.contourArea(contour)
                        if(area>minarea):
                                M = cv2.moments(contour)
                                cx = int(M["m10"]/M["m00"])
                                cy = int(M["m01"]/M["m00"])
                                cv2.circle(img,(cx,cy),pointersize,(255,255,255),-1)
                                x,y,w,h = cv2.boundingRect(contour)     
                                cv2.putText(img,"pH 8",(cx+5,cy),cv2.FONT_HERSHEY_SIMPLEX, fontsize, (255,255,255))  

                 #Tracking the blue Color
                (contours,hierarchy)=cv2.findContours(blue,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
                for pic, contour in enumerate(contours):
                        area = cv2.contourArea(contour)
                        if(area>minarea):
                                M = cv2.moments(contour)
                                cx = int(M["m10"]/M["m00"])
                                cy = int(M["m01"]/M["m00"])
                                cv2.circle(img,(cx,cy),pointersize,(255,255,255),-1)
                                x,y,w,h = cv2.boundingRect(contour)     
                                cv2.putText(img,"pH 9",(cx+5,cy),cv2.FONT_HERSHEY_SIMPLEX, fontsize, (255,255,255))  

                 #Tracking the violet Color
                (contours,hierarchy)=cv2.findContours(violet,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
                for pic, contour in enumerate(contours):
                        area = cv2.contourArea(contour)
                        if(area>minarea):
                                M = cv2.moments(contour)
                                cx = int(M["m10"]/M["m00"])
                                cy = int(M["m01"]/M["m00"])
                                cv2.circle(img,(cx,cy),pointersize,(255,255,255),-1)
                                x,y,w,h = cv2.boundingRect(contour)     
                                cv2.putText(img,"pH 10",(cx+5,cy),cv2.FONT_HERSHEY_SIMPLEX, fontsize, (255,255,255))  
                          

                
               
                cv2.imshow("Detecting.. press 's' to save image",img)
                key = cv2.waitKey(5)
                if  key &  0xFF == ord('q'):
                        cap.release()
                        cv2.destroyAllWindows()
                        break
                if  key  & 0xFF == ord('s'):
                        ROOT = tk.Tk()
                        ROOT.withdraw()  

                        file_name = simpledialog.askstring(title="Save image",
                                  prompt="Enter File name:")
                        name=str(file_name)+".jpg"
                        cv2.imwrite(name,img)
                                             
window = tk.Tk()
window.geometry("200x75")

def callback_from_camera():
        calculate_ph(0)
        
def callback_from_file():
        my_filetypes = [('all files', '.*'), ('Video files', '.mp4')]
        file_name = filedialog.askopenfilename(parent=window,initialdir=os.getcwd(),title="Please select a video file",filetypes=my_filetypes)
        calculate_ph(file_name)
        
button_camera = tk.Button(window, text="Feed from camera", command=callback_from_camera)
button_file = tk.Button(window, text="Import file", command=callback_from_file)
button_camera.grid(row=0,column=1)
button_file.grid(row=0,column=3)
tk.mainloop()
        
