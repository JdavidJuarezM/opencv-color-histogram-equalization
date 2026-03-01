<div align="center">

# 📊 OpenCV Color Histogram Equalization

**A computer vision script for enhancing color image contrast using OpenCV**

[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](#)
[![OpenCV](https://img.shields.io/badge/OpenCV-5C3EE8?style=for-the-badge&logo=opencv&logoColor=white)](#)
[![Data Visualization](https://img.shields.io/badge/Data_Viz-FF6F00?style=for-the-badge&logo=python&logoColor=white)](#)

*A Python-based image processing utility that splits BGR/RGB channels, independently equalizes their histograms to improve contrast, and generates visual plots of the before-and-after distributions.*

</div>

<br />

## 📑 Table of Contents
- [✨ Key Features](#-key-features)
- [🏗️ Architecture & Structure](#️-architecture--structure)
- [🚀 Getting Started](#-getting-started)
  - [Prerequisites](#prerequisites)
  - [Execution](#execution)
- [🛠️ Tech Stack](#️-tech-stack)

---

## ✨ Key Features

* **✔️ Color Channel Separation:** Effectively splits color images into their respective Blue, Green, and Red (BGR) channels.
* **✔️ Independent Equalization:** Applies histogram equalization to each color channel independently to drastically improve image contrast and dynamic range.
* **✔️ Visual Reporting:** Automatically generates and saves detailed plot graphs (`.png`) comparing the original vs. equalized histograms for every color channel.
* **✔️ Automated Output Generation:** Merges the processed channels back into a single cohesive image and organizes all outputs into a dedicated directory.

---

## 🏗️ Architecture & Structure

The repository is kept simple and lightweight, focusing on the core image processing logic:

```text
opencv-color-histogram-equalization/
├── equalize_color_channels.py    # Main computer vision and plotting script
├── input_image.jpg               # Sample input image to process
├── output_color/                 # Automatically generated outputs
│   ├── equalized_color_image.jpg # The final contrast-enhanced image
│   ├── histogram_blue_*.png      # Blue channel histograms (Original/Equalized)
│   ├── histogram_green_*.png     # Green channel histograms (Original/Equalized)
│   └── histogram_red_*.png       # Red channel histograms (Original/Equalized)
└── README.md                     # Project documentation
```

---

## 🚀 Getting Started

### Prerequisites

To run this project, ensure you have Python installed on your local machine along with the required computer vision libraries:

* **Python:** Version 3.x
* **OpenCV:** For image processing (`cv2`)
* **Matplotlib:** For generating histogram plot visualizations

You can install the required dependencies using pip:
```bash
pip install opencv-python matplotlib
```

### Execution

1. Clone this repository to your local machine:
   ```bash
   git clone <your-repository-url>
   ```
2. Navigate to the project directory:
   ```bash
   cd opencv-color-histogram-equalization
   ```
3. Run the Python script:
   ```bash
   python equalize_color_channels.py
   ```
4. The script will read `input_image.jpg`, process it, and save the resulting image and plots inside the `output_color/` folder.

---

## 🛠️ Tech Stack

* **Python** - Core programming language
* **OpenCV (`cv2`)** - Computer Vision and image array manipulation
* **Matplotlib (`pyplot`)** - Mathematical plotting and histogram generation

<br />

<div align="center">
  <i>Developed with ☕ to explore Image Processing and Computer Vision.</i>
</div>
