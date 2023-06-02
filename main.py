import cv2

trained_face_data = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_fullbody.xml')
trained_face_data2 = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

webcam = cv2.VideoCapture(0)

x_face = 0
y_face = 0



while True:

    successful_frame_read, frame = webcam.read()

    grayscaled_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    full_body_coordinates = trained_face_data.detectMultiScale(grayscaled_frame)
    face_coordinates = trained_face_data2.detectMultiScale(grayscaled_frame)

    for (x, y, w, h) in face_coordinates:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        x_face = x
        y_face = y
        # print(f"Height: {h} pixels")
        # print(f"Height: {x} pixels")
        # print(f"Height: {y} pixels")
        # print(f"Height: {w} pixels")

    # print("#########################")
    for (x, y, w, h) in full_body_coordinates:
        cv2.rectangle(frame, (x + (x_face - x), y + (y_face - y)), (x + w - (x_face - x), y + h), (0, 255, 0), 2)
        # print(f"Height: {y+h} pixels")
        # print(f"Height: {x} pixels")
        # print(f"Height: {y} pixels")
        # print(f"Height: {x+w} pixels")
        print(f"Height: {w - (x_face - x)} pixels")

    cv2.imshow("Height Estimation",frame)
    key = cv2.waitKey(1)

    # Stop if K key is pressed
    if key == 75 or key == 107:
        break

webcam.release()
print("Code Completed")