# Google Cloud Vision 多言語OCRツール

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.18910589.svg)](https://doi.org/10.5281/zenodo.18910589)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](#インストール)
[![English](https://img.shields.io/badge/README-English-green.svg)](README.md)

Google Cloud Vision API を用いて、多言語画像からテキストを抽出するための研究用OCRツールです。

このツールは、ローカル画像ファイルおよびリモート画像URLを対象として、コマンドラインから実行できます。特に、ベトナム語、タイ語、中国語、日本語などを含む多言語資料の研究利用を想定しています。

## 主な機能

- Google Cloud Vision API を利用した OCR
- ローカル画像と画像URLの両方に対応
- `--ocr-hint` による言語ヒント指定、または自動認識
- `lang/` 配下の JSON による英語・日本語UI
- `modules/ocr_vision.py` によるモジュール化された実装
- 研究用途のOCR・文字抽出ワークフローに適した構成

## インストール

### 必要条件

- Python 3.10 以上
- Vision API を有効化した Google Cloud プロジェクト
- Google Cloud Vision API 用サービスアカウント鍵

### セットアップ

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
export GOOGLE_APPLICATION_CREDENTIALS="service-account-key.json"
```

Windows では仮想環境の有効化に次を利用します。

```bash
.venv\Scripts\activate
```

## 使い方

### 基本実行

```bash
python get_ocr_vision.py ./samples/image.jpg
```

### UI表示言語の指定

```bash
python get_ocr_vision.py ./samples/image.jpg --lang ja
```

### OCR言語ヒントの指定

```bash
python get_ocr_vision.py ./samples/image.jpg --ocr-hint "vi,th,zh,ja"
```

### 自動判別

```bash
python get_ocr_vision.py ./samples/image.jpg --ocr-hint auto
```

### リモート画像URL

```bash
python get_ocr_vision.py "https://example.org/sample.jpg" --ocr-hint "vi,lo"
```

## ディレクトリ構成

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

本ツールは Google Cloud Vision API を利用して画像OCRを行います。

利用にあたっては、次の点に注意してください。

- 処理対象画像を利用する権利があることを確認する
- 著作権、プライバシー、データ所有権を尊重する
- 機密性の高い画像や情報を外部APIへ送信してよいか事前に確認する
- Google Cloud Vision API の利用制限、課金、利用条件に従う
- 研究成果やデータベースに再利用する前にOCR結果を必ず確認する

本ツールはサービス制限や保護機構の回避を目的とするものではありません。

## 制限事項

- OCR精度は画像品質、コントラスト、解像度、レイアウトに大きく依存します
- 言語混在や劣化資料では誤認識が生じる場合があります
- 薄い文字、ノイズ、影のある画像では前処理が必要なことがあります
- Google Cloud Vision API の仕様変更により結果が変わる可能性があります
- 本リポジトリは実用的なCLIワークフローを提供するものであり、完全なバッチ管理システムではありません

## Academic Use

本ソフトウェアは、多言語研究資料に対する画像OCRのための実用的な研究ツールとして開発されました。

想定される利用例:

- デジタル・ヒューマニティーズ
- 東南アジア研究
- 歴史資料処理
- 多言語画像資料からの文字抽出ワークフロー

研究で利用する場合は、リポジトリまたは DOI の引用をご検討ください。

## DOI

本リポジトリは Zenodo にアーカイブされています。

https://doi.org/10.5281/zenodo.18910589

## Citation

研究で本ソフトウェアを利用する場合は、次のように引用してください。

Kitani, K. (2026).  
Google Cloud Vision Multi-Language OCR Tool (Version 1.5.0).  
Zenodo. https://doi.org/10.5281/zenodo.18910589

## リポジトリ内の主なファイル

- `get_ocr_vision.py` — メインCLIスクリプト
- `modules/ocr_vision.py` — OCR処理の中核モジュール
- `lang/en.json` — 英語UIメッセージ
- `lang/ja.json` — 日本語UIメッセージ
- `README.md` — 英語版ドキュメント
- `README_ja.md` — 日本語版ドキュメント
- `LICENSE` — MITライセンス
- `requirements.txt` — Python依存関係

## Author

**Kimiya Kitani**  
京都大学東南アジア地域研究研究所

## License

本プロジェクトは **MIT License** の下で公開されています。
Copyright (c) 2026 Kimiya Kitani
