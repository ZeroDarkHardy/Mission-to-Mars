# IMPORT DEPENDENCIES
from splinter import Browser
from bs4 import BeautifulSoup as soup
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import datetime as dt
import time

# INITIATE HEADLESS DRIVER FOR DEPLOYMENT
def scrape_all():
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=True)
    news_title, news_paragraph = mars_news(browser)
    
    data = {
        "news_title": news_title,
        "news_paragraph": news_paragraph,
        "featured_image": featured_image(browser),
        "facts": mars_facts(),
        "hemispheres": mars_hemispheres(browser),
        "last_modified": dt.datetime.now()
    }

    # Stop Webdriver and return data
    browser.quit()
    return data

def mars_news(browser):
    # VISIT THE MARS NASA NEWS SITE
    url = 'https://redplanetscience.com'
    browser.visit(url)

    # optional delay for loading the page
    browser.is_element_present_by_css('div.list_text', wait_time=1)

    # Convert the browser html to a soup object and then quit the browser
    html = browser.html
    news_soup = soup(html, 'html.parser')
    
    # add try/except for error handling
    try:
        slide_elem = news_soup.select_one('div.list_text')

        news_title = slide_elem.find('div', class_='content_title')

        # Use the parent element to find the first 'a' tag and save it as 'news_title'
        news_title = slide_elem.find('div', class_='content_title').get_text()

        # use the parent element to find the paragraph text
        news_p = slide_elem.find('div', class_='article_teaser_body').get_text()

    except AttributeError:
        return None, None
    
    return news_title, news_p

# ## JPL SPACE IMAGES FEATURED IMAGE

# VISIT URL
def featured_image(browser):
    # visit URL
    url = 'https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/index.html'
    browser.visit(url)
# FIND AND CLICK THE FULL IMAGE BUTTON
    full_image_elem = browser.find_by_tag('button')[1]
    full_image_elem.click()

    # PARSE THE RESULTING HTML WITH SOUP
    html = browser.html
    img_soup = soup(html, 'html.parser')

    # FIND THE RELATIVE IMAGE URL
    try:
        img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')

    except AttributeError:
        return None

    # USE THE BASE URL TO CREATE AN ABSOLUTE URL
    img_url = f'https://spaceimages-mars.com/{img_url_rel}'
    
    return img_url
# ## MARS FACTS
def mars_facts():
# CREATE A DATAFRAME FROM THE FIRST TABLE ENCOUNTERED AT GALAXYFACTS-MARS.COM
    try:
        df = pd.read_html('https://galaxyfacts-mars.com')[0]
    except BaseException:
        return None
    df.columns=['description', 'Mars', 'Earth']
    df.set_index('description', inplace=True)
    

    # CONVERT DATAFRAME BACK INTO HTML TO USE WITH OUR WEB APPLICATION
    return df.to_html(classes="table table-striped")

# ## MARS HEMISPHERES
def mars_hemispheres(browser):
    url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(url)

    time.sleep(1)

    # Parse the html data
    hemi_html = browser.html
    hemi_soup = soup(hemi_html, 'html.parser')
    items = hemi_soup.find_all('div', class_='item')
    # 2. Create a list to hold the images and titles.
    hemisphere_image_urls = []

    # 3. Write code to retrieve the image urls and titles for each hemisphere.
    hemi_url = "https://astrogeology.usgs.gov/"

    for x in items:
        # create dictionary to hold titles and urls for full resolution images
        hemi_dict = {}
        title = x.find('h3').text
        # create links for full resolution images
        link_url = x.find('a', class_='itemLink product-item')['href']
        browser.visit(hemi_url + link_url)
        # parse resulting html
        img_html = browser.html
        img_soup = soup(img_html, 'html.parser')
        # identify urls for full resolution images
        downloads = img_soup.find('div', class_='downloads')
        img_url = downloads.find('a')['href']
        
        # append dictionary
        hemi_dict['title'] = title
        hemi_dict['img_url'] = img_url
        hemisphere_image_urls.append(hemi_dict)
        browser.back()
    
    return hemisphere_image_urls

if __name__ == "__main__":

    # if running as script, print scraped data
    print(scrape_all())