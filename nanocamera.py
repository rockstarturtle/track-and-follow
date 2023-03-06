
import cv2
import torch
import nanocamera as nano



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
        a = (int(results.pandas().xyxy[0].xmax[i])-int(results.pandas().xyxy[0].xmin[i]))/2
        b = (int(results.pandas().xyxy[0].ymax[i])-int(results.pandas().xyxy[0].ymin[i]))/2
        list2 = [int(a), int(b)]
        y.append(list2)
        
# from nanocamera.NanoCam import Camera


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
