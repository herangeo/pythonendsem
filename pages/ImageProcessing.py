 

import streamlit as st
import cv2
from PIL import Image
import numpy as np

def process_image(image, processing_techniques):
    new_image = image.copy()



    if "Image Cropping" in processing_techniques:

        new_image = new_image[50:150, 50:150]

    if "Conversion" in processing_techniques:
        pass

    if "Resize" in processing_techniques:
        new_image = cv2.resize(new_image, (200, 200))

    if "Image Rotation" in processing_techniques:

        rows, cols = new_image.shape[:2]
        new_image = cv2.warpAffine(new_image,cv2.getRotationMatrix2D((cols / 2, rows / 2), 45, 1), (cols, rows))

    if "Grayscale" in processing_techniques:
        new_image = cv2.cvtColor(new_image, cv2.COLOR_BGR2GRAY)


    return new_image
def main():
    st.title("Process Your Images")

    col1, col2 = st.columns([1, 1])

    with col1:
            image = Image.open("image2.jpg")
            st.image(cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR), caption="Image", use_column_width=True)

    with col2:
            processing_techniques = st.multiselect("Choose the techniques",
                                ["Resize", "Grayscale", "Conversion", "Image Cropping", "Image Rotation"])
            if st.button("Process"):
                new_image = process_image(cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR), processing_techniques)
                st.image(new_image, caption="Processed Image", use_column_width=True)
        
        






if __name__ == "__main__":
    main()


    
