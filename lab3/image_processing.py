import cv2

def load_image(image_path):
    """Loads an image using OpenCV."""
    try:
        img = cv2.imread(image_path)
        if img is None:
            raise FileNotFoundError(f"Image not found: {image_path}")
        return img
    except FileNotFoundError as e:
        raise FileNotFoundError(f"Error loading image: {e}") from e
    except Exception as e:
        raise Exception(f"An unexpected error occurred while loading the image: {e}") from e

def get_image_size(img):
    """Gets the dimensions of an image."""
    return img.shape[:2]

def binarize_image(img):
    """Binarizes an image."""
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    _, binary_img = cv2.threshold(gray, 127, 256, cv2.THRESH_BINARY)
    return binary_img
