# -*- coding: utf-8 -*-
"""
Created on Thu Sep 30 12:13:28 2021

@author: Admin
"""
#for image processing 
import cv2
import torch

model = torch.hub.load('ultralytics/yolov5', 'yolov5m')

imgs = []
for i in range(21):
    path = './test/s' + str(i+1) + '.jpg'
    imgs.append(cv2.imread(path))

# Inference
results = model(imgs, size=640)  # includes NMS

# Results
results.print()
# results.save()  # or .show()
for i in range(21):
    print(results.pandas().xyxy[i].name.unique())
    
    #for image processing 
    import cv2
import torch

model = torch.hub.load('ultralytics/yolov5', 'yolov5m')

cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)

while True:
    success, frame = cap.read()
    if success:
        # Inference
        results = model(frame, size=640)  # includes NMS

        # Results
        results.print()
        results.save()  # or .show()
        print(results.pandas().xyxy[0].name.unique())
    else:
        print('HEY')  # For debugging purposes