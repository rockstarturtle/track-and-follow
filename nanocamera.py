
import cv2
import torch
import nanocamera as nano

model = torch.hub.load('ultralytics/yolov5', 'yolov5s', force_reload=True)

def det(frame):
    im2 = frame[..., ::-1]  # OpenCV image (BGR to RGB)
    imgs = [im2]
    results = model(imgs, size=640)  # includes NMS
    detections = []
    xy = []
    for i in range(0,len(results.pandas().xyxy[0])):
        xmin=int(results.pandas().xyxy[0].xmin[i])
        ymin=int(results.pandas().xyxy[0].ymin[i])
        ymax=int(results.pandas().xyxy[0].ymax[i])
        xmax=int(results.pandas().xyxy[0].xmax[i])
        conf=round(results.pandas().xyxy[0].confidence[i],2)
        detection = [i, xmin, ymin ,xmax, ymax, conf ,results.pandas().xyxy[0].name[i]]
        detections.append(detection)
        x = (xmax-xmin)/2+xmin
        y = (ymax-ymin)/2+ymin
        list2=[int(x),int(y)]
        xy.append(list2)
    
    if len(xy) >0:
        a=detections[0]
        cv2.rectangle(frame, (a[1],a[2]), (a[3],a[4]), (0, 255, 0), 2)
    return xy
from nanocamera.NanoCam import Camera


if __name__ == '__main__':
    # Create the Camera instance
    camera = nano.Camera(flip=0, width=640, height=480, fps=30)
    # For multiple CSI camera
    # camera_2 = nano.Camera(device_id=1, flip=0, width=1280, height=800, fps=30)
    print('CSI Camera is now ready')
    while True:
        try:
            # read the camera image
            frame = camera.read()
            # display the frame
            im = det(frame)
            cv2.imshow("Video Frame", im)
            if cv2.waitKey(25) & 0xFF == ord('q'):
                break
        except KeyboardInterrupt:
            break

    # close the camera instance
    camera.release()

    # remove camera object
    del camera
