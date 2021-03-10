import cv2
from cv2 import dnn_superres
from torchvision import models, transforms
import torch
from PIL import Image
import torch.nn as nn
import streamlit as st

image_size = 64
batch_size = 32
stats = (0.5, 0.5, 0.5), (0.5, 0.5, 0.5)
latent_size = 150

def denorm(img_tensors):
    return img_tensors * stats[1][0] + stats[0][0]



def resolute():
	generator = torch.load("WEIGHTS/w2.pth", map_location = "cpu")
	generator.eval()	
	device = torch.device('cpu')
	generator.to(device);
	y = generator(torch.randn(batch_size, latent_size, 1, 1))
	gen_imgs = denorm(y.detach())
	to_pil_image = transforms.ToPILImage()
	result1 = to_pil_image(gen_imgs[0])
	result2 = to_pil_image(gen_imgs[1])
	result3 = to_pil_image(gen_imgs[2])
	newsize = (70,70) 
	im1 = result1.resize(newsize)
	im2 = result2.resize(newsize)
	im3 = result3.resize(newsize)
	im1 = im1.save("SUPERSAMPLES/new.jpg",quality=100)
	im2 = im2.save("SUPERSAMPLES/new1.jpg",quality=100)
	im3 = im3.save("SUPERSAMPLES/new2.jpg",quality=100)

	sr = dnn_superres.DnnSuperResImpl_create()

	image = cv2.imread('./SUPERSAMPLES/new.jpg')
	image2 = cv2.imread('./SUPERSAMPLES/new1.jpg')
	image3 = cv2.imread('./SUPERSAMPLES/new2.jpg')

	path = "LapSRN_x8.pb"
	sr.readModel(path)

	sr.setModel("lapsrn", 8)

	result = sr.upsample(image)
	result1 = sr.upsample(image2)
	result2 = sr.upsample(image3)



	cv2.imwrite("./SUPERSAMPLES/supernew.png", result)
	cv2.imwrite("./SUPERSAMPLES/supernew1.png", result1)
	#cv2.imwrite("./SUPERSAMPLES/supernew2.png", result2)
