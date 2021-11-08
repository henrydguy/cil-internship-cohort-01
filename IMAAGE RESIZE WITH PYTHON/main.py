import cv2
print('man')

img = cv2.imread("./download.jfif")

print(img.shape)

imgResize =cv2.resize(img,(150,250))
print(imgResize.shape) #to confirm the resized dimension
cv2.imshow("output",img)
cv2.imshow("Resized image",imgResize)

cv2.waitKey(0)


