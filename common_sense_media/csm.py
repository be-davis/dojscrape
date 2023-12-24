#%%
"""
Pulls app review data from Common Sense Media Non-Profit
"""
from bs4 import BeautifulSoup
import requests
import re
import pandas as pd
import datetime
import os
#%%
APP_NAME = input('What app are you looking for?  ')
NOW = datetime.datetime.now().strftime("%m-%d-%Y-%H:%M:%S")
def get_possible_apps():
    
    link = 'https://www.commonsensemedia.org/search/category/app/' + APP_NAME
    page_data = BeautifulSoup(requests.get(link).content, 'lxml')
    possible_apps = page_data.find_all('a',{
                                    'href':re.compile('/app-reviews/'),
                                    'class':'link link--title'})
    app_info = {}
    for app in possible_apps:
        app_info[app.get_text()] = app['href']

    return app_info

def get_soup(html_str):
    html = requests.get(html_str)
    return BeautifulSoup(html.text, 'lxml')

def get_num_stars(html_str):
    soup = get_soup(html_str=html_str)
    star_rating = str(soup.find('div', {'class': "rating rating--inline rating--lg"}))
    return len(re.findall( r'class="icon-star-rating active', star_rating))
def get_sexuality_score(html_str):
    soup = get_soup(html_str=html_str)
    sexuality_star_rating = str(soup.find('button',{'id': "content-grid-item-sex-score"}))
    return len(re.findall(r'class="icon-circle-solid active"', sexuality_star_rating))
def get_language_score(html_str):
    soup = get_soup(html_str=html_str)
    language_star_rating = str(soup.find('button',{'id': "content-grid-item-language-score"}))
    return len(re.findall(r'class="icon-circle-solid active"', language_star_rating))
def get_drinking_score(html_str):
    soup = get_soup(html_str=html_str)
    drinking_star_rating = str(soup.find('button',{'id': "content-grid-item-drinking-score"}))
    return len(re.findall(r'class="icon-circle-solid active"', drinking_star_rating))
def get_violence_score(html_str):
    soup = get_soup(html_str=html_str)
    violence_star_rating = str(soup.find('button',{'id': "content-grid-item-violence-score"}))
    return len(re.findall(r'class="icon-circle-solid active"', violence_star_rating))
def get_positive_messages_score(html_str):
    soup = get_soup(html_str=html_str)
    positive_messages_star_rating = str(soup.find('button',{'id': "content-grid-item-positive-messages-score"}))
    return len(re.findall(r'class="icon-circle-solid active"', positive_messages_star_rating))
def get_diverse_representations_score(html_str):
    soup = get_soup(html_str=html_str)
    diverse_representations_star_rating = str(soup.find('button',{'id': "content-grid-item-diverse-representations-score"}))
    return len(re.findall(r'class="icon-circle-solid active"', diverse_representations_star_rating))
def get_ease_of_play_score(html_str):
    soup = get_soup(html_str=html_str)
    ease_of_play_star_rating = str(soup.find('button',{'id': "content-grid-item-ease-of-play-score"}))
    return len(re.findall(r'class="icon-circle-solid active"', ease_of_play_star_rating))
def get_consumerism_score(html_str):
    soup = get_soup(html_str=html_str)
    consumerism_star_rating = str(soup.find('button',{'id': "content-grid-item-consumerism-score"}))
    return len(re.findall(r'class="icon-circle-solid active"', consumerism_star_rating))
# %%
import sys
import time

def spinning_cursor():
    while True:
        for cursor in '|/-\\':
            yield cursor


def get_search_results():
    
    res_dict = {}
    apps_dict = get_possible_apps()
    base_link ='https://www.commonsensemedia.org/'
    spinner = spinning_cursor()
    for _ in range(240):
        sys.stdout.write(next(spinner))
        sys.stdout.flush()
        time.sleep(0.1)
        sys.stdout.write('\b')
    for app_key, app_link in apps_dict.items():
        res_dict[app_key] = {
            'sexuality_score':get_sexuality_score(base_link + app_link),
            'language_score': get_language_score(base_link + app_link),
            'drinking_score': get_drinking_score(base_link + app_link),
            'violence_score': get_violence_score(base_link + app_link),
            'positive_messages_score': get_positive_messages_score(base_link + app_link),
            'diverse_representations_score': get_diverse_representations_score(base_link + app_link),
            'ease_of_play_score': get_ease_of_play_score(base_link + app_link),
            'consumerism_score': get_consumerism_score(base_link + app_link)
        }
        print(app_key,get_sexuality_score(base_link + app_link))
    #df = pd.DataFrame(pd.Series(res_dict, index=res_dict.keys())).reset_index().rename(columns={'index':'csm_app_name', 0:'sexuality_score'})
    df = pd.DataFrame(res_dict).T
    print(df)
    df.to_csv('../data/dataframes/{}.csv'.format(APP_NAME))
    return res_dict
#%%
def get_all_app_lists():
    # replace with your folder's path
    folder_path = r'../data/dataframes'

    all_files = os.listdir(folder_path)

    # Filter out non-CSV files
    csv_files = [f for f in all_files if f.endswith('.csv')]

    # Create a list to hold the dataframes
    df_list = []

    for csv in csv_files:
        file_path = os.path.join(folder_path, csv)
        try:
            # Try reading the file using default UTF-8 encoding
            df = pd.read_csv(file_path)
            df_list.append(df)
        except UnicodeDecodeError:
            try:
                # If UTF-8 fails, try reading the file using UTF-16 encoding with tab separator
                df = pd.read_csv(file_path, sep='\t', encoding='utf-16')
                df_list.append(df)
            except Exception as e:
                print(f"Could not read file {csv} because of error: {e}")
        except Exception as e:
            print(f"Could not read file {csv} because of error: {e}")

    # Concatenate all data into one DataFrame
    big_df = pd.concat(df_list, ignore_index=True)
    big_df.to_csv('csm_master_df_' +'.csv')
    return big_df
#%%
if __name__ == '__main__':
    get_search_results()
    get_all_app_lists()
# %%
"""
app rating: done
sexuality rating: done
get meta content where name="description": TODO
"""

