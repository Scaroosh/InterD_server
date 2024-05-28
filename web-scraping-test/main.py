import requests
from bs4 import BeautifulSoup
import os
import time
import re


def sanitize_filename(filename):
    return re.sub(r'[\\/*?:"<>|]', "", filename)


def scrape_article(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    title_tag = soup.find('h1', class_='article_title')
    title = title_tag.text.strip() if title_tag else "Title not found"
    title = sanitize_filename(title)

    article_text = ''
    article_content = soup.find('div', class_='content_text')
    if article_content:
        for p in article_content.find_all('p'):
            article_text += p.text.strip() + '\n'

    folder_name = 'scraped_articles'
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

    file_name = os.path.join(folder_name, f"{title[:50]}.txt")  # Limit the filename length to 50 characters
    with open(file_name, 'w', encoding='utf-8') as file:
        file.write(f"Article Title: {title}\n\n")
        file.write(f"Article Text:\n{article_text}")

    print(f"Article saved to {file_name}")


def scrape_articles_from_search(url):
    page = 1
    while True:
        page_url = f"{url}&page={page}"
        response = requests.get(page_url)
        soup = BeautifulSoup(response.text, 'html.parser')

        articles = soup.find_all('div', class_='row news-item start-xs')
        if not articles:
            break

        for article in articles:
            article_url = article.find('a', href=True)['href']
            full_article_url = f"https://cryptonews.net{article_url}"
            scrape_article(full_article_url)

        page += 1
        time.sleep(2)


if __name__ == "__main__":
    query = input("Enter search keywords: ")
    print("Enter the news category ID from the list (default is -1):")
    print(" -1  : Latest news")
    print(" -2  : Video")
    print("  1  : Bitcoin")
    print("  14 : DeFi")
    print("  15 : NFT")
    print("  2  : Ethereum")
    print("  3  : Altcoins")
    print("  4  : Blockchain")
    print("  6  : Mining")
    print("  7  : Finance")
    print("  18 : Metaverse")
    print("  8  : Legal")
    print("  9  : Security")
    print("  10 : Analytics")
    print("  11 : Exchange")
    print("  12 : Other")
    print("  16 : GameFi")
    print("  5  : ICO")
    rubric_id = input("Category ID: ") or "-1"

    search_url = f'https://cryptonews.net/?q={query}&rubricId={rubric_id}'

    scrape_articles_from_search(search_url)
