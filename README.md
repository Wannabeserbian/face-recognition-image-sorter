# Face Recognition Image Sorter

This Python script scans a folder of images and moves images containing a recognized face to a designated output folder. It uses the `face_recognition` library for facial comparison and multiprocessing for parallel processing.

## ✅ Features

- Loads a reference image and detects the face encoding.
- Scans an input folder for images containing the same face.
- Moves matching images to an output folder.
- Uses multiprocessing for efficient processing.

## 🛠️ Prerequisites

- **Python 3**
- **Required Python libraries:** `pip install face_recognition pillow`
- **dlib** — (Automatically installed with `face_recognition`, but may require additional system dependencies)

## ⚡ Usage

### 1️⃣ Update Paths

Modify the script to specify the correct paths:

```bash
reference_image_path = "REF_IMAGE_PATH"  # Path to the reference image
input_folder = "PHOTOS_INPUT_FOLDER_PATH"  # Folder containing images to scan
output_folder = "PHOTOS_OUTPUT_FOLDER_PATH"  # Folder where matching images will be moved
```

### 2️⃣ Run the Script

Execute the script with:

```bash
python main.py
```

### 3️⃣ Output

- Images containing a face matching the reference image will be moved to the output folder.
- Non-matching images remain in the input folder.
- Errors during processing will be logged to the console.

### How It Works

1. The script loads the reference image and encodes the face.
2. It scans all images in the input folder and extracts face encodings.
3. Each image is compared to the reference encoding using `face_recognition.compare_faces()`.
4. If a match is found, the image is moved to the output folder.

### Troubleshooting

- No face detected in the reference image: Ensure the image clearly shows a single face.
- Low matching accuracy: Adjust `face_recognition.compare_faces()` parameters to fine-tune sensitivity.
- Script is slow: Performance improves with a higher CPU core count, as the script uses multiprocessing.
