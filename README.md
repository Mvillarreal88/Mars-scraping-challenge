# web-scraping-challenge


## Initial Scraping

In this activity I do an initial scrape using Jupyter notebook, BeautifulSoup, Pandas and requests on the Mars news website. This returns the following information needed for our scrape.

Total scrapes are 4 different scrapes to get information:

* Mars News:
  * Grabs the first news headline and paragraphs.

* Space images
  * Using splinter navigate to the site to grab the featured image and save as URL string
 
* Mars Facts
  * Using pandas I was able to scrape the Mars facts webpage to grab the table and turn it into a HTML table string

* Mars Hemispheres
  * Visited the Astrology site to obtain high resolution images for each of Mars's hemispheres. Saved these as URL links, and grabbed the titles.


## MongoDB and Flask Application

I then used the MongoDB with Flask templating to create an HTML site to display the data that was scraped from the news sites.

>- Matthew Villarreal
