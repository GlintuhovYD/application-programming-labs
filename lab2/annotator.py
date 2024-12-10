import csv
import os
from typing import Iterator

class ImageIterator:
    def __init__(self, annotation_file: str):
        self.annotation_file = annotation_file

    def __iter__(self) -> Iterator[str]:
        try:
            with open(self.annotation_file, 'r', encoding='utf-8') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    yield row['absolute_path']
        except FileNotFoundError:
            print(f"Ошибка: Файл аннотаций {self.annotation_file} не найден.")
        except Exception as e:
            print(f"Произошла непредвиденная ошибка: {e}")


def create_annotation_file(image_dir: str, annotation_file: str) -> None:
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
        print(f"Ошибка при создании файла аннотаций: {e}")
