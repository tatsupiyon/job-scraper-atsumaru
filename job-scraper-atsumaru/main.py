from utils.scraper import scrape_jobs

if __name__ == "__main__":
    input_html = "samples/html1.html"
    output = scrape_jobs(input_html)
    print(f"完了: {output}")


