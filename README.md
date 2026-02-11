# 🌐 Google Cloud Vision Multi-Language OCR Tool

> A robust, modular Python wrapper for the **Google Cloud Vision API** designed for high-accuracy **Document Text Detection (OCR)**.  
> Optimized for multilingual environments including **Vietnamese, Thai, Chinese, and Japanese**.  
> Supports both **local image files** and **remote image URLs**.

---

## ✨ Features

- 🔍 **Auto-Detection**  
  Seamlessly handles both local file paths and remote image URLs.

- 🌏 **Multi-Language Support**  
  Optimized for complex scripts (Thai, Vietnamese, etc.) using `language_hints`.

- 🧩 **Modular Design**  
  Clean, class-based implementation (`VisionAPIWrapper`) for easy integration.

- 🌐 **Localization (I18n)**  
  UI messages managed via external JSON files in the `lang/` directory.

- 🛡 **Future-Proof**  
  Suppresses version-related `FutureWarning` messages common in older Python environments (e.g., macOS system Python 3.9).

---

## 📋 Prerequisites

### 🖥 macOS Users
Install **Xcode Command Line Tools**:

```bash
xcode-select --install
```

### 🐍 Python
- Python **3.10 ~ 3.14+** (latest recommended)

### ☁ Google Cloud
- A Google Cloud project with **Cloud Vision API enabled**

---

## 🔑 How to Get Google Cloud API Credentials

1. **Create a Google Cloud Project**  
   Go to the Google Cloud Console and create a new project.

2. **Enable Cloud Vision API**  
   Navigate to:  
   `APIs & Services > Library`  
   Search for **Cloud Vision API** → Click **Enable**

3. **Create a Service Account**  
   Go to:  
   `IAM & Admin > Service Accounts`  
   Click **+ CREATE SERVICE ACCOUNT**

4. **Assign Roles**  
   Assign the role:  
   `Cloud Vision API User`

5. **Generate JSON Key**
   - Go to **Keys**
   - Click **ADD KEY > Create new key (JSON)**

6. **Setup**
   - Rename the downloaded file to:

```
service-account-key.json
```

   - Place it in your project root directory.

⚠ **Important:** Never share this file.

---

## 🚀 Installation & Setup (macOS Best Practice)

> ⚠ Do NOT modify macOS system Python (`/usr/bin/python3`).  
> This project uses a sandboxed approach via **Homebrew + venv**.

---

### 1️⃣ Install Homebrew & Latest Python

Install Homebrew (if not already installed):

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

*It is better not to incorporate the path settings required by homebrew. It is just meant to be used as a sub.

Install Python 3.14:

```bash
brew install python@3.14
```

---

### 2️⃣ Create an Isolated Virtual Environment

Navigate to the project folder:

```bash
cd path/to/vision-ocr-tool
```

Create the environment using the specific Homebrew Python path:

```bash
/opt/homebrew/bin/python3.14 -m venv .venv
```

---

### 3️⃣ Activate and Install Dependencies

Activate virtual environment:

```bash
source .venv/bin/activate
```

Install required library:

```bash
pip install google-cloud-vision
```

or

```bash
/opt/homebrew/bin/python3.14 -m pip install google-cloud-vision
```

---

## 📁 Project Structure

```text
get_ocr_googlevision/
├── lang/
│   ├── en.json                 # English UI messages
│   └── ja.json                 # Japanese UI messages
├── ocr_vision.py               # Core logic module
├── get_ocr_vision.py           # CLI execution script
└── LICENSE                     # MIT License file

```

---

## ⚙ Configuration

### 🔧 Global Variables

All global variables in `ocr_vision.py`  
(e.g., `DEFAULT_LANGUAGE_HINTS`)  
are documented with English comments for easy customization.

---

### 🔐 Credentials Environment Variable

Set before running the script:

```bash
export GOOGLE_APPLICATION_CREDENTIALS="service-account-key.json"
```

---

## ▶ Usage

Make sure your virtual environment is activated:

```bash
source .venv/bin/activate
```

### 📂 Process a Local Image

```bash
python get_ocr_vision.py ./samples/image.jpg
```

### 🌐 Process an Image from URL

```bash
python get_ocr_vision.py https://example.com/image.png
```

---

## 📚 Appendix: Why This Method?

### ❗ The “PATH” Pitfall

Many tutorials suggest:

- Adding `/opt/homebrew/bin` to your global `PATH`
- Aliasing `python` to the Homebrew version

⚠ This is risky.

macOS system tasks rely on the default Python.  
Changing it globally can break OS-level functionality.

---

### ✅ The Solution: Full-Path venv

By using the **Full-Path venv creation method**, we ensure:

- ✔ The project runs on **Python 3.14**
- ✔ macOS system Python remains untouched
- ✔ Dependencies are isolated in `.venv`
- ✔ No library version conflicts

---

## 👤 Author

**Kimiya Kitani**

---

## 📜 License

This project is licensed under the **MIT License**.  
See the `LICENSE` file for details.

---

