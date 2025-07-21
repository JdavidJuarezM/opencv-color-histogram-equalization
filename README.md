# Opencv-color-histogram-equalization
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
