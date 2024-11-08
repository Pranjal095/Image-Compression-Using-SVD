import streamlit as st
from PIL import Image
import numpy as np
import cv2

image_path = './AuroraBorealis.jpg'
image = Image.open(image_path)
img_array = np.array(image)
img_array = cv2.cvtColor(img_array, cv2.COLOR_RGB2BGR)

def compress_image(k,img_array):
    b,g,r = cv2.split(img_array)

    compressed_channels = []
    for channel in [b,g,r]:
        U,E,vT = np.linalg.svd(channel)
        compressed_E = np.diagflat(E[:k])
        compressed_U = U[:,:k]
        compressed_vT = vT[:k,:]
        compressed_channel = np.matmul(np.matmul(compressed_U,compressed_E),compressed_vT)
        compressed_channel = (compressed_channel-np.min(compressed_channel)) / (np.max(compressed_channel)-np.min(compressed_channel))*255
        compressed_channels.append(compressed_channel.astype(np.uint8))
    
    compressed_img_array = cv2.merge(compressed_channels)
    return compressed_img_array

st.title("Image Compression with SVD")
st.write("Adjust the slider to change the value of k and see the effect on the image.")

k = st.slider('Select k value',min_value=1,max_value=min(img_array.shape[0],img_array.shape[1]),value=50)

compressed_img_array = compress_image(k,img_array)

st.image(cv2.cvtColor(compressed_img_array,cv2.COLOR_BGR2RGB), caption=f'Compressed Image with k={k}',use_column_width=True)
st.image(cv2.cvtColor(img_array, cv2.COLOR_BGR2RGB),caption='Original Image',use_column_width=True)
