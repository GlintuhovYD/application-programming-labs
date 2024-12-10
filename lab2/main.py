import argparse

import annotator
import downloader

if __name__ == "__main__":
    """Downloads images based on a keyword and creates an annotation file.

    Parses command-line arguments to specify the keyword for image search,
    the directory to save images, and the path for the annotation CSV file.
    Calls downloader.download_images and annotator.create_annotation_file
    to perform the download and annotation tasks.

    Args:
        None (Parses arguments from command line)

    Returns:
        None
    """
    try:
        parser = argparse.ArgumentParser(description='Download and annotate images.')
        parser.add_argument('keyword', type=str, help='Keyword for image search')
        parser.add_argument('image_dir', type=str, help='Directory to save images')
        parser.add_argument('annotation_file', type=str, help='Path to annotation CSV file')
        args = parser.parse_args()

        downloader.download_images(args.keyword, args.image_dir)
        annotator.create_annotation_file(args.image_dir, args.annotation_file)
        print(f"Изображения скачаны и аннотированы в {args.annotation_file}")
    except Exception as e:
        print(f"An error occurred: {e}")
