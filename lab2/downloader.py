from icrawler.builtin import GoogleImageCrawler
import os

def download_images(keyword, image_dir, num_images=10):
    os.makedirs(image_dir, exist_ok=True)
    google_crawler = GoogleImageCrawler(storage={'root_dir': image_dir})
    google_crawler.crawl(keyword=keyword, max_num=num_images)