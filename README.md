# get_ocr_googlevision

**English** | [Japanese](README_ja.md)

A lightweight research tool for extracting text from local image files or remote image URLs with the Google Cloud Vision API.
It is designed for practical OCR work in multilingual environments, especially when dealing with Vietnamese, Thai, Chinese, Japanese, Lao, and mixed-script materials.

## Overview

This repository provides a small command-line wrapper around Google Cloud Vision Document Text Detection.
It supports:

- OCR for local image files
- OCR for remote image URLs
- optional language hints for better recognition accuracy
- simple UI message localization via JSON files
- a modular structure that can be reused in other research workflows

This project is intended as a reusable research tool rather than a large framework.

## Features

- Simple CLI interface
- Google Cloud Vision API based OCR
- Automatic detection mode when no language hints are provided
- Manual language hint mode with comma-separated codes such as `vi,th,ja`
- English and Japanese UI message files in `lang/`
- Separated core logic in `modules/ocr_vision.py`

## Project structure

```text
get_ocr_googlevision/
├── CITATION.cff
├── CHANGELOG.md
├── LICENSE
├── README.md
├── README_ja.md
├── requirements.txt
├── get_ocr_vision.py
├── lang/
│   ├── en.json
│   └── ja.json
└── modules/
    └── ocr_vision.py
```

## Requirements

- Python 3.10 or later
- A Google Cloud project with Vision API enabled
- A service account key for authentication

Install dependencies:

```bash
pip install -r requirements.txt
```

## Setup

### 1. Create a virtual environment

```bash
python -m venv .venv
source .venv/bin/activate
```

On Windows:

```bat
.venv\Scripts\activate
```

### 2. Prepare credentials

Create a service account in Google Cloud, enable the Vision API, and download a JSON key.
Then set the environment variable:

```bash
export GOOGLE_APPLICATION_CREDENTIALS="/path/to/service-account-key.json"
```

On Windows PowerShell:

```powershell
$env:GOOGLE_APPLICATION_CREDENTIALS="C:\path\to\service-account-key.json"
```

## Usage

### Local image

```bash
python get_ocr_vision.py ./samples/image.jpg
```

### Remote image URL

```bash
python get_ocr_vision.py "https://example.org/image.jpg"
```

### Specify UI language

```bash
python get_ocr_vision.py ./samples/image.jpg --lang en
python get_ocr_vision.py ./samples/image.jpg --lang ja
```

### Specify OCR language hints

```bash
python get_ocr_vision.py ./samples/image.jpg --ocr-hint "vi,lo"
```

### Force automatic detection

```bash
python get_ocr_vision.py ./samples/image.jpg --ocr-hint auto
```

## Language hints

Language hints can improve OCR quality for difficult or mixed-script materials, but they do not guarantee perfect recognition.
For research use, OCR results should still be checked against the source image.

Examples:

- `vi` for Vietnamese
- `th` for Thai
- `zh` for Chinese
- `ja` for Japanese
- `lo` for Lao

## Typical use cases

- temple signboards and inscriptions
- funeral books and memorial materials
- multilingual archival images
- photographed documents in field research
- exploratory OCR before structured metadata extraction



## License

This project is released under the MIT License. See `LICENSE`.

Copyright (c) 2026 Kimiya Kitani

## Author

Kimiya Kitani
