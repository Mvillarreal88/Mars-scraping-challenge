from splinter import Browser
from bs4 import BeautifulSoup as bs
import pandas as pd
from webdriver_manager.chrome import ChromeDriverManager
import requests

def scrape_info():

    # Set up Splinter
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

    # Visit URL
    url = "https://redplanetscience.com/"
    browser.visit(url)
    soup = bs(browser.html, 'lxml')

    news_title = soup.find("div", class_ = "content_title").text
    news_paragraph = soup.find("div", class_ = "article_teaser_body").text

    # Visit Image url through splinter module
    url_marsimage = "https://spaceimages-mars.com/"
    browser.visit(url_marsimage)

    # HTML Object
    img_html = browser.html
    img_soup = bs(img_html, "html.parser")

    # Find image url to the full size
    featured_image = img_soup.find("img", class_ = "headerimage fade-in").text + "image/featured/mars2.jpg"

    # Display url of the full image
    featured_image_url = f"https://spaceimages-mars.com/{featured_image}"

    # Visit the galaxy Facts webpage and use Pandas to scrape the table
    url_facts = "https://galaxyfacts-mars.com/"


    # Use Pandas to scrape tabular data from a page
    mars_facts = pd.read_html(url_facts)

    mars_df = mars_facts[0]

    mars_df.columns = ["Description", "Mars", "Earth"]
    mars_df.set_index("Description", inplace=True)

    html_facts = mars_df.to_html()

    # clean up the table
    html_facts.replace("\n", '')

    # Save html code
    mars_df.to_html("mars_facts_data.html")

    html_facts = mars_df.to_html(classes = 'table table-striped')

    # Visit the hemisphere site
    url_hem = "https://marshemispheres.com/"
    hem_response = requests.get(url_hem)
    hem_soup = bs(hem_response.text, 'html.parser')

    browser.visit(url_hem)

    hem_img_urls = []

    hem_links = browser.find_by_css('a.product-item img')

    for link in range(len(hem_links)):
            browser.find_by_css('a.product-item img')[link].click()
            image = browser.links.find_by_text("Sample").first
            
            image_url = image['href']
            pic_title = browser.find_by_css("h2.title").text
            hem_img_urls.append({"image_url": image_url, "pic_title": pic_title})
            browser.back()
            


    mars_data = {
        "news_title": news_title,
        "news_paragraph": news_paragraph,
        "featured_image_url": featured_image_url,
        "mars_facts": html_facts,
        "hem_img_urls": hem_img_urls}
    # Close the browser after scraping

    browser.quit()

    # Return results
    return (mars_data)
