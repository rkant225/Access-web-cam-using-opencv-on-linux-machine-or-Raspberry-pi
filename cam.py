import cv2
cap=cv2.VideoCapture(-1)
if(not cap.isOpened()):
    print("can't open camera")
else:
    while True:
        success,frame=cap.read()
        cv2.imshow("Captured:",frame)
        if(cv2.waitKey(1)==32):
            break
cap.release()        
