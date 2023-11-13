import dlib
import cv2
import numpy as np
import glob

face_detector = dlib.get_frontal_face_detector()


for img in glob.glob("image/*.jpg"):
    img = cv2.imread(img)
    for f in face_detector(img):
        
        # img = np.float32(img)
        cv2.rectangle(img, (f.left(), f.top()), (f.right(), f.bottom()), (255, 0, 0), 2)
    
    print(img.shape)
    change_size = 1000
    img = cv2.resize(img, dsize=(int(img.shape[1]*change_size/img.shape[0]), change_size))
    cv2.imshow("1", img)
    cv2.waitKey(0) 