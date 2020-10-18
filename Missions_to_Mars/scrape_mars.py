from splinter import Browser
from bs4 import BeautifulSoup
import numpy as np

def init_browser():
    executable_path = {"executable_path": "C:/chromedriver/chromedriver.exe"}
    return Browser("chrome", **executable_path, headless=False)

def scrape():
    browser = init_browser()
    articles = []

    url = "https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest"
    browser.visit(url)

    html = browser.html
    soup = BeautifulSoup(html, "html.parser")
    browser.quit()

    articles_data = soup.find_all(class_='list_text')

    articles = []

    for ea in articles_data:
        articles.append({'title': ea.find(class_='content_title').text, 'paragraph': ea.find(class_='article_teaser_body').text})
    return articles
    

