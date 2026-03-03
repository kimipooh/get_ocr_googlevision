# 🌐 Google Cloud Vision Multi-Language OCR Tool

> A robust, modular Python wrapper for the **Google Cloud Vision API** designed for high-accuracy **Document Text Detection (OCR)**.  
> Optimized for multilingual environments including **Vietnamese, Thai, Chinese, and Japanese**.  
> Supports both **local image files** and **remote image URLs**.

---

## ✨ Features

- 🔍 **Auto-Detection & Manual Hints** Switch between "auto" mode for automatic language detection and "hint" mode to improve accuracy for specific languages.

- 🌏 **Multi-Language Support** Optimized for complex scripts (Thai, Vietnamese, etc.) using `language_hints`.

- 🌐 **Localization (I18n)** UI messages managed via external JSON files in the `lang/` directory, supporting English and Japanese.

- 🧩 **Modular Design** Clean, class-based implementation (`VisionAPIWrapper`) for easy integration into other projects.

- 🛡 **Future-Proof** Suppresses version-related `FutureWarning` messages common in various Python environments.

---

## 📋 Prerequisites

### 🐍 Python
- Python **3.10 ~ 3.14+** (latest recommended)

### ☁ Google Cloud Setup
1. Enable **Cloud Vision API** in your Google Cloud Console.
2. Create a **Service Account** with the `Cloud Vision API User` role.
3. Generate a **JSON Key** and save it as `service-account-key.json` in your project root.

> [!CAUTION]
> **Important:** Never share your JSON key. The Google Cloud Vision API offers a free quota of 1,000 units per month as of February 2026.

---

## 🚀 Installation & Setup

### 1. Create a Virtual Environment
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows use: .venv\Scripts\activate
```

### 2. Install Dependencies
```bash
pip install google-cloud-vision
```

---

## ⚙ Configuration

### 🔐 Credentials
Set the environment variable before running the script:
```bash
export GOOGLE_APPLICATION_CREDENTIALS="service-account-key.json"
```

### 🔧 Global Variables
Customize behavior in `ocr_vision.py`:
- `DEFAULT_LANGUAGE_HINTS`: Default hints (e.g., `["vi", "th", "zh", "ja"]`).
- `HIDE_PYTHON_WARNINGS`: Toggle suppression of API-related warnings.

---

## ▶ Usage

### 📂 Basic Execution (Auto-Detection)
```bash
python get_ocr_vision.py ./samples/image.jpg
```

### 🌐 Specify UI Language
Use the `--lang` option to use specific messages from the `lang/` directory.
```bash
python get_ocr_vision.py ./samples/photo.png --lang en
```

### 🌏 Provide OCR Language Hints
Provide comma-separated language codes to improve accuracy for specific scripts.
```bash
python get_ocr_vision.py https://example.com/image.jpg --ocr-hint "vi,lo"
```

---

## 📁 Project Structure

```text
get_ocr_googlevision/
├── lang/
│   ├── en.json                 # English UI messages
│   └── ja.json                 # Japanese UI
├── modules/
│   └── ocr_vision.py           # Core logic (API messages Wrapper)
├── get_ocr_vision.py           # CLI execution script
└── LICENSE                     # MIT License file
```

---

## 👤 Author
**Kimiya Kitani**

## 📜 License
This project is licensed under the **MIT License**.

Copyright (c) 2026 Kimiya Kitani
