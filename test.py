import cv2
import torch




model = torch.hub.load('ultralytics/yolov5', 'yolov5s', force_reload=True)

def det(images):
    im2 = images[..., ::-1]  # OpenCV image (BGR to RGB)
    imgs = [im2]
    results = model(imgs, size=640)  # includes NMS
    x = []
    y = []
    for i in range(0,len(results.pandas().xyxy[0])):
        listem = [i,int(results.pandas().xyxy[0].xmin[i]),
        int(results.pandas().xyxy[0].ymin[i]),
        int(results.pandas().xyxy[0].xmax[i]),
        int(results.pandas().xyxy[0].ymax[i]),
        round(results.pandas().xyxy[0].confidence[i],2),
        results.pandas().xyxy[0].name[i]]
        x.append(listem)
        a = ((int(results.pandas().xyxy[0].xmax[i])-int(results.pandas().xyxy[0].xmin[i]))/2)+int(results.pandas().xyxy[0].xmin[i])
        b = ((int(results.pandas().xyxy[0].ymax[i])-int(results.pandas().xyxy[0].ymin[i]))/2)+int(results.pandas().xyxy[0].ymin[i])
        list2=[int(a),int(b)]
        y.append(list2)
    print(y)
    if len(x) >0:
        a=x[0]
        cv2.rectangle(images, (a[1],a[2]), (a[3],a[4]), (0, 255, 0), 2)
    return y
