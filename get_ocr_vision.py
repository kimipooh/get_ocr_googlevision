"""
Author: Kimiya Kitani
License: MIT License (See LICENSE file for details)
Version: 1.0
Date: 11 Feb 2026
Description: Main execution script for the Vision OCR tool.
"""

import sys
import os
from ocr_vision import VisionAPIWrapper, LanguageLoader

def main(target):
    """
    Main entry point. Detects environment language and executes OCR.
    """
    # --- UI Localization Logic ---
    # Automatically switch to Japanese if the 'ja.json' file exists in the lang folder.
    base_dir = os.path.dirname(__file__)
    lang_code = "ja" if os.path.exists(os.path.join(base_dir, "lang", "ja.json")) else "en"
    
    # Load localized strings for this main script
    ui_lang = LanguageLoader(lang_code)
    
    # Initialize the OCR tool with the appropriate UI language
    ocr_tool = VisionAPIWrapper(lang_code=lang_code)

    try:
        # Display analysis start message
        print(ui_lang.get("MSG_STATUS_START").format(target=target))
        
        # Execute the OCR process
        result_text = ocr_tool.execute_ocr(target)
        
        # Output the results
        print(ui_lang.get("MSG_RESULT_HEADER"))
        print(result_text)
        
    except Exception as e:
        # Handle and display errors using localized messages
        print(ui_lang.get("MSG_ERR_GENERAL").format(error=e))

if __name__ == "__main__":
    # Ensure a target path or URL is provided as a command line argument
    if len(sys.argv) == 2:
        main(sys.argv[1])
    else:
        # If arguments are missing, show the usage instructions in the localized language
        base_dir = os.path.dirname(__file__)
        lang_code = "ja" if os.path.exists(os.path.join(base_dir, "lang", "ja.json")) else "en"
        ui_lang = LanguageLoader(lang_code)
        print(ui_lang.get("USAGE").format(program=sys.argv[0]))