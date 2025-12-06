import requests
from bs4 import BeautifulSoup
from time import sleep
import pandas as pd

def scrape_jobs(input_html_path, output_csv="atsumaru.csv"):
    with open(input_html_path, "r", encoding="utf-8-sig") as f:
        html = f.read()

    soup = BeautifulSoup(html, "lxml")
    visited = set()
    d_list = []

    li_lists = soup.select("li.bl_slick_item")

    base_url = "https://atsumaru.jp/"
    headers = {"User-Agent": "Mozilla/5.0"}

    for li in li_lists:
        a_tag = li.select_one("figure > a")
        url = base_url + a_tag.get("href")

        try:
            page = requests.get(url, headers=headers, timeout=10)
            sleep(1)

            final_url = page.url
            if final_url in visited:
                continue

            visited.add(final_url)
            soup2 = BeautifulSoup(page.content, "lxml")

            try:
                company_name = soup2.select_one("span.bl_card2_ttl_text").text
            except:
                company_name = "会社名 不明"

            try:
                company_address = soup2.select_one(
                    'td:-soup-contains("地図はこちら") > p'
                ).text
            except:
                company_address = "住所 不明"

            try:
                tel = soup2.select_one("div.telNo strong a")
                tel = tel.text if tel else soup2.select_one("div.telNo").text
            except:
                tel = "電話番号 不明"

            d_list.append(
                {"会社名": company_name, "住所": company_address, "電話番号": tel}
            )

        except:
            print(f"アクセス失敗: {url}")
            continue

    df = pd.DataFrame(d_list)
    df.to_csv(output_csv, index=False, encoding="utf-8-sig")

    return output_csv