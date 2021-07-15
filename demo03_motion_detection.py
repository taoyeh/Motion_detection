import cv2
import face_recognition
import datetime

#打开摄像头并且展示数据

camera= cv2.VideoCapture(0)
while True:
    ret,frame=camera.read()
    cv2.putText(frame, "Motion: Undetected", (10,20), cv2.FONT_HERSHEY_DUPLEX, 0.5, (0,255,0), 1)
    cv2.putText(frame, datetime.datetime.now().strftime("%A %d %B %Y %I:%M%S%p"),
                (10, frame.shape[0]-10), cv2.FONT_HERSHEY_DUPLEX, 0.35, (0, 255, 0), 1)

    cv2.imshow("Video", frame)
    if cv2.waitKey(1) & 0XFF == ord('q'):
        break

# 释放资源
camera.release()
cv2.destroyAllWindows()
