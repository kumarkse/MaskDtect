import numpy as np
import matplotlib.pyplot as plt
from PIL import Image



def process(input_img_path ):
    image = Image.open(input_img_path)
    plt.imshow(image)
    image = image.resize((128,128))
    plt.imshow(image)
    image = image.convert('RGB')
    plt.imshow(image)
    image = np.array(image)
    img_scaled= image/255

    img_scaled = np.reshape(img_scaled,[1,128,128,3])
    return img_scaled