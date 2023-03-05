import cv2
import test
from importlib import reload
reload(test)

cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    if not ret:
        break

    im = test.det(frame)
    cv2.imshow('image', im)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cv2.destroyAllWindows()
