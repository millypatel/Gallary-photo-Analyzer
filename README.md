# 📸 Gallery Photo Analyzer

**Gallery Photo Analyzer** is a powerful Python application that scans image galleries and provides detailed insights, including:
- 🔁 Duplicate detection
- 🔍 Blurry image detection
- 🧠 OCR (text extraction)
- 🙂 Face detection and clustering


---

## 🚀 Features

| Feature                   | Description                                                                 |
|---------------------------|-----------------------------------------------------------------------------|
| 🔁 Duplicate Detection     | Detects exact or nearly identical images using perceptual hashing           |
| 🔍 Blur Detection          | Flags blurry images using the Laplacian variance method                     |
| 🧠 OCR                    | Extracts text from images using `pytesseract`                                |
| 🙂 Face Clustering         | Groups images with similar faces using `face_recognition` and DBSCAN        |

---

## 🧰 Requirements

- Python 3.7+
- [Tesseract OCR](https://github.com/tesseract-ocr/tesseract) (must be installed separately)

Install Python dependencies:

```bash
pip install -r requirements.txt
