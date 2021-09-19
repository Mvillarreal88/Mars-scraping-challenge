from splinter import Browser
from bs4 import BeautifulSoup as bs
import pandas as pd
from webdriver_manager.chrome import ChromeDriverManager


def scrape_info():
    # Set up Splinter
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

    # Visit Mars site
    url = "https://redplanetscience.com/"
    browser.visit(url)

    # Scrape page into Soup
    html = browser.html
    soup = bs(html, "html.parser")

    # results = soup.find_all("div", class_="list_text")
    # result = results[0]

    status = True
    while status:
        try:
            results = soup.find_all('div', class_='list_text')
            result = results[0]
            status = False
        except:
            pass
    
    news_title = result.find("div", class_="content_title").text().strip()
    news_paragraph = result.find("div", class_="article_teaser_body").text().strip()

    # Close the browser after scraping
    browser.quit()

    mars_news_dict ={}
    mars_news_dict['news_title'] = news_title
    mars_news_dict['news_paragraph'] = news_paragraph
    # Return results
    return (mars_news_dict)
