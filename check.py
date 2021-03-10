import cv2
from cv2 import dnn_superres


sr = dnn_superres.DnnSuperResImpl_create()


image = cv2.imread('./new6.jpg')

path = "LapSRN_x8.pb"
sr.readModel(path)

sr.setModel("lapsrn", 8)


result = sr.upsample(image)


cv2.imwrite("./upscaled.png", result)

