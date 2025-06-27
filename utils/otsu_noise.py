import cv2
import numpy as np
from skimage.filters import threshold_otsu

def add_gaussian_noise(image, mean=0, sigma=80):
    gaussian_noise = np.random.normal(mean, sigma, image.shape)
    noisy_image = image + gaussian_noise
    noisy_image = np.clip(noisy_image, 0, 255).astype(np.uint8)
    return noisy_image

def apply_otsu(image):
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    threshold = threshold_otsu(gray_image)
    binary_image = (gray_image > threshold).astype(np.uint8) * 255
    print(f"Otsu threshold value: {threshold}")
    return binary_image
