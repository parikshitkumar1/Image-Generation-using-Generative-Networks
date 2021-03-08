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


def new():
	for i in range(1,2):
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
	  result4 = to_pil_image(gen_imgs[3])
	  result5 = to_pil_image(gen_imgs[4])
	  result6 = to_pil_image(gen_imgs[5])
	  result7 = to_pil_image(gen_imgs[6]) 
	  result8 = to_pil_image(gen_imgs[7]) 
	  result9 = to_pil_image(gen_imgs[8]) 

	  newsize = (70,70) 
	  im1 = result1.resize(newsize)
	  im2 = result2.resize(newsize)
	  im3 = result3.resize(newsize)
	  im4 = result4.resize(newsize)
	  im5 = result5.resize(newsize)
	  im6 = result6.resize(newsize) 
	  im7 = result7.resize(newsize)
	  im8 = result8.resize(newsize)
	  im9 = result9.resize(newsize)

	  im1 = im1.save("SAMPLES/new.jpg",quality=100)
	  im2 = im2.save("SAMPLES/new1.jpg",quality=100)
	  im3 = im3.save("SAMPLES/new2.jpg",quality=100)
	  im4 = im4.save("SAMPLES/new3.jpg",quality=100)
	  im5 = im5.save("SAMPLES/new4.jpg",quality=100)
	  im6 = im6.save("SAMPLES/new5.jpg",quality=100)
	  im7 = im7.save("SAMPLES/new6.jpg",quality=100)
	  im8 = im8.save("SAMPLES/new7.jpg",quality=100)
	  im9 = im9.save("SAMPLES/new8.jpg",quality=100)

	  st.image(["SAMPLES/new.jpg","SAMPLES/new1.jpg","SAMPLES/new2.jpg","SAMPLES/new3.jpg","SAMPLES/new4.jpg","SAMPLES/new5.jpg","SAMPLES/new6.jpg","SAMPLES/new7.jpg"],width = 70)


	for i in range(1,2):
	  generator = torch.load("WEIGHTS/w1.pth", map_location = "cpu")
	  generator.eval()	
	  device = torch.device('cpu')
	  generator.to(device);
	  y = generator(torch.randn(batch_size, latent_size, 1, 1))
	  gen_imgs = denorm(y.detach())
	  to_pil_image = transforms.ToPILImage()
	  result1 = to_pil_image(gen_imgs[0])
	  result2 = to_pil_image(gen_imgs[1])
	  result3 = to_pil_image(gen_imgs[2])
	  result4 = to_pil_image(gen_imgs[3])
	  result5 = to_pil_image(gen_imgs[4])
	  result6 = to_pil_image(gen_imgs[5])
	  result7 = to_pil_image(gen_imgs[6]) 
	  result8 = to_pil_image(gen_imgs[7]) 
	  result9 = to_pil_image(gen_imgs[8]) 

	  newsize = (70,70) 
	  im1 = result1.resize(newsize)
	  im2 = result2.resize(newsize)
	  im3 = result3.resize(newsize)
	  im4 = result4.resize(newsize)
	  im5 = result5.resize(newsize)
	  im6 = result6.resize(newsize) 
	  im7 = result7.resize(newsize)
	  im8 = result8.resize(newsize)
	  im9 = result9.resize(newsize)

	  im1 = im1.save("SAMPLES/new.jpg",quality=100)
	  im2 = im2.save("SAMPLES/new1.jpg",quality=100)
	  im3 = im3.save("SAMPLES/new2.jpg",quality=100)
	  im4 = im4.save("SAMPLES/new3.jpg",quality=100)
	  im5 = im5.save("SAMPLES/new4.jpg",quality=100)
	  im6 = im6.save("SAMPLES/new5.jpg",quality=100)
	  im7 = im7.save("SAMPLES/new6.jpg",quality=100)
	  im8 = im8.save("SAMPLES/new7.jpg",quality=100)
	  im9 = im9.save("SAMPLES/new8.jpg",quality=100)

	  st.image(["SAMPLES/new.jpg","SAMPLES/new1.jpg","SAMPLES/new2.jpg","SAMPLES/new3.jpg","SAMPLES/new4.jpg","SAMPLES/new5.jpg","SAMPLES/new6.jpg","SAMPLES/new7.jpg"],width = 70)   

