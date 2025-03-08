import cv2
import numpy as np


def load_image(image_path: str) -> np.ndarray:
    """Loads an image from the specified path using OpenCV.

    Args:
        image_path (str): The path to the image file.

    Returns:
        np.ndarray: The loaded image as a NumPy array.

    Raises:
        FileNotFoundError: If the image file is not found.
        Exception: If any other error occurs during image loading. Includes detailed error message.
    """
    try:
        img = cv2.imread(image_path)
        if img is None:
            raise FileNotFoundError(f"Image file not found: {image_path}")
        return img
    except FileNotFoundError as e:
        raise FileNotFoundError(f"Image file not found: {image_path}, Original error: {e}") from e
    except Exception as e:
        raise Exception(f"An unexpected error occurred while loading the image '{image_path}': {e}") from e


def get_image_size(img: np.ndarray) -> tuple[int, int]:
    """Returns the dimensions (height, width) of an image.

    Args:
        img (np.ndarray): The input image (OpenCV Mat object).

    Returns:
        tuple: A tuple containing the height and width of the image.

    Raises:
        TypeError: if input is not a NumPy array.
        Exception: If any other error occurs.
    """
    if not isinstance(img, np.ndarray):
        raise TypeError("Input image is not a NumPy array.")
    try:
        return img.shape[:2]
    except Exception as e:
        raise Exception(f"Error getting image size: {e}") from e


def binarize_image(img: np.ndarray) -> np.ndarray:
    """Converts a color image to grayscale and then to a binary image using thresholding.

    Args:
        img (np.ndarray): The input color image (OpenCV Mat object).

    Returns:
        np.ndarray: The binarized image as a NumPy array.

    Raises:
        TypeError: if input is not a NumPy array.
        Exception: If any other error occurs during binarization.
    """
    if not isinstance(img, np.ndarray):
        raise TypeError("Input image is not a NumPy array.")
    try:
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        _, binary_img = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
        return binary_img
    except Exception as e:
        raise Exception(f"Error during binarization: {e}") from e
