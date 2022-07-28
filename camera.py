import cv2  #importing cv2
from pygame import mixer  #importing for our opinion sound

mixer.init()
mixer.music.load('AnyConv.com__sound.mp3')       #Police Sound

camera = cv2.VideoCapture(0)

while camera.isOpened():     # calling loop
    r, frame = camera.read()  # calling to rate frame
    r, newframe = camera.read()  # dupplicate frame (to see the difference)
    differ = cv2.absdiff(frame, newframe)  # differ refers difference
    gray = cv2.cvtColor(differ,cv2.COLOR_RGB2GRAY)  # changing the color RGB colours to gray (like black and white)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)  # Bluring the image
    _, threshold = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)

    dilate = cv2.dilate(threshold, None, iterations=3)
    contours,_ = cv2.findContours(dilate, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    for c in contours:
        if cv2.contourArea(c) < 5000:
            continue
        x,y,w,h = cv2.boundingRect(c)

        cv2.rectangle(frame, (x,y), (x+w,y+h), (0,255,0), 2)    #0,255,0=green color

        mixer.music.play()  #to get a sound it will be play music in the above

    if cv2.waitKey(10) == ord('q'):   # calling the key to close window
        break
    cv2.imshow('Granny cam', frame)    #showing opencv
