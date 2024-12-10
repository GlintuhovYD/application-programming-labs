import csv
import os
from typing import Iterator

class ImageIterator:
    """Iterator for processing images from an annotation file."""

    def __init__(self, annotation_file: str):
        """Initializes the iterator.

        Args:
            annotation_file: Path to the annotation CSV file.
        """
        self.annotation_file = annotation_file

    def __iter__(self) -> Iterator[str]:
        """Returns an iterator over image paths.

        Yields:
            str: The absolute path to an image.

        Raises:
            FileNotFoundError: If the annotation file is not found.
            Exception: If any other error occurs during file processing.

        """
        try:
            with open(self.annotation_file, 'r', encoding='utf-8') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    yield row['absolute_path']
        except FileNotFoundError as e:
            raise FileNotFoundError(f"Annotation file not found: {e}") from e
        except Exception as e:
            raise Exception(f"An unexpected error occurred: {e}") from e


def create_annotation_file(image_dir: str, annotation_file: str) -> None:
    """Creates an annotation CSV file.

    Creates a CSV file containing absolute and relative paths to images
    within a specified directory. Handles exceptions during file creation.


    Args:
        image_dir: Directory containing the images.
        annotation_file: Path to save the annotation CSV file.

    Returns:
        None. Prints an error message if an exception occurs.
    """
    try:
        with open(annotation_file, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['absolute_path', 'relative_path'])
            for filename in os.listdir(image_dir):
                if filename.lower().endswith(('.jpg', '.jpeg', '.png')):
                    abs_path = os.path.abspath(os.path.join(image_dir, filename))
                    rel_path = os.path.relpath(os.path.join(image_dir, filename))
                    writer.writerow([abs_path, rel_path])
    except Exception as e:
        raise Exception(f"Error creating annotation file: {e}") from e
