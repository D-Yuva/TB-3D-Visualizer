import cv2
import numpy as np
import os

def load_images(image_path: str, mask_path: str):
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    mask = cv2.imread(mask_path, cv2.IMREAD_GRAYSCALE)
    if image is None or mask is None:
        raise FileNotFoundError("Image or mask file not found.")
    return image, mask

def apply_mask(image, mask):
    masked_image = cv2.bitwise_and(image, image, mask=mask) # Keeps only the parts of the image where the mask is white, rest all are set to black
    return masked_image

def save_masked_image(image_path: str, mask_path: str, output_path: str = "data/masked_result.png"):

    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    mask = cv2.imread(mask_path, cv2.IMREAD_GRAYSCALE)

    masked_image = cv2.bitwise_and(image, image, mask=mask)
    cv2.imwrite(output_path, masked_image)

def generate_mask_from_image(image_path, mask_path):

    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    _, mask = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY) 
    """
    (BINARY MASK) Applies binary thresholding: Pixels above 127 → set to 255 (white), Pixels below or equal to 127 → set to 0 (black)
    Highlight TB infected areas
    Mask out irrelevant background
    """
    cv2.imwrite(mask_path, mask)