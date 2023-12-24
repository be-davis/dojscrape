#%%
from bs4 import BeautifulSoup
import requests
import re
import pandas as pd
from csa_press.common_sense_media.csm import get_search_results

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
    #print(page_data.find('a',{'href': '#pred'}))
    return len(page_data.find('a',{'href': '#pred'}).find_all('span', {'class': 'circle circle-full'}))

    
#%%
num_pages = 8


def get_all_predation_scores():
    app_predation_scores = {}
    for page_num in range(1,num_pages+1):
        page_link = 'https://www.bark.us/app-reviews/page/{}'.format(page_num) + '/?category=all'
        page_app_links = get_all_app_links(page_link)
        for app_link in page_app_links:
            print(app_link)
            app_predation_scores[get_name(app_link)] = get_predation_score(app_link)
    return app_predation_scores
#get_all_predation_scores()

#%%
get_search_results()
def main():
    app_predation_scores = get_all_predation_scores()
    print(app_predation_scores)
    df = pd.DataFrame(pd.Series(app_predation_scores, index=app_predation_scores.keys())).reset_index().rename(columns={'index': 'app_name', 0:'predation_score'})
    df['app_name'] = df['app_name'].str.replace('-',' ').str.replace('review','')
    
    return df
x = main()
#%%
if __name__ == '__main__':
    main()
