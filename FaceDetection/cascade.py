import cv2


"""
def mycascade(cap,face_cascade):
    while True:
        
        success, img = cap.read()

        if not success:
            break
        else:
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(gray, 1.1, 4)

            for (x, y, w, h) in faces:
                cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)

            ret,buffer = cv2.imencode('.jpg',img)
            img = buffer.tobytes()
            yield (b'--img\r\n'
                    b'Content-Type: image/jpeg\r\n\r\n' + img + b'\r\n')  # concat frame one by one and show result

"""



def mycascade(camera, face_cascade):
    while True:
        # Capture frame-by-frame
        
        success, frame = camera.read()  # read the camera frame
        
        if not success:
            break
        else:
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(gray, 1.1, 4)

            for (x, y, w, h) in faces:
                cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')  # concat frame one by one and show result

