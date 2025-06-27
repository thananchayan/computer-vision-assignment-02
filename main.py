import cv2
import os
import matplotlib.pyplot as plt
from utils.otsu_noise import add_gaussian_noise, apply_otsu
from utils.region_grow import region_growing

# Create output folder
output_dir = 'outputs'
os.makedirs(output_dir, exist_ok=True)

# Load your input image
image = cv2.imread('inputs/input.png')
if image is None:
    print("Error: Image not found.")
    exit()

# Display original image
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
plt.figure()
plt.title('Original Image')
plt.imshow(image_rgb)
plt.axis('off')
plt.savefig(os.path.join(output_dir, 'original_image.png'))
plt.show()

# Add Gaussian noise
noisy_image = add_gaussian_noise(image, mean=0, sigma=80)
noisy_rgb = cv2.cvtColor(noisy_image, cv2.COLOR_BGR2RGB)
plt.figure()
plt.title('Noisy Image')
plt.imshow(noisy_rgb)
plt.axis('off')
plt.savefig(os.path.join(output_dir, 'noisy_image.png'))
plt.show()

# Apply Otsu's thresholding
otsu_result = apply_otsu(noisy_image)
plt.figure()
plt.title('Otsu Thresholding Result')
plt.imshow(otsu_result, cmap='gray')
plt.axis('off')
plt.savefig(os.path.join(output_dir, 'otsu_result.png'))
plt.show()

# Interactive Seed Selection for Region Growing
plt.figure()
plt.title('Click to Select Seed Point')
plt.imshow(noisy_rgb)
plt.axis('off')
coords = plt.ginput(1)
plt.close()
seed_point = (int(coords[0][1]), int(coords[0][0]))
print(f"Selected seed point: {seed_point}")

# Apply Region Growing
region = region_growing(noisy_image, seed_point, threshold=50)
plt.figure()
plt.title('Region Growing Result')
plt.imshow(region, cmap='gray')
plt.axis('off')
plt.savefig(os.path.join(output_dir, 'region_growing_result.png'))
plt.show()

print(f"All results saved in the '{output_dir}' folder.")
