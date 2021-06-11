import cv2
'''camera = cv2.VideoCapture(0, cv2.CAP_DSHOW)
img_arr = []
for _ in range(50):
	ret_value,image = camera.read()
	img_arr.append(image)

for each in img_arr:
	cv2.imshow("image.png",each)
	print(each.shape)
	cv2.waitKey(0)
del(camera)
'''

cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)
ret_value , image = cam.read()
cv2.imshow("image.png",each)
print(image)
cv2.waitKey(0)
del(cam)