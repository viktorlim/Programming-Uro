#Tugas URO Programming
#Victor Lim, 16524233, STEI-R
#Program dengan bahasa python ini bekerja untuk membuat batas persegi dari sebuah video lingkaran berwarna merah yang bergerak di background putih
#Program bekerja dengan bantuan OpenCV
import cv2, numpy as np

video_path = "C:/Users/User/Downloads/object_video.mp4"

cap = cv2.VideoCapture(video_path)

while True:
    ret, frame = cap.read()     
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blurred_frame = cv2.GaussianBlur(gray_frame, (15, 15), 0)
    circles = cv2.HoughCircles(
    blurred_frame, 
    cv2.HOUGH_GRADIENT, dp=1, minDist=50,
    param1=50, 
    param2=30,  
    minRadius=30,  
    maxRadius=150 
    )

    if circles is not None:
            circles = np.round(circles[0, :]).astype("int")
            for (x, y, r) in circles:
                top_left = (x - r, y - r)
                bottom_right = (x + r, y + r)
                cv2.rectangle(frame, top_left, bottom_right, (0, 0, 255), 2)

    cv2.imshow('Lingkaran dibatasi persegi', frame)

    if cv2.waitKey(5) & 0xFF == ord('x'):
        break

cap.release()
cv2.destroyAllWindows()
