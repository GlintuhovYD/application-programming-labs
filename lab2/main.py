import argparse
import annotator
import downloader

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Download and annotate images.')
    parser.add_argument('keyword', type=str, help='Keyword for image search')
    parser.add_argument('image_dir', type=str, help='Directory to save images')
    parser.add_argument('annotation_file', type=str, help='Path to annotation CSV file')
    args = parser.parse_args()

    downloader.download_images(args.keyword, args.image_dir)
    annotator.create_annotation_file(args.image_dir, args.annotation_file)
    print(f"Изображения скачаны и аннотированы в {args.annotation_file}")
