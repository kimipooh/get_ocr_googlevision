# Google Cloud Vision Multi-Language OCR Tool

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.18910589.svg)](https://doi.org/10.5281/zenodo.18910589)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](#installation)
[![Japanese](https://img.shields.io/badge/README-日本語-green.svg)](README_ja.md)

Research software for OCR text extraction using Google Cloud Vision API.

This tool provides a practical command-line workflow for multilingual OCR on local image files and remote image URLs. It was developed for research use cases that involve Southeast Asian and East Asian materials, including Vietnamese, Thai, Chinese, and Japanese text.

## Features

- Google Cloud Vision API based OCR
- Supports local image files and remote image URLs
- Automatic OCR mode or manual language hints via `--ocr-hint`
- English and Japanese UI messages via JSON language files
- Modular core implementation in `modules/ocr_vision.py`
- Suitable for research-oriented OCR and text extraction workflows

## Installation

### Requirements

- Python 3.10 or later
- A Google Cloud project with the Vision API enabled
- A service account key for Google Cloud Vision API

### Setup

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
export GOOGLE_APPLICATION_CREDENTIALS="service-account-key.json"
```

On Windows, activate the virtual environment with:

```bash
.venv\Scripts\activate
```

## Usage

### Basic

```bash
python get_ocr_vision.py ./samples/image.jpg
```

### Specify UI language

```bash
python get_ocr_vision.py ./samples/image.jpg --lang en
```

### Provide OCR language hints

```bash
python get_ocr_vision.py ./samples/image.jpg --ocr-hint "vi,th,zh,ja"
```

### Automatic OCR detection

```bash
python get_ocr_vision.py ./samples/image.jpg --ocr-hint auto
```

### Remote image URL

```bash
python get_ocr_vision.py "https://example.org/sample.jpg" --ocr-hint "vi,lo"
```

## Directory Structure

```text
get_ocr_googlevision/
├── lang/
│   ├── en.json
│   └── ja.json
├── modules/
│   └── ocr_vision.py
├── .gitignore
├── CHANGELOG.md
├── CITATION.cff
├── CODE_OF_CONDUCT.md
├── CONTRIBUTING.md
├── LICENSE
├── README.md
├── README_ja.md
├── get_ocr_vision.py
└── requirements.txt
```

## Responsible and Ethical Use

This tool uses the Google Cloud Vision API to perform OCR processing on images.

Please use it responsibly:

- Ensure you have the right to process the images you submit
- Respect copyright, privacy, and data ownership
- Avoid sending sensitive or confidential material to external APIs unless you have confirmed it is appropriate to do so
- Follow Google Cloud Vision API usage limits, billing rules, and applicable terms
- Check OCR results before reuse in research outputs, databases, or publications

This tool does not attempt to bypass service limitations or protections.

## Limitations

- OCR accuracy depends heavily on image quality, contrast, resolution, and layout
- Some languages, mixed scripts, or degraded materials may be recognized incorrectly
- Preprocessing may still be necessary for faint, noisy, or shadowed images
- Google Cloud Vision API behavior and output may change over time
- This repository currently provides a practical CLI workflow rather than a full batch management system

## Academic Use

This software was originally developed as a practical research tool for OCR extraction from image-based materials in multilingual research contexts.

Typical use cases include:

- Digital humanities
- Southeast Asian studies
- Historical document processing
- Multilingual image-based text extraction workflows

If you use this software in academic research, a citation to the repository or DOI is appreciated.

## DOI

This repository is archived on Zenodo.

https://doi.org/10.5281/zenodo.18910589

## Citation

If you use this software in your research, please cite:

Kitani, K. (2026).  
Google Cloud Vision Multi-Language OCR Tool (Version 1.5.0).  
Zenodo. https://doi.org/10.5281/zenodo.18910589

## Files in This Repository

- `get_ocr_vision.py` — main CLI script
- `modules/ocr_vision.py` — core OCR processing module
- `lang/en.json` — English UI messages
- `lang/ja.json` — Japanese UI messages
- `README.md` — English documentation
- `README_ja.md` — Japanese documentation
- `LICENSE` — MIT License
- `requirements.txt` — Python dependencies

## Author

**Kimiya Kitani**  
Center for Southeast Asian Studies, Kyoto University

## License

This project is licensed under the **MIT License**.
Copyright (c) 2026 Kimiya Kitani
