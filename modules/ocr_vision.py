"""
Author: Kimiya Kitani
Description: A wrapper for Google Cloud Vision API to perform OCR on local or remote images.
License: MIT License (See LICENSE file for details)
Version: 1.1
Date: 25 Feb 2026
"""

import os
import json
import warnings
from google.cloud import vision

# ==========================================
# グローバル設定・メッセージ定義
# ==========================================
# デフォルトのOCR言語ヒント (指定がない場合のフォールバック)
DEFAULT_LANGUAGE_HINTS = ["vi", "th", "zh", "ja"]

# 言語ファイル読み込み失敗時の緊急用メッセージ
EMERGENCY_MESSAGES = {
    "MSG_ERR_API_RESPONSE": "Error: {error}", 
    "MSG_ERR_FILE_NOT_FOUND": "File not found: {path}"
}

# Pythonの警告表示設定
HIDE_PYTHON_WARNINGS = True
if HIDE_PYTHON_WARNINGS:
    warnings.filterwarnings("ignore", category=FutureWarning, module="google.api_core")
# ==========================================

class LanguageLoader:
    def __init__(self, lang_code="en"):
        self.lang_code = lang_code
        self.messages = {}
        self._load_messages()

    def _load_messages(self):
        current_dir = os.path.dirname(__file__)
        base_dir = os.path.dirname(current_dir)
        lang_file = os.path.join(base_dir, "lang", f"{self.lang_code}.json")
        
        if not os.path.exists(lang_file):
            lang_file = os.path.join(base_dir, "lang", "en.json")
            
        try:
            with open(lang_file, "r", encoding="utf-8") as f:
                self.messages = json.load(f)
        except Exception:
            # グローバル定数からロード
            self.messages = EMERGENCY_MESSAGES

    def get(self, key):
        return self.messages.get(key, key)

class VisionAPIWrapper:
    def __init__(self, language_hints=None, lang_code="en"):
        """
        :param language_hints: OCR用の言語コードリスト。Noneの場合はデフォルト、空リスト[]の場合はAPIの自動判定。
        :param lang_code: UI表示（エラー等）に使用する言語。
        """
        self.client = vision.ImageAnnotatorClient()
        self.lang = LanguageLoader(lang_code)
        
        # language_hintsがNoneならデフォルトを使用。
        # 空のリスト [] が渡された場合は、そのまま空リストとして扱いAPIの自動判定を促す。
        hints = language_hints if language_hints is not None else DEFAULT_LANGUAGE_HINTS
        self.image_context = vision.ImageContext(language_hints=hints)

    def _is_url(self, target):
        return target.startswith(('http://', 'https://'))

    def _prepare_image(self, path_or_url):
        image = vision.Image()
        if self._is_url(path_or_url):
            image.source.image_uri = path_or_url
        else:
            if not os.path.exists(path_or_url):
                error_msg = self.lang.get("MSG_ERR_FILE_NOT_FOUND").format(path=path_or_url)
                raise FileNotFoundError(error_msg)
            with open(path_or_url, 'rb') as f:
                image.content = f.read()
        return image

    def execute_ocr(self, path_or_url):
        image = self._prepare_image(path_or_url)
        response = self.client.document_text_detection(
            image=image, 
            image_context=self.image_context
        )

        if response.error.message:
            error_msg = self.lang.get("MSG_ERR_API_RESPONSE").format(error=response.error.message)
            raise Exception(error_msg)

        return response.full_text_annotation.text