# 🧠 Computer Vision Assignment 2

This repository contains the solutions for **EE7204 – Computer Vision and Image Processing: Take Home Assignment 2**. The project demonstrates advanced image processing techniques including **Gaussian noise addition**, **Otsu's thresholding**, and **region-growing segmentation** using Python and OpenCV.

---

## 📂 Folder Structure

```
image-processing-assignment-02/
├── main.py                       # Main script to run all tasks
├── utils/
│   ├── otsu_noise.py             # Functions for Otsu thresholding with noise
│   └── region_grow.py            # Region growing segmentation
├── inputs/
│   └── input.png       # Synthetic image with 3 intensity levels
├── outputs/                      # Output results (thresholds, segmentations)
├── README.md                     # This file
```

---

## ✅ Tasks Implemented

### 1. Gaussian Noise + Otsu’s Thresholding

- Generates a synthetic grayscale image with 2 objects and a background.
- Adds **Gaussian noise** to the image.
- Applies **Otsu's thresholding** to segment the image.

### 2. Region Growing Segmentation

- Starts from a **seed pixel** within the object.
- Grows the region by including neighboring pixels within a **value threshold**.
- Produces a binary segmentation mask.

---

## 🚀 How to Run

### 🧰 Step 1: Clone the Repository

```bash
git clone https://github.com/thananchayan/image-processing-assignment-02.git
cd image-processing-assignment-02
```

---

### 🐍 Step 2: Create & Activate a Virtual Environment

#### 🔹 Windows

```bash
python -m venv venv
venv\Scripts\activate
```

---

### 📦 Step 3: Install Required Libraries

```bash
pip install opencv-python numpy matplotlib
```

---

### ▶️ Step 4: Run the Assignment Code

```bash
python main.py
```

All results will be saved inside the `outputs/` folder.

---

## 🖼️ Output Samples

- `original.png`: Synthetic base image with 3 pixel values
- `noisy.png`: Gaussian-noisy version of the image
- `otsu_result.png`: Thresholded image using Otsu’s method
- `region_grow.png`: Output of region-growing segmentation

