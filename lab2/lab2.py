import argparse
import os
from icrawler.builtin import GoogleImageCrawler
import csv

def create_annotation_file(image_dir, annotation_file, keyword):
    with open(annotation_file, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['absolute_path', 'relative_path'])
        for filename in os.listdir(image_dir):
            if filename.endswith(('.jpg', '.jpeg', '.png')):
                abs_path = os.path.abspath(os.path.join(image_dir, filename))
                rel_path = os.path.join(os.path.relpath(image_dir), filename)
                writer.writerow([abs_path, rel_path])


def download_images(keyword, image_dir, num_images=10):
    google_crawler = GoogleImageCrawler(storage={'root_dir': image_dir})
    google_crawler.crawl(keyword=keyword, max_num=num_images)


def image_iterator(annotation_file):
    with open(annotation_file, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            yield row['absolute_path']


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Download and annotate images.')
    parser.add_argument('keyword', type=str, help='Keyword for image search')
    parser.add_argument('image_dir', type=str, help='Directory to save images')
    parser.add_argument('annotation_file', type=str, help='Path to annotation CSV file')
    args = parser.parse_args()

    os.makedirs(args.image_dir, exist_ok=True)
    download_images(args.keyword, args.image_dir)
    create_annotation_file(args.image_dir, args.annotation_file, args.keyword)
    print(f"Images downloaded and annotated to {args.annotation_file}")

    for image_path in image_iterator(args.annotation_file):
        print(f"Processing image: {image_path}")
