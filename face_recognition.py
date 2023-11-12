import dlib
import cv2
import numpy as np

face_detector = dlib.get_frontal_face_detector()

test_img = cv2.imread("image/2.jpg")
img = np.float32(test_img)

for f in face_detector(test_img):
    cv2.rectangle(test_img, (f.left(), f.top()), (f.right(), f.bottom()), (255, 0, 0), 2)

cv2.imshow("1", test_img)
cv2.waitKey(0)