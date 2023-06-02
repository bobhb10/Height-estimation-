import cv2
from tkinter import *
from PIL import Image, ImageTk

trained_face_data = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_fullbody.xml')
trained_face_data2 = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# img = cv2.imread('image1.jpg')
webcam = cv2.VideoCapture(1)
font = cv2.FONT_HERSHEY_SIMPLEX

# width_in_pixels = webcam.get(cv2.CAP_PROP_FRAME_WIDTH)
# print(f"width_in_pixels:{width_in_pixels}")
# height_in_pixels = webcam.get(cv2.CAP_PROP_FRAME_HEIGHT)
# print(f"height_in_pixels:{height_in_pixels}")

app = Tk()
app.title("Height Estimation")
# app.iconbitmap(r"C:\Users\mereu\PycharmProjects\pythonProject\Height_Estimation\Camera.ico")
# app.geometry("300x50")
# app.bind('<Escape>', lambda e: app.quit())

# app.geometry("600x600")

label_widget = Label(app)
label_widget.pack()


def open_camera():
    button1.pack_forget()
    successful_frame_read, frame = webcam.read()

    grayscaled_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    full_body_coordinates = trained_face_data.detectMultiScale(grayscaled_frame)
    face_coordinates = trained_face_data2.detectMultiScale(grayscaled_frame)

    x_face = 0
    y_face = 0

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
        # print(f"Height: {w - (x_face - x)} pixels")
        # print(f"Height:{w - (x_face - x)* 1.52} cm")
        if (w - (x_face - x)) > 100 & (w - (x_face - x)) < 130:
            cv2.putText(frame, f"{w - (x_face - x) * 1.52} cm", (50, 50), font, 1, (0, 0, 255), 2)

    color_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)  # Convert BGR to RGB

    captured_frame = Image.fromarray(color_frame)

    photo_frame = ImageTk.PhotoImage(image=captured_frame)

    label_widget.photo_frame = photo_frame

    # photo_frame = cv2.putText(image, 'OpenCV', org, font, fontScale, color, thickness, cv2.LINE_AA)

    label_widget.configure(image=photo_frame)

    label_widget.after(5, open_camera)


button1 = Button(app, text="Open Camera", command=open_camera)
button1.pack()

app.mainloop()

webcam.release()
print("Code Completed")

# distanta dintre camera si persoana este de 305 cm
# rezolutia la camera sa fie acceasi la aceasta distanta