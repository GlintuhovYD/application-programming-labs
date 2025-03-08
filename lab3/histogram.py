import cv2
import matplotlib.pyplot as plt
import numpy as np

def calculate_histogram(img: cv2.Mat) -> tuple:
    """Calculates the histogram for three color channels (BGR).

    Args:
        img: The input image (must be a color image in BGR format).

    Returns:
        A tuple containing three NumPy arrays, one for each color channel (B, G, R).
        Returns (None, None, None) if the input is invalid or not a color image.
    """
    if not isinstance(img, np.ndarray):
        print("Error: Input image is not a NumPy array.")
        return None, None, None
    if len(img.shape) != 3:
        print("Error: Input image is not a color image (must have 3 channels).")
        return None, None, None

    try:
        b, g, r = cv2.split(img)

        hist_b = cv2.calcHist([b], [0], None, [256], [0, 256]).flatten()
        hist_g = cv2.calcHist([g], [0], None, [256], [0, 256]).flatten()
        hist_r = cv2.calcHist([r], [0], None, [256], [0, 256]).flatten()

        return hist_b, hist_g, hist_r
    except cv2.error as e:
        print(f"OpenCV error during histogram calculation: {e}")
        return None, None, None
    except Exception as e:
        print(f"An unexpected error occurred during histogram calculation: {e}")
        return None, None, None


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
    """
    if not (isinstance(hist_b, np.ndarray) and hist_b.ndim == 1 and len(hist_b) == 256 and
            isinstance(hist_g, np.ndarray) and hist_g.ndim == 1 and len(hist_g) == 256 and
            isinstance(hist_r, np.ndarray) and hist_r.ndim == 1 and len(hist_r) == 256):
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
    except FileNotFoundError:
        print(f"Could not save histogram to {output_path}. Check the path.")
        return False
    except Exception as e:
        print(f"An unexpected error occurred while plotting the histogram: {e}")
        return False

