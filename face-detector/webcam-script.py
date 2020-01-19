import cv2, time
while True:
    video = cv2.VideoCapture(0)
    check, frame = video.read()
    print(check)
    print(frame)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#     time.sleep(3)
    cv2.imshow("Capturning",gray)
    key = cv2.waitKey(1000)
    if key == ord('q'):
        break

video.release()
cv2.destroyAllWindows()