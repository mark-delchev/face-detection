import cv2

trained_face_data = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
img = cv2.imread("image2.jpg")
grayscaled_img = cv2.cvtColor( img, cv2.COLOR_BGR2GRAY)
face_coordinates = trained_face_data.detectMultiScale(grayscaled_img)
#print(face_coordinates)

for (x, y, w, h) in face_coordinates:
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)

if face_coordinates == ():
    print("There isn't a face in this image.")
else:
    cv2.imshow("Face detection", img)
    cv2.waitKey()

print("Code Completed")