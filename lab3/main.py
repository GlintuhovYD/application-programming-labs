import argparse
import os

import cv2
import histogram
import image_processing

def process_image(input_image: str, output_dir: str, show_images: bool = False) -> None:
    """Processes an image, calculates its histogram, and saves the results.

    Args:
        input_image (str): Path to the input image file.
        output_dir (str): Directory to save the processed images (original, binary, and histogram).
        show_images (bool, optional): Boolean flag to display the original and binary images using cv2.imshow. Defaults to False.

    Raises:
        FileNotFoundError: If the input image file is not found or the output directory is invalid.
        Exception: If any other error occurs during image processing.  Provides detailed error message.
    """
    try:
        img = image_processing.load_image(input_image)
        if img is None:
            raise FileNotFoundError(f"Could not load image from {input_image}")

        size = image_processing.get_image_size(img)
        print(f"Image size: {size}")

        hist_b, hist_g, hist_r = histogram.calculate_histogram(img)
        if hist_b is None:
            raise Exception("Histogram calculation failed.")

        os.makedirs(output_dir, exist_ok=True)
        if not os.path.isdir(output_dir):
            raise FileNotFoundError(f"Could not create output directory: {output_dir}")

        histogram_filepath = os.path.join(output_dir, "histogram.png")
        histogram.plot_histogram(hist_b, hist_g, hist_r, histogram_filepath)

        cv2.imwrite(os.path.join(output_dir, "original.png"), img)
        binary_img = image_processing.binarize_image(img)
        cv2.imwrite(os.path.join(output_dir, "binary.png"), binary_img)

        if show_images:
            cv2.imshow("Original Image", img)
            cv2.imshow("Binary Image", binary_img)
            cv2.waitKey(0)
            cv2.destroyAllWindows()

        print(f"Results saved to: {output_dir}")

    except FileNotFoundError as e:
        print(f"Error: File not found - {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


def main():
    parser = argparse.ArgumentParser(description='Image processing script.')
    parser.add_argument('input_image', type=str, help='Path to input image')
    parser.add_argument('output_dir', type=str, help='Directory to save processed images and histogram')
    parser.add_argument('--show_images', action='store_true', help='Display images using cv2.imshow (optional)')
    args = parser.parse_args()
    process_image(args.input_image, args.output_dir, args.show_images)


if __name__ == "__main__":
    main()
