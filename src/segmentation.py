# src/segmentation.py

import cv2
import numpy as np

def detect_green_areas(image):
    """
    Detects green areas in the input image using HSV color thresholding.

    Args:
        image (numpy.ndarray): Input preprocessed image (normalized).

    Returns:
        mask (numpy.ndarray): Binary mask where green areas are white (255) and others are black (0).
    """
    # Convert image from RGB to BGR (since OpenCV loads as BGR)
    image_bgr = (image * 255).astype(np.uint8)

    # Convert BGR to HSV
    hsv = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2HSV)

    # Define green color range in HSV
    lower_green = np.array([35, 40, 40])
    upper_green = np.array([85, 255, 255])

    # Create mask
    mask = cv2.inRange(hsv, lower_green, upper_green)

    return mask
