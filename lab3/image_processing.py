import cv2

def load_image(image_path: str) -> cv2.Mat:
    """Loads an image from the specified path using OpenCV.

    Args:
        image_path (str): The path to the image file.

    Returns:
        cv2.Mat: The loaded image as a NumPy array.

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

def get_image_size(img: cv2.Mat) -> tuple:
    """Returns the dimensions (height, width) of an image.

    Args:
        img (cv2.Mat): The input image (OpenCV Mat object).

    Returns:
        tuple: A tuple containing the height and width of the image. Returns (0,0) if input is invalid
    """
    try:
        return img.shape[:2]
    except Exception as e:
        print(f"Error getting image size: {e}")
        return 0, 0


def binarize_image(img: cv2.Mat) -> cv2.Mat:
    """Converts a color image to grayscale and then to a binary image using thresholding.

    Args:
        img (cv2.Mat): The input color image (OpenCV Mat object).

    Returns:
        cv2.Mat: The binarized image as a NumPy array.
    """
    try:
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        _, binary_img = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
        return binary_img
    except Exception as e:
        print(f"Error during binarization: {e}")
        return None

