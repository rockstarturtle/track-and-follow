
import cv2
import argparse



def gstreamer_pipeline(
    sensor_id=0,
    capture_width=1920,
    capture_height=1080,
    display_width=960,
    display_height=540,
    framerate=30,
    flip_method=0,
):
    return (
        "nvarguscamerasrc sensor-id=%d !"
        "video/x-raw(memory:NVMM), width=(int)%d, height=(int)%d, framerate=(fraction)%d/1 ! "
        "nvvidconv flip-method=%d ! "
        "video/x-raw, width=(int)%d, height=(int)%d, format=(string)BGRx ! "
        "videoconvert ! "
        "video/x-raw, format=(string)BGR ! appsink"
        % (
            sensor_id,
            capture_width,
            capture_height,
            framerate,
            flip_method,
            display_width,
            display_height,
        )
    )


def show_camera():
    
    

    print(gstreamer_pipeline(flip_method=0))

video_capture = cv2.VideoCapture(gstreamer_pipeline(flip_method=0), cv2.CAP_GSTREAMER)
    
fileName = "/home/andrena/Desktop/vscodeprojects/webcammmm.mp4"
codec = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
frameRate = 30
resolution = (1920, 1080)

videoFileOutput = cv2.VideoWriter(fileName, codec, frameRate, resolution)

if video_capture.isOpened():
        try:
            window_handle = cv2.namedWindow("webcam", cv2.WINDOW_AUTOSIZE)
            while True:
                ret_val, frame = video_capture.read()
        
                if cv2.getWindowProperty('webcam', cv2.WND_PROP_AUTOSIZE) >= 0:
                    videoFileOutput.write(frame)
                    cv2.imshow('webcam', frame)

                else:
                    break 
                keyCode = cv2.waitKey(2) & 0xFF
                # Stop the program on the ESC key or 'q'
                if keyCode == 27 or keyCode == ord('q'):
                    break
        finally:
            videoFileOutput.release()
            video_capture.release()
            cv2.destroyAllWindows()
else:
        print("Error: Unable to open camera")


if __name__ == "__main__":
    show_camera()