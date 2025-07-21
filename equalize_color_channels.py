# -*- coding: utf-8 -*-
"""
Performs histogram equalization on each color channel of an image.

This script loads a color image, separates its BGR channels, and applies
histogram equalization to each channel independently. It saves the
resulting image and the histograms for each channel before and after
equalization.

Dependencies:
    - opencv-python
    - matplotlib
    - numpy

Usage:
    1. Save this script in a folder.
    2. Place an input image named 'input_image.jpg' in the same folder.
    3. Run the script. All output files will be saved to a new
       'output_color/' subfolder.
"""
import cv2
import matplotlib.pyplot as plt
import os

# --- CONFIGURATION ---
INPUT_IMAGE_PATH = 'input_image.jpg'
OUTPUT_FOLDER = 'output_color'

# Create the output directory if it doesn't exist.
if not os.path.exists(OUTPUT_FOLDER):
    os.makedirs(OUTPUT_FOLDER)
    print(f"Created directory: {OUTPUT_FOLDER}")

# Verify the input image exists.
if not os.path.isfile(INPUT_IMAGE_PATH):
    print(f"Error: Input image not found at '{INPUT_IMAGE_PATH}'")
    exit()

def plot_and_save_histogram(channel_data, color_name, title_suffix):
    """
    Plots, shows, and saves the histogram for a single color channel.

    Args:
        channel_data (numpy.ndarray): The image data for the channel.
        color_name (str): The name of the color (e.g., 'blue', 'green').
        title_suffix (str): Suffix for the plot title (e.g., 'Original').
    """
    plt.figure()
    plt.title(f"{color_name.title()} Channel Histogram ({title_suffix})")
    plt.xlabel("Pixel Intensity")
    plt.ylabel("Number of Pixels")
    plt.hist(channel_data.ravel(), bins=256, range=[0, 256], color=color_name.lower())
    
    # Sanitize filename for saving
    filename = f"histogram_{color_name}_{title_suffix.lower()}.png"
    save_path = os.path.join(OUTPUT_FOLDER, filename)
    plt.savefig(save_path)
    print(f"Saved {filename}")
    # plt.show() # Uncomment to display plots during script execution

# --- PROCESSING ---
# 1. Load the color image.
color_image = cv2.imread(INPUT_IMAGE_PATH)

# 2. Split the image into its B, G, R channels.
blue_channel, green_channel, red_channel = cv2.split(color_image)

# 3. Plot histograms for the original channels.
print("--- Analyzing Original Channels ---")
plot_and_save_histogram(blue_channel, 'blue', 'Original')
plot_and_save_histogram(green_channel, 'green', 'Original')
plot_and_save_histogram(red_channel, 'red', 'Original')

# 4. Equalize each channel independently.
print("\n--- Equalizing Channels ---")
blue_eq = cv2.equalizeHist(blue_channel)
green_eq = cv2.equalizeHist(green_channel)
red_eq = cv2.equalizeHist(red_channel)

# 5. Merge the equalized channels back into a color image.
equalized_color_image = cv2.merge((blue_eq, green_eq, red_eq))
output_image_path = os.path.join(OUTPUT_FOLDER, 'equalized_color_image.jpg')
cv2.imwrite(output_image_path, equalized_color_image)
print(f"Saved equalized_color_image.jpg")

# 6. Plot histograms for the equalized channels.
print("\n--- Analyzing Equalized Channels ---")
plot_and_save_histogram(blue_eq, 'blue', 'Equalized')
plot_and_save_histogram(green_eq, 'green', 'Equalized')
plot_and_save_histogram(red_eq, 'red', 'Equalized')

print(f"\nProcessing complete. Check the '{OUTPUT_FOLDER}' folder.")