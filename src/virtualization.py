# src/visualization.py

import matplotlib.pyplot as plt

def plot_images(past_img, past_mask, current_img, current_mask):
    """
    Plots past and current images along with their green masks.

    Args:
        past_img (numpy.ndarray): Past year image.
        past_mask (numpy.ndarray): Past year green mask.
        current_img (numpy.ndarray): Current year image.
        current_mask (numpy.ndarray): Current year green mask.
    """
    fig, axes = plt.subplots(2, 2, figsize=(12, 8))

    axes[0, 0].imshow(past_img)
    axes[0, 0].set_title('Past Year Image')
    axes[0, 0].axis('off')

    axes[0, 1].imshow(past_mask, cmap='gray')
    axes[0, 1].set_title('Past Year Green Areas')
    axes[0, 1].axis('off')

    axes[1, 0].imshow(current_img)
    axes[1, 0].set_title('Current Year Image')
    axes[1, 0].axis('off')

    axes[1, 1].imshow(current_mask, cmap='gray')
    axes[1, 1].set_title('Current Year Green Areas')
    axes[1, 1].axis('off')

    plt.tight_layout()
    plt.show()
