import face_recognition
import os
import shutil
from multiprocessing import Pool
from PIL import Image

# Paths
reference_image_path = "REF_IMAGE_PATH"
input_folder = "PHOTOS_INPUT_FOLDER_PATH"
output_folder = "PHOTOS_OUTPUT_FOLDER_PATH"

# Function to initialize pool workers


def initialize_worker(reference_encoding_param):
    global reference_encoding
    reference_encoding = reference_encoding_param

# Function to process each file


def process_file(file_name):
    file_path = os.path.join(input_folder, file_name)

    # Check if the file is an image
    if not file_name.lower().endswith((".jpg", ".jpeg", ".png")):
        return None  # Skip non-image files

    try:
        # Load the current image
        current_image = face_recognition.load_image_file(file_path)

        # Find face encodings in the current image
        current_encodings = face_recognition.face_encodings(current_image)

        # Compare faces
        match = any(face_recognition.compare_faces(
            current_encodings, reference_encoding))

        # If a match is found, return the file name
        if match:
            return file_name

    except Exception as e:
        print(f"Error processing {file_name}: {e}")
    return None


if __name__ == '__main__':
    # Ensure the output folder exists
    os.makedirs(output_folder, exist_ok=True)

    # Load the reference image and encode the face
    print("Loading reference image...")
    reference_image = face_recognition.load_image_file(reference_image_path)
    reference_encoding = face_recognition.face_encodings(reference_image)[0]

    # Process files in parallel
    print("Scanning images in the input folder...")
    with Pool(initializer=initialize_worker, initargs=(reference_encoding,)) as pool:
        matches = pool.map(process_file, os.listdir(input_folder))

    # Move matched files to the output folder
    # Remove None values
    matches = [file_name for file_name in matches if file_name]
    for match in matches:
        shutil.move(os.path.join(input_folder, match),
                    os.path.join(output_folder, match))

    print("Organizing complete. Check the output folder for results.")
