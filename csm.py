#%%
from bs4 import BeautifulSoup
import requests
import re
html = requests.get('https://www.commonsensemedia.org/app-reviews/dont-let-the-pigeon-run-this-app')
soup = BeautifulSoup(html.text, "lxml") # lxml is just the parser for reading the html

star_rating = str(soup.find('div', {'class': "rating rating--inline rating--lg"}))
def get_num_stars():
    return len(re.findall( r'class="icon-star-rating', star_rating))

# %%
# %%
