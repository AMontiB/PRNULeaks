import subprocess
import csv
import os

def check_metadata(image_path, metadata_keywords):
    try:
        result = subprocess.run(['exiftool', '-s', image_path], capture_output=True, text=True, check=True)
        metadata = result.stdout.strip().split('\n')
        matching_keywords = [keyword for keyword in metadata_keywords if any(keyword.lower() in field.lower() for field in metadata)]
        return matching_keywords
    except subprocess.CalledProcessError:
        return []

def find_images_with_metadata(root_path, metadata_keywords):
    image_data = []
    for foldername, subfolders, filenames in os.walk(root_path):
        for filename in filenames:
            if filename.lower().endswith(('.jpg', '.jpeg', '.png', '.gif', '.bmp')):
                try:
                    image_path = os.path.join(foldername, filename)
                    matching_keywords = check_metadata(image_path, metadata_keywords)
                    if matching_keywords:
                        image_data.append((image_path, matching_keywords))
                except:
                    print('skip')
    return image_data

def save_to_csv(csv_filename, image_paths):
    with open(csv_filename, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(['Image Path'])
        csv_writer.writerows([[path] for path in image_paths])

if __name__ == "__main__":
    root_path = #PATH2Dataset like "/media/mmlab/Datasets_4TB/FORLAB"
    software_tags = ['Photos', 'VSCO', 'Picasa', 'picasa', 'Lightroom', 'Photoshop', 'photoshop',
                    'photoscape', 'PhotoScape', 'lightroom', 'Darktable', 'darktable', 'GIMP', 'Shotwell']
    csv_filename = "list_outcamera_images.csv"

    image_paths = find_images_with_metadata(root_path, software_tags)

    if image_paths:
        save_to_csv(csv_filename, image_paths)
        print(f"CSV file '{csv_filename}' created with paths of images containing specified software tags.")
    else:
        print("No images found with specified software tags.")

