import cv2
import matplotlib.pyplot as plt
#reading image
image1=cv2.imread("displayer.jpg")
#converting bgr to rgb
image_rgb=cv2.cvtColor(image1,cv2.COLOR_BGR2RGB)
plt.imshow(image_rgb)
plt.title("RGB IMAGE")
plt.show()
#
#converting bgr to grayscale
image_GRAY=cv2.cvtColor(image1,cv2.COLOR_BGR2GRAY)
plt.imshow(image_GRAY)
plt.title("GRAY SCALE IMAGE")
plt.show()
#croping the image
cropped_image = image1[100:300, 200:400]
#converting into rgb
croped_rgb=cv2.cvtColor(cropped_image,cv2.COLOR_BGR2RGB)
plt.imshow(cropped_image)
plt.title("THE CROPED IMAGE")
plt.show()