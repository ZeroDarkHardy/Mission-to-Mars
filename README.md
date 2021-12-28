# Mission-to-Mars

## Overview of Project

Using BeautifulSoup, Splinter, Pandas, and WebDriver Manager, our goal was to scrape information and images related to the planet Mars, and then display the scraped data on a user-friendly webpage using Flask and MongoDB.

## Scraping the Data

We wanted our webpage to include:
- Recent news about Mars from [RedPlanetScience.com](http://redplanetscience.com).
- A recent "Featured Image" from the [Jet Propulsion Laboratory](https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/index.html) page at the California Institute of Technology.  These are images taken by satellites orbiting Mars.
- A table of facts about Mars from [Galaxy Facts](https://galaxyfacts-mars.com) with comparitive information on Earth.
- Current, high-resolution images of the various hemispheres of Mars scraped from [marshemispheres.com](http://marshemispheres.com)
- An interactive button that initiates a new scrape of all the sites, and a date/time readout showing when the data was last updated.

## Delieverable 1 (Scrape Full-Resolution Mars Hemisphere Images and Titles):

We created a file with Jupyter Notebook, ["Mission_to_Mars_Challenge.ipynb"](https://github.com/ZeroDarkHardy/Mission-to-Mars/blob/main/Mission_to_Mars_Challenge.ipynb), to scrape the various sites and verify our data, to help build our Flask app.  Having already built code to scrape the earlier elements, this deliverable asked us to refactor that code to scrape the full-res image URLs and image titles from [marshemispheres.com](http://marshemispheres.com).

![deliverable_1.png](https://github.com/ZeroDarkHardy/Mission-to-Mars/blob/main/resources/deliverable_1.png)

## Deliverable 2 (Update the Web App with Mars' Hemisphere Images and Titles):

We created [scraping.py](https://github.com/ZeroDarkHardy/Mission-to-Mars/blob/main/scraping.py) to be the workhorse of our scraping site.  Within the file, we created the function "scrape_all()" to return the data we want, but referencing several other functions (mars_news, featured_image, mars_facts) within it.  

![deliverable_2b.png](https://github.com/ZeroDarkHardy/Mission-to-Mars/blob/main/resources/deliverable_2b.png)
Once built, this deliverable asked that we introduce a new function (which I named mars_hemispheres) to scrape and return the titles full-resolution image URLs of Mars' hemispheres, so that they can be added to our MongoDB and finally referenced in our web template.

