import cv2
import numpy as np
from PIL import Image

def process_image(uploaded_file):
    image = Image.open(uploaded_file)
    image = np.array(image)
    image = cv2.resize(image, (224, 224))
    return image
