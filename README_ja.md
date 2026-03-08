# get_ocr_googlevision

**Japanese** / [English](README.md) 

Google Cloud Vision API を用いて、ローカル画像ファイルまたはリモート画像 URL から文字を抽出する、軽量な研究用 OCR ツールです。
ベトナム語、タイ語、中国語、日本語、ラオ語など、複数言語・複数文字体系が混在する資料の実務的な OCR 利用を想定しています。

## 概要

このリポジトリは、Google Cloud Vision の Document Text Detection を使いやすい CLI として包んだ小規模ツールです。
主な用途は次のとおりです。

- ローカル画像の OCR
- リモート画像 URL の OCR
- 言語ヒントによる認識精度の補助
- JSON による簡易 UI 多言語化
- 他の研究ワークフローへ流用しやすいモジュール構成

大きなフレームワークではなく、再利用しやすい研究ツールとして整理しています。

## 特徴

- シンプルな CLI
- Google Cloud Vision API ベースの OCR
- 言語ヒント未指定時は自動判定モード
- `vi,th,ja` のようなカンマ区切りヒント指定に対応
- `lang/` に英語・日本語の UI メッセージを配置
- コア処理を `modules/ocr_vision.py` に分離

## ディレクトリ構成

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

## 動作要件

- Python 3.10 以上
- Vision API を有効化した Google Cloud プロジェクト
- 認証用サービスアカウント JSON キー

依存関係のインストール:

```bash
pip install -r requirements.txt
```

## セットアップ

### 1. 仮想環境の作成

```bash
python -m venv .venv
source .venv/bin/activate
```

Windows の場合:

```bat
.venv\Scripts\activate
```

### 2. 認証情報の準備

Google Cloud 側でサービスアカウントを作成し、Vision API を有効化し、JSON キーを取得します。
その後、環境変数を設定します。

```bash
export GOOGLE_APPLICATION_CREDENTIALS="/path/to/service-account-key.json"
```

PowerShell の場合:

```powershell
$env:GOOGLE_APPLICATION_CREDENTIALS="C:\path\to\service-account-key.json"
```

## 使い方

### ローカル画像

```bash
python get_ocr_vision.py ./samples/image.jpg
```

### リモート画像 URL

```bash
python get_ocr_vision.py "https://example.org/image.jpg"
```

### UI 表示言語を指定

```bash
python get_ocr_vision.py ./samples/image.jpg --lang en
python get_ocr_vision.py ./samples/image.jpg --lang ja
```

### OCR 言語ヒントを指定

```bash
python get_ocr_vision.py ./samples/image.jpg --ocr-hint "vi,lo"
```

### 自動判定を明示

```bash
python get_ocr_vision.py ./samples/image.jpg --ocr-hint auto
```

## 言語ヒントについて

言語ヒントは、難読資料や混在スクリプト資料では OCR 精度の改善に役立つことがあります。
ただし、完全な認識を保証するものではないため、研究利用では原画像との照合が必要です。

例:

- `vi` ベトナム語
- `th` タイ語
- `zh` 中国語
- `ja` 日本語
- `lo` ラオ語

## 想定利用例

- 寺院看板や碑文の読取り
- 葬送本・追悼資料の OCR
- 多言語アーカイブ画像の確認
- フィールド調査で撮影した文書画像の読取り
- 構造化メタデータ作成前の探索的 OCR



## ライセンス

このプロジェクトは MIT License で公開しています。詳細は `LICENSE` を参照してください。

Copyright (c) 2026 Kimiya Kitani


## 作成者

Kimiya Kitani
