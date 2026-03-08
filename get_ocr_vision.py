#!/usr/bin/env python3
"""
Google Cloud Vision Multi-Language OCR Tool

Author: Kimiya Kitani
Affiliation: Center for Southeast Asian Studies, Kyoto University
License: MIT License (see LICENSE)
Version: 1.5.0
Release date: 2026-03-08
DOI: https://doi.org/10.5281/zenodo.18910589

Description:
    Command-line OCR tool for extracting text from local image files or remote image URLs
    using Google Cloud Vision API. The tool supports multilingual OCR workflows and allows
    optional language hints such as vi, th, zh, ja, and lo.

Typical usage:
    python get_ocr_vision.py ./image.jpg
    python get_ocr_vision.py ./image.jpg --lang en
    python get_ocr_vision.py ./image.jpg --ocr-hint "vi,th,zh,ja"
    python get_ocr_vision.py "https://example.org/image.jpg" --ocr-hint auto

Notes:
    - Set GOOGLE_APPLICATION_CREDENTIALS before execution.
    - Do not commit service account keys or credentials files.
    - OCR accuracy depends on image quality and source layout.
"""

import sys
import os
import argparse
from modules.ocr_vision import VisionAPIWrapper, LanguageLoader

# ==========================================
# Global configuration and message definitions
# ==========================================
DEFAULT_UI_LANG = "en"

MSG_INFO_OCR_HINTS   = "OCR Language hints: {hints}" 
MSG_INFO_AUTO_DETECT = "OCR Language: Automatic detection mode (No hints provided)"
MSG_ERR_CRITICAL     = "Critical Error: {error}"
# ==========================================

def main():
    parser = argparse.ArgumentParser(description="Vision OCR Tool")
    parser.add_argument("target", help="Target image path or URL")
    parser.add_argument("--lang", type=str, default=None, 
                        help="Set UI language (e.g., ja, en).")
    parser.add_argument("--ocr-hint", type=str, default=None,
                        help="Language hint(s) for OCR, comma-separated (e.g., --ocr-hint=\"vi,lo\"). Use 'auto' for automatic detection.")

    args = parser.parse_args()

    base_dir = os.path.dirname(__file__)
    if args.lang:
        ui_lang_code = args.lang
    else:
        ui_lang_code = "ja" if os.path.exists(os.path.join(base_dir, "lang", "ja.json")) else DEFAULT_UI_LANG

    ui_lang = LanguageLoader(ui_lang_code)
    ocr_hints_list = []

    if args.ocr_hint:
        if args.ocr_hint.lower() == "auto":
            ocr_hints_list = []
        else:
            ocr_hints_list = [h.strip() for h in args.ocr_hint.split(',')]
    elif args.lang:
        ocr_hints_list = [args.lang]
    else:
        ocr_hints_list = []

    ocr_tool = VisionAPIWrapper(language_hints=ocr_hints_list, lang_code=ui_lang_code)

    try:
        print(ui_lang.get("MSG_STATUS_START").format(target=args.target))

        if not ocr_hints_list:
            print(MSG_INFO_AUTO_DETECT)
        else:
            print(MSG_INFO_OCR_HINTS.format(hints=", ".join(ocr_hints_list)))

        result_text = ocr_tool.execute_ocr(args.target)

        print(ui_lang.get("MSG_RESULT_HEADER"))
        print(result_text)

    except Exception as e:
        print(MSG_ERR_CRITICAL.format(error=e))

if __name__ == "__main__":
    main()
