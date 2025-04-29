# app.py

import streamlit as st
import cv2
import numpy as np
from src.preprocessing import load_and_preprocess
from src.segmentation import detect_green_areas
from src.analysis import calculate_green_percentage, detect_deforestation
from src.virtualization import plot_images

def main():
    # Title of the web app
    st.title("AI-based Deforestation Detection")

    # File uploader for past and current year images
    st.header("Upload Satellite Images (Past and Current Year)")
    past_image_file = st.file_uploader("Upload Past Year Image", type=["jpg", "png"])
    current_image_file = st.file_uploader("Upload Current Year Image", type=["jpg", "png"])

    if past_image_file and current_image_file:
        # Load and preprocess images
        past_image = load_and_preprocess(past_image_file)
        current_image = load_and_preprocess(current_image_file)

        # Detect green areas
        past_mask = detect_green_areas(past_image)
        current_mask = detect_green_areas(current_image)

        # Calculate green percentages
        past_green_percentage = calculate_green_percentage(past_mask)
        current_green_percentage = calculate_green_percentage(current_mask)

        # Detect deforestation
        deforestation_detected = detect_deforestation(past_green_percentage, current_green_percentage)

        # Show the results
        st.subheader(f"Past Year Green Cover: {past_green_percentage:.2f}%")
        st.subheader(f"Current Year Green Cover: {current_green_percentage:.2f}%")
        if deforestation_detected:
            st.error("Deforestation Detected!")
        else:
            st.success("No Deforestation Detected.")

        # Visualize images and green areas
        st.subheader("Visual Comparison:")
        plot_images(past_image, past_mask, current_image, current_mask)

if __name__ == "__main__":
    main()
