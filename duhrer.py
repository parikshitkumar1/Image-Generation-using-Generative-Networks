from torchvision import models, transforms
import torch
from PIL import Image
import torch.nn as nn
import streamlit as st
from utils import *

st.markdown(
    """
    <style>
    .reportview-container {
        background: url("https://user-images.githubusercontent.com/52780573/110473221-4efd2f80-8104-11eb-9b61-577ab3d2d584.png")
    }
   .sidebar .sidebar-content {
        background: url("url_goes_here")
    }
    </style>
    """,
    unsafe_allow_html=True
)



st.title("Dürer")



st.subheader("generative adversarial network generated Albrecht Dürer paintings")


st.write("Reload for more paintings")


  #plt.imshow(results)

  
for i in range(1,4):
	new()

#st.image(["training.gif"],height=70, width = 70)

st.markdown("![image](https://user-images.githubusercontent.com/52780573/110349151-6d0d5600-8058-11eb-8f61-6537f7119b43.png)")

st.markdown("![ezgif-4-e34793170921](https://user-images.githubusercontent.com/52780573/110349231-844c4380-8058-11eb-8a61-0290d814020f.gif)")












                                     



