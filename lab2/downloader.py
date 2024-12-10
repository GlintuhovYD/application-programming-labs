import os
from icrawler.builtin import GoogleImageCrawler

def download_images(keyword: str, image_dir: str, num_images: int = 10) -> None:
    """Downloads images using Google Image Crawler.

    Creates a directory if it doesn't exist, then uses GoogleImageCrawler
    to download images based on the provided keyword.  Handles exceptions
    during the download process.

    Args:
        keyword: The keyword to search for images.
        image_dir: The directory to save the downloaded images.
        num_images: The maximum number of images to download (default is 10).

    Returns:
        None. Prints an error message if an exception occurs during download.
    """
    try:
        os.makedirs(image_dir, exist_ok=True)
        google_crawler = GoogleImageCrawler(storage={'root_dir': image_dir})
        google_crawler.crawl(keyword=keyword, max_num=num_images)
    except Exception as e:
        raise Exception(f"Error downloading images: {e}") from e
