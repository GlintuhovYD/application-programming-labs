import cv2
import matplotlib.pyplot as plt
from typing import Union
import numpy as np

def calculate_histogram(img: cv2.Mat) -> np.ndarray:
    """Calculates the grayscale histogram of an image.

    Args:
        img: The input image (grayscale or color).  Color images will be converted to grayscale.

    Returns:
        A NumPy array representing the histogram.  The array will have a length of 256,
        representing the frequency of each grayscale intensity value (0-255).
        Returns None if the input is invalid.
    """
    try:
      if img is None:
        return None
      gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) if len(img.shape) == 3 else img
      hist = cv2.calcHist([gray], [0], None, [256], [0, 256])
      return hist.flatten() #convert to 1D array
    except Exception as e:
        raise Exception(f"An error occurred during histogram calculation: {e}") from e

def plot_histogram(hist: np.ndarray, output_path: str) -> None:
    """Plots and saves the given histogram to a PNG file.

    Args:
        hist: The histogram data as a 1D NumPy array.
        output_path: The path to save the histogram plot (PNG format).

    Raises:
        Exception: If an error occurs during plotting or saving the histogram.
    """
    try:
        plt.figure()
        plt.plot(hist)
        plt.xlabel("Intensity")
        plt.ylabel("Frequency")
        plt.title("Image Histogram")
        plt.savefig(output_path)
        plt.close()
    except Exception as e:
        raise Exception(f"An error occurred while plotting the histogram: {e}") from e
