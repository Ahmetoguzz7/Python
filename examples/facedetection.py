import cv2
import mediapipe as mp
mp_face_detection=mp.solutions.face_detection.FaceDetection()
mp_drawing=mp.solutions.drawing_uilts

webcam=cv2.VideoCapture(0)

while webcam.isOpened():
    success,img=webcam.read()

    img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    results=mp_face_detection.process(img)
    
    img=cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
    if results.detections:
        for detection in results.detections:
            mp_drawing.draw_detection(img,detection)
    cv2.imshow("koolac",img)
    if cv2.waitkey(5) & 0xFF == ord("q"):
        break

webcam.release()
cv2.destroyAllWindows()