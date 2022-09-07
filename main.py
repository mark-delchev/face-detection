import cv2
trained_face_data = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
img = cv2.imread("image1.jpeg")
cv2.imshow("Elon Musk", img)
cv2.waitKey()
print("Code Completed")