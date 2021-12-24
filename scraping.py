# IMPORT DEPENDENCIES
from splinter import Browser
from bs4 import BeautifulSoup as soup
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd

# SET UP SPLINTER
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)

# VISIT THE MARS NASA NEWS SITE
url = 'https://redplanetscience.com'
browser.visit(url)

# optional delay for loading the page
browser.is_element_present_by_css('div.list_text', wait_time=1)

# Convert the browser html to a soup object and then quit the browser
html = browser.html
news_soup = soup(html, 'html.parser')

slide_elem = news_soup.select_one('div.list_text')

slide_elem.find('div', class_='content_title')

# Use the parent element to find the first 'a' tag and save it as 'news_title'
news_title = slide_elem.find('div', class_='content_title').get_text()
news_title

# use the parent element to find the paragraph text
news_p = slide_elem.find('div', class_='article_teaser_body').get_text()
news_p


# ## JPL SPACE IMAGES FEATURED IMAGE

# VISIT URL
url = 'https://spaceimages-mars.com'
browser.visit(url)

# FIND AND CLICK THE FULL IMAGE BUTTON
full_image_elem = browser.find_by_tag('button')[1]
full_image_elem.click()

# PARSE THE RESULTING HTML WITH SOUP
html = browser.html
img_soup = soup(html, 'html.parser')

# FIND THE RELATIVE IMAGE URL
img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')
img_url_rel

# USE THE BASE URL TO CREATE AN ABSOLUTE URL
img_url = f'https://spaceimages-mars.com/{img_url_rel}'
img_url

# ## MARS FACTS

# CREATE A DATAFRAME FROM THE FIRST TABLE ENCOUNTERED AT GALAXYFACTS-MARS.COM
df = pd.read_html('https://galaxyfacts-mars.com')[0]
df.columns=['description', 'Mars', 'Earth']
df.set_index('description', inplace=True)
df

# CONVERT DATAFRAME BACK INTO HTML TO USE WITH OUR WEB APPLICATION
df.to_html()

# CLOSE THE BROWSER WINDOW
browser.quit()

