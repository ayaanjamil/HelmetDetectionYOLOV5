import numpy as np
import torch
from matplotlib import pyplot as plt
import cv2

model = torch.hub.load('yolov5', 'custom', path='yolov5/runs/train/helmet_detection2/weights/last.pt', source='local')

cap = cv2.VideoCapture(0)
while cap.isOpened():
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)
    results = model(frame)
    cv2.imshow('lolz', np.squeeze(results.render()))

    if cv2.waitKey(10) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()