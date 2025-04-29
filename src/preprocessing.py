# # src/preprocessing.py

# import cv2
# import os


# # def load_and_preprocess(image_path, target_size=(512, 512)):
# #     """
# #     Loads an image, resizes it, and normalizes pixel values.

# #     Args:
# #         image_path (str): Path to the image file.
# #         target_size (tuple): Desired image size (width, height).

# #     Returns:
# #         image (numpy.ndarray): Preprocessed image.
# #     """
# #     # Load the image
# #     image = cv2.imread(image_path)

# #     if image is None:
# #         raise ValueError(f"Failed to load image at {image_path}")

# #     # Resize image
# #     image = cv2.resize(image, target_size)

# #     # Normalize pixel values (optional)
# #     image = image / 255.0

# #     return image
# def load_and_preprocess(image_path):
#     print(f"Image path: {image_path}, Type: {type(image_path)}")
#     if not isinstance(image_path, (str, bytes, os.PathLike)):
#         raise TypeError("Expected image_path to be a string or path-like object")
    
#     image = cv2.imread(image_path)
#     if image is None:
#         raise FileNotFoundError(f"Failed to load image from path: {image_path}")
    
#     # continue preprocessing...
#     return image



import os
import cv2
import numpy as np

def load_and_preprocess(image_file, target_size=(512, 512)):
    """
    Loads an uploaded image file, resizes it, and normalizes pixel values.

    Args:
        image_file: A file-like object (e.g., from Streamlit's file_uploader)
        target_size (tuple): Desired image size (width, height)

    Returns:
        image (numpy.ndarray): Preprocessed image
    """
    # Read file-like object into a NumPy array
    file_bytes = np.asarray(bytearray(image_file.read()), dtype=np.uint8)
    
    # Decode the image
    image = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)
    
    if image is None:
        raise ValueError("Failed to decode the uploaded image.")

    # Resize and normalize
    image = cv2.resize(image, target_size)
    image = image / 255.0  # Normalize pixel values (0-1 range)

    return image
