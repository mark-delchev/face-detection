import cv2
trained_face_data = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
img = cv2.imread("image2.jpg")
grayscaled_img = cv2.cvtColor( img, cv2.COLOR_BGR2GRAY)

cv2.imshow("Boyko", grayscaled_img)
cv2.waitKey()
print("Code Completed")