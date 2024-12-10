import argparse
import os

import cv2
import histogram
import image_processing

def process_image(input_image, output_dir, show_images=False):
    """Processes an image, calculates its histogram, and saves the results.

    Args:
        input_image: Path to the input image file.
        output_dir: Directory to save the processed images and histogram.
        show_images: Boolean flag to display the original and binary images using cv2.imshow (optional). Defaults to False.

    Raises:
        FileNotFoundError: If the input image file is not found.
        Exception: If any other error occurs during image processing.
    """
    try:
        img = image_processing.load_image(input_image)
        size = image_processing.get_image_size(img)
        print(f"Image size: {size}")

        hist = histogram.calculate_histogram(img)
        os.makedirs(output_dir, exist_ok=True)
        histogram.plot_histogram(hist, os.path.join(output_dir, "histogram.png"))
        cv2.imwrite(os.path.join(output_dir, "original.png"), img)
        cv2.imwrite(os.path.join(output_dir, "binary.png"), image_processing.binarize_image(img))

        if show_images:
            cv2.imshow("Original Image", img)
            cv2.imshow("Binary Image", image_processing.binarize_image(img))
            cv2.waitKey(0)
            cv2.destroyAllWindows()

        print(f"Results saved to: {output_dir}")

    except FileNotFoundError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


def main():
    """Main function to parse command-line arguments and process the image."""
    parser = argparse.ArgumentParser(description='Image processing script.')
    parser.add_argument('input_image', type=str, help='Path to input image')
    parser.add_argument('output_dir', type=str, help='Directory to save results')
    parser.add_argument('--show_images', action='store_true', help='Display images using cv2.imshow (optional)')
    args = parser.parse_args()
    process_image(args.input_image, args.output_dir, args.show_images)

if __name__ == "__main__":
    main()
