# Helmet Detection Using YOLOV5

```python
python -m pip install ultralytics torch torchvision
cd yolov5
python detect detect.py --weights runs/train/helmet_detection2/weights/last.pt --img 640 --conf 0.25 --source 0

```

I made this Helmet Detection Model using YOLOv5 with a dataset I came across on Kaggle.

## Running it on normal traffic

![1.jpg](/images/1.jpg)

![2.jpg](/images/2.jpg)

This can be used at traffic signals to automatically detect riders who are not wearing helmet.

This model can smartly differentiatiate between a helmet in frame and a helmet on a person's head.

## Running it on CCTV footage

![3.jpg](/images/3.jpg)

![4.jpg](/images/4.jpg)

This can be used in ATMs to see whether someone is wearing a helmet or not.
