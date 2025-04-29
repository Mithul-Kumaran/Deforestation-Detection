# src/analysis.py

import numpy as np

def calculate_green_percentage(mask):
    """
    Calculates the percentage of green areas in the image.

    Args:
        mask (numpy.ndarray): Binary mask with green areas.

    Returns:
        float: Green area percentage.
    """
    total_pixels = mask.size
    green_pixels = np.count_nonzero(mask)

    green_percentage = (green_pixels / total_pixels) * 100

    return green_percentage

def detect_deforestation(past_percentage, current_percentage, threshold=5.0):
    """
    Detects if deforestation has occurred based on green cover drop.

    Args:
        past_percentage (float): Green cover percentage in past image.
        current_percentage (float): Green cover percentage in current image.
        threshold (float): Minimum percentage drop to consider as deforestation.

    Returns:
        bool: True if deforestation detected, False otherwise.
    """
    drop = past_percentage - current_percentage

    if drop >= threshold:
        return True
    else:
        return False
