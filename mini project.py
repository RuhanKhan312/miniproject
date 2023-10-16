import cv2
# tkinter GUI for making applications
from tkinter import *
from tkinter import ttk

root = Tk()
root.geometry('400x400')




def vid():
    vid = cv2.VideoCapture(0)
    while True:
        ret, video = vid.read()
        cv2.imshow('orgvideo', video)

        if cv2.waitKey(1) == ord('q'):
            break
    vid.release()

def img():
    img = cv2.imread("C:/Users/hp/Desktop/miniproject/miniproject/smilingman1.jpg")
    cv2.imshow('Andrew',img)

def gray_img():
    gray_img = cv2.imread("C:/Users/hp/Desktop/miniproject/miniproject/smilingman1.jpg")
    gray_img = cv2.cvtColor(gray_img,cv2.COLOR_BGR2GRAY)
    cv2.imshow("Gray Image",gray_img)

def HSV_img():
    HSV_img = cv2.imread("C:/Users/hp/Desktop/miniproject/miniproject/smilingman1.jpg")
    HSV_img = cv2.cvtColor(HSV_img, cv2.COLOR_BGR2HSV)
    cv2.imshow("HSV image",HSV_img)

def detect_face():
    face_cascade = cv2.CascadeClassifier("C:/Users/hp/Desktop/miniproject/miniproject/haarcascade_frontalface_default.xml")
    detect_face = cv2.imread("C:/Users/hp/Desktop/miniproject/miniproject/smilingman.jpg")
    faces = face_cascade.detectMultiScale(detect_face, scaleFactor=1.1, minNeighbors=5)

    for (x, y, w, h) in faces:
        cv2.rectangle(detect_face, (x, y), (x + w, y + h), (0, 255, 0), 2)

    cv2.imshow("Face detection", detect_face)

def detect_eyes():
    eye_cascade = cv2.CascadeClassifier("C:/Users/hp/Desktop/miniproject/miniproject/haarcascade_eye.xml")
    detect_eyes = cv2.imread("C:/Users/hp/Desktop/miniproject/miniproject/smilingman.jpg")
    eyes = eye_cascade.detectMultiScale(detect_eyes, scaleFactor=1.1, minNeighbors=5)

    for (x, y, w, h) in eyes:
        cv2.rectangle(detect_eyes, (x, y), (x +w, y + h), (0, 255, 0), 2)

    cv2.imshow("eye detection", detect_eyes)

def detect_smile():
    smile_cascade = cv2.CascadeClassifier("C:/Users/hp/Desktop/miniproject/miniproject/haarcascade_smile.xml")
    detect_smile = cv2.imread("C:/Users/hp/Desktop/miniproject/miniproject/smilingman.jpg")
    smile = smile_cascade.detectMultiScale(detect_smile, scaleFactor=1.1, minNeighbors=5)

    for (x, y, w, h) in smile:
        cv2.rectangle(detect_smile, (x, y), (x + w, y + h), (0, 255, 0), 2)

    cv2.imshow("smile detection", detect_smile)

def detect_all():
    # Load the pre-trained Haar cascades
    face_cascade = cv2.CascadeClassifier('C:/Users/hp/Desktop/miniproject/miniproject/haarcascade_frontalface_default.xml')
    eye_cascade = cv2.CascadeClassifier('C:/Users/hp/Desktop/miniproject/miniproject/haarcascade_eye.xml')
    smile_cascade = cv2.CascadeClassifier('C:/Users/hp/Desktop/miniproject/miniproject/haarcascade_smile.xml')

    # Load the image
    image = cv2.imread('C:/Users/hp/Desktop/miniproject/miniproject/smilingman.jpg')

    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Detect faces
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # Iterate over the detected faces
    for (x, y, w, h) in faces:
        # Draw a rectangle around the face
        cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2)

        # Extract the region of interest (ROI) within the face rectangle
        roi_gray = gray[y:y + h, x:x + w]
        roi_color = image[y:y + h, x:x + w]

        # Detect eyes within the face ROI
        eyes = eye_cascade.detectMultiScale(roi_gray)

        # Iterate over the detected eyes
        for (ex, ey, ew, eh) in eyes:
            # Draw a rectangle around each eye
            cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)

        # Detect smiles within the face ROI
        smiles = smile_cascade.detectMultiScale(roi_gray, scaleFactor=1.7, minNeighbors=22, minSize=(25, 25))

        # Iterate over the detected smiles
        for (sx, sy, sw, sh) in smiles:
            # Draw a rectangle around each smile
            cv2.rectangle(roi_color, (sx, sy), (sx + sw, sy + sh), (0, 0, 255), 2)

    # Display the resulting image
    cv2.imshow('Face Detection', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

Button(root, text="Open Web cam", bg="red", command=vid).place(x=50, y=20)
Button(root, text="Quit", command=root.destroy).place(x=50, y=70)
Button(root,text="Open Image",bg="red",fg="yellow",command=img).place(x=50,y=130)
Button(root,text="Gray Image",command=gray_img).place(x=50,y=180)
Button(root, text="HSV", command=HSV_img).place(x=50, y=230)
Button(root, text="Detect Face", command=detect_face).place(x=50, y=280)
Button(root, text="Detect eyes", command=detect_eyes).place(x=50, y=330)
Button(root, text="Detect smile", command=detect_smile).place(x=50, y=380)
Button(root, text="Detect all", command=detect_all).place(x=50, y=430)
root.mainloop()