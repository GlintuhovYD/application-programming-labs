from icrawler.builtin import GoogleImageCrawler
import os

def download_images(keyword: str, image_dir: str, num_images: int = 10) -> None:
    try:
        os.makedirs(image_dir, exist_ok=True)
        google_crawler = GoogleImageCrawler(storage={'root_dir': image_dir})
        google_crawler.crawl(keyword=keyword, max_num=num_images)
    except Exception as e:
        print(f"Ошибка при загрузке изображений: {e}")

