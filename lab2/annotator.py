import csv
import os

def create_annotation_file(image_dir, annotation_file):
    with open(annotation_file, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['absolute_path', 'relative_path'])
        for filename in os.listdir(image_dir):
            if filename.endswith(('.jpg', '.jpeg', '.png')):
                abs_path = os.path.abspath(os.path.join(image_dir, filename))
                rel_path = os.path.relpath(os.path.join(image_dir, filename)) #Исправлено
                writer.writerow([abs_path, rel_path])

def image_iterator(annotation_file):
    with open(annotation_file, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            yield row['absolute_path']