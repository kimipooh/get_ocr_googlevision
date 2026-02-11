"""
Author: Kimiya Kitani
Description: A wrapper for Google Cloud Vision API to perform OCR on local or remote images.
License: MIT License (See LICENSE file for details)
Version: 1.0
Date: 11 Feb 2026
Usage Reminder:
    1. Ensure the 'lang/' directory exists with 'en.json' and 'ja.json'.
    2. Place your Google Cloud 'service-account-key.json' in the project root.
    3. Set the environment variable: 
       export GOOGLE_APPLICATION_CREDENTIALS="service-account-key.json"
"""

import os
import json
import warnings
from google.cloud import vision

# --- Global configuration variables ---

# Default language hints for OCR (Vietnamese, Thai, Chinese, Japanese)
# Providing these hints significantly improves recognition accuracy for specific scripts.
DEFAULT_LANGUAGE_HINTS = ["vi", "th", "zh", "ja"]

# If True, suppresses the FutureWarning related to older Python versions in Google libraries.
HIDE_PYTHON_WARNINGS = True

if HIDE_PYTHON_WARNINGS:
    # Specifically ignore FutureWarnings from the Google API core module
    warnings.filterwarnings("ignore", category=FutureWarning, module="google.api_core")

class LanguageLoader:
    """
    Utility class to load UI messages from JSON files in the 'lang' directory.
    This allows for easy switching between Japanese (ja) and English (en).
    """
    def __init__(self, lang_code="en"):
        # The language code to load (e.g., 'en' or 'ja')
        self.lang_code = lang_code
        # Dictionary to store localized strings
        self.messages = {}
        self._load_messages()

    def _load_messages(self):
        """Loads the JSON file corresponding to the current lang_code."""
        base_dir = os.path.dirname(__file__)
        lang_file = os.path.join(base_dir, "lang", f"{self.lang_code}.json")
        
        # Fallback to English if the requested language file is missing
        if not os.path.exists(lang_file):
            lang_file = os.path.join(base_dir, "lang", "en.json")
            
        try:
            with open(lang_file, "r", encoding="utf-8") as f:
                self.messages = json.load(f)
        except Exception:
            # Emergency strings if JSON loading fails entirely
            self.messages = {
                "MSG_ERR_API_RESPONSE": "Error: {error}", 
                "MSG_ERR_FILE_NOT_FOUND": "File not found: {path}"
            }

    def get(self, key):
        """Returns the localized string for a given key."""
        return self.messages.get(key, key)

class VisionAPIWrapper:
    """
    Core class to interact with Google Cloud Vision API.
    Handles image preparation and OCR execution.
    """
    def __init__(self, language_hints=None, lang_code="en"):
        """
        Initializes the Vision API client and language settings.
        :param language_hints: List of language codes for OCR accuracy.
        :param lang_code: Code for the UI output language.
        """
        # Initialize the Google Cloud Vision client (uses GOOGLE_APPLICATION_CREDENTIALS)
        self.client = vision.ImageAnnotatorClient()
        # Initialize the localization helper
        self.lang = LanguageLoader(lang_code)
        
        # Use provided hints or fallback to the global default
        hints = language_hints if language_hints is not None else DEFAULT_LANGUAGE_HINTS
        # Set up the context for the API request
        self.image_context = vision.ImageContext(language_hints=hints)

    def _is_url(self, target):
        """Checks if the input string is a web URL."""
        return target.startswith(('http://', 'https://'))

    def _prepare_image(self, path_or_url):
        """Prepares a Vision API Image object from a local file or a URL."""
        image = vision.Image()
        if self._is_url(path_or_url):
            # Tell Google to fetch the image from the URL
            image.source.image_uri = path_or_url
        else:
            # Read image data from the local file system
            if not os.path.exists(path_or_url):
                error_msg = self.lang.get("MSG_ERR_FILE_NOT_FOUND").format(path=path_or_url)
                raise FileNotFoundError(error_msg)
            with open(path_or_url, 'rb') as f:
                image.content = f.read()
        return image

    def execute_ocr(self, path_or_url):
        """
        Performs Document Text Detection on the target image.
        Returns the full text as a string.
        """
        image = self._prepare_image(path_or_url)
        # Call the high-accuracy document detection method
        response = self.client.document_text_detection(
            image=image, 
            image_context=self.image_context
        )

        if response.error.message:
            error_msg = self.lang.get("MSG_ERR_API_RESPONSE").format(error=response.error.message)
            raise Exception(error_msg)

        return response.full_text_annotation.text