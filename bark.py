#%%
from bs4 import BeautifulSoup
import requests
import re

from splink.duckdb.linker import DuckDBLinker
import splink.duckdb.comparison_library as cl
import splink.duckdb.comparison_template_library as ctl
from splink.duckdb.blocking_rule_library import block_on
from splink.datasets import splink_datasets


# %%
all_apps_link = 'https://www.bark.us/app-reviews/page/1/?category=all'

#snapchat, for example
base_link = 'https://www.bark.us/app-reviews/apps/'
# %%
def get_all_app_links(pl):
    page_data = BeautifulSoup(requests.get(pl).content, 'lxml')
    app_data = page_data.find_all('a',{'href': re.compile('/app-reviews/'),
                                               'class': 'listing-card-link'})
    app_links = []
    for app in app_data:
        app_links.append(str(app['href']))
    return app_links
def get_name(link):
    return re.search(r'https://www.bark.us/app-reviews/apps/(.*?)/', link).group(1)
def get_predation_score(link):
    page_data = BeautifulSoup(requests.get(link).content, 'lxml')
    return len(page_data.find('a',{'href': '#pred'}).find_all('span', {'class': 'circle circle-full'}))
def remove_extra_chars(app_name):
    if '-review' in app_name:
        return app_name.replace('-review','').replace('-', ' ')
        
    else:
        return app_name.replace('-', ' ')
    
#%%
num_pages = 8
app_predations_scores = {}

def get_all_predation_scores():
    for page_num in range(1,num_pages+1):
        page_link = 'https://www.bark.us/app-reviews/page/{}'.format(page_num) + '/?category=all'
        page_app_links = get_all_app_links(page_link)
        for app_link in page_app_links:
            app_predations_scores[get_name(app_link)] = get_predation_score(app_link)
    return app_predations_scores
get_all_predation_scores()
app_predations_scores
#%%
import pandas as pd
df = pd.DataFrame(pd.Series(app_predations_scores, index=app_predations_scores.keys())).reset_index()
df['index'] = df['index'].str.replace('-',' ').str.replace('review','')