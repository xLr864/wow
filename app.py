import streamlit as st 
from PIL import Image
import pickle
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os

st.set_option('deprecation.showfileUploaderEncoding', False)

html_temp = """
   <head>
      <title>Adivision By Chetan Khatri</title>
   </head>
   <div class="" style="background-color:blue;" >
   <div class="clearfix">           
   <div class="col-md-12">
   <center><p style="font-size:40px;color:white;margin-top:10px;">Poornima Institute of Engineering & Technology</p></center> 
   <center><p style="font-size:30px;color:white;margin-top:10px;">Digital Image Processing lab</p></center> 
   </div>
   </div>
   </div>
   """
st.markdown(html_temp,unsafe_allow_html=True)
  
st.title("""
        Addivision
         """
         )
file= st.file_uploader("Please upload image", type=("jpg", "png"))
ch = st.selectbox("What do you want to do",("subtraction of value 255","multiplication of value 0.5"))


import cv2 
from  PIL import Image, ImageOps
def import_and_predict(my_img1):
  if(ch=="subtraction of value 255"):
    print("Addition\n")
    image_data = cv2.subtract(my_img1, 255)
#     cv2.imshow("image_data",image_data)
  elif(ch=="multiplication of value 0.5"):
    print("Division\n")
    image_data = cv2.multiply(my_img1, 0.5)
#     cv2.imshow("image_data",image_data)

  st.image(image_data, use_column_width=True)
  return 0
if file is None:
  st.text("Please upload an Image file")
else:
  file_bytes = np.asarray(bytearray(file.read()), dtype=np.uint8)
  my_img1 = cv2.imdecode(file_bytes, 1)
  st.image(file,caption='Uploaded Image.', use_column_width=True)
    
if st.button("Perform "):
  result=import_and_predict(my_img1)
  
if st.button("About"):
  st.header(" Chetan")
  st.subheader("Student, Department of Computer Engineering")
html_temp = """
   <div class="" style="background-color:orange;" >
   <div class="clearfix">           
   <div class="col-md-12">
   <center><p style="font-size:20px;color:white;margin-top:10px;">Digital Image processing Experiment</p></center> 
   </div>
   </div>
   </div>
   """
st.markdown(html_temp,unsafe_allow_html=True)
