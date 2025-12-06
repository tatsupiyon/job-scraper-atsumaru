# job-scraper-atsumaru
Atsumaru（あつまる求人）掲載ページから、企業名・住所・電話番号を自動取得し、CSV にまとめるスクレイピングツールです。

requests + BeautifulSoup を使用した軽量構成で、求人系のデータ取得案件のサンプルとして利用できます。

---

## 🚀 機能

- BeautifulSoup4 を使った HTML パース  
- 求人リンクを抽出して個別ページへアクセス  
- 会社名 / 住所 / 電話番号を自動抽出  
- 重複 URL をスキップ（無駄なアクセスを防止）  
- CSV に整形して出力  

---

## 📦 使用している技術

- Python 3.x  
- requests  
- BeautifulSoup4（bs4）  
- lxml  
- pandas  

---

## 🔧 インストール

```bash
git clone https://github.com/<あなたのアカウント名>/job-scraper-atsumaru.git
cd job-scraper-atsumaru

pip install -r requirements.txt

## ▶️ 使い方
- 1:samples/html1.html にスクレイピング対象の求人一覧 HTML を置く
- 2:実行 python main.py
- 3:下記ファイルが作成されます：atsumaru.csv








