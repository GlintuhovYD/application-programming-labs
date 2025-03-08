import cv2
import matplotlib.pyplot as plt
import numpy as np


def calculate_histogram(img: np.ndarray) -> tuple:
    """Calculates the histogram for three color channels (BGR).

    Args:
        img: The input image (must be a color image in BGR format).

    Returns:
        A tuple containing three NumPy arrays, one for each color channel (B, G, R).
        Raises exceptions for invalid input.
    """
    if not isinstance(img, np.ndarray):
        raise TypeError("Input image is not a NumPy array.")
    if len(img.shape) != 3:
        raise ValueError("Input image is not a color image (must have 3 channels).")

    try:
        b, g, r = cv2.split(img)
        hist_b = cv2.calcHist([b], [0], None, [256], [0, 256]).flatten()
        hist_g = cv2.calcHist([g], [0], None, [256], [0, 256]).flatten()
        hist_r = cv2.calcHist([r], [0], None, [256], [0, 256]).flatten()
        return hist_b, hist_g, hist_r
    except cv2.error as e:
        raise RuntimeError(f"OpenCV error during histogram calculation: {e}") from e
    except Exception as e:
        raise RuntimeError(f"An unexpected error occurred during histogram calculation: {e}") from e


def plot_histogram(hist_b: np.ndarray, hist_g: np.ndarray, hist_r: np.ndarray, output_path: str) -> bool:
    """Plots and saves the three-channel histogram to a PNG file.

    Args:
        hist_b (np.ndarray): The histogram data as a NumPy array for the Blue channel.
        hist_g (np.ndarray): The histogram data as a NumPy array for the Green channel.
        hist_r (np.ndarray): The histogram data as a NumPy array for the Red channel.
        output_path (str): The path to save the histogram plot (PNG format).

    Returns:
        bool: True if the histogram was plotted and saved successfully, False otherwise.

    Raises:
        ValueError: If the input histogram data is invalid.
        Exception: If any other error occurs during plotting.
    """
    if not all(
            isinstance(hist, np.ndarray) and hist.ndim == 1 and len(hist) == 256 for hist in [hist_b, hist_g, hist_r]):
        raise ValueError("Invalid histogram data. Must be three 1D NumPy arrays of length 256.")

    try:
        bins = np.arange(256)
        plt.figure(figsize=(12, 6))
        plt.plot(bins, hist_b, color='blue', linewidth=2, label='Blue')
        plt.plot(bins, hist_g, color='green', linewidth=2, label='Green')
        plt.plot(bins, hist_r, color='red', linewidth=2, label='Red')
        plt.xlabel("Intensity (0-255)", fontsize=12)
        plt.ylabel("Frequency", fontsize=12)
        plt.title("Three-Channel Image Histogram (BGR)", fontsize=14)
        plt.legend()
        plt.grid(linestyle='--', alpha=0.7)
        plt.savefig(output_path)
        plt.close()
        return True
    except FileNotFoundError as e:
        raise FileNotFoundError(f"Could not save histogram to {output_path}. Check the path.") from e
    except Exception as e:
        raise Exception(f"An unexpected error occurred while plotting the histogram: {e}") from e
