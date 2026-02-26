"""
Author: Kimiya Kitani
License: MIT License (See LICENSE file for details)
Version: 1.5
Date: 25 Feb 2026
Description: Vision OCR tool supporting comma-separated language hints (e.g., --ocr-hint="vi,lo").
"""

import sys
import os
import argparse
from ocr_vision import VisionAPIWrapper, LanguageLoader

# ==========================================
# グローバル設定・メッセージ定義
# ==========================================
# UI言語のファイルが見つからない場合のデフォルト
DEFAULT_UI_LANG = "en"

# 実行時の通知メッセージ
MSG_INFO_OCR_HINTS   = "OCR Language hints: {hints}" 
MSG_INFO_AUTO_DETECT = "OCR Language: Automatic detection mode (No hints provided)"

# 致命的なエラーが発生した際のエラーメッセージ
MSG_ERR_CRITICAL     = "Critical Error: {error}"
# ==========================================

def main():
    # --- 引数の解析 ---
    parser = argparse.ArgumentParser(description="Vision OCR Tool")
    parser.add_argument("target", help="Target image path or URL")
    
    # UI表示言語の切り替え
    parser.add_argument("--lang", type=str, default=None, 
                        help="Set UI language (e.g., ja, en).")
    
    # OCR言語ヒント。カンマ区切りの文字列を受け取るように変更
    parser.add_argument("--ocr-hint", type=str, default=None,
                        help="Language hint(s) for OCR, comma-separated (e.g., --ocr-hint=\"vi,lo\"). Use 'auto' for automatic detection.")
    
    args = parser.parse_args()

    # --- 1. UI言語コードの決定 ---
    base_dir = os.path.dirname(__file__)
    if args.lang:
        ui_lang_code = args.lang
    else:
        # ja.jsonがあれば日本語、なければデフォルト(en)
        ui_lang_code = "ja" if os.path.exists(os.path.join(base_dir, "lang", "ja.json")) else DEFAULT_UI_LANG

    # UI用メッセージローダー
    ui_lang = LanguageLoader(ui_lang_code)

    # --- 2. Google Vision OCR用言語ヒントの処理 ---
    ocr_hints_list = []

    if args.ocr_hint:
        # 'auto' が指定された場合は空リスト（APIの自動判別）
        if args.ocr_hint.lower() == "auto":
            ocr_hints_list = []
        else:
            # カンマで分割し、前後の空白を除去してリスト化
            ocr_hints_list = [h.strip() for h in args.ocr_hint.split(',')]
    elif args.lang:
        # --lang の指定がある場合は、それをヒントとして採用
        ocr_hints_list = [args.lang]
    else:
        # 何も指定がない場合は空リスト（自動判別）
        ocr_hints_list = []

    # --- 3. OCRツールの実行 ---
    # ocr_vision.py 側の VisionAPIWrapper(language_hints=...) にリストを渡す
    ocr_tool = VisionAPIWrapper(language_hints=ocr_hints_list, lang_code=ui_lang_code)

    try:
        # 処理開始の通知
        print(ui_lang.get("MSG_STATUS_START").format(target=args.target))
        
        if not ocr_hints_list:
            print(MSG_INFO_AUTO_DETECT)
        else:
            # 設定されたヒントをカンマ区切りで表示
            print(MSG_INFO_OCR_HINTS.format(hints=", ".join(ocr_hints_list)))
        
        # OCRプロセスの実行
        result_text = ocr_tool.execute_ocr(args.target)
        
        # 結果の出力
        print(ui_lang.get("MSG_RESULT_HEADER"))
        print(result_text)
        
    except Exception as e:
        # グローバル変数を利用したエラー表示
        print(MSG_ERR_CRITICAL.format(error=e))

if __name__ == "__main__":
    main()