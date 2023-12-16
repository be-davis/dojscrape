#%%
from bs4 import BeautifulSoup
import requests
import re
import pandas as pd
import datetime
import os
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
        res_dict[app_key] = get_sexuality_score(base_link + app_link)
        print(app_key,get_sexuality_score(base_link + app_link))
    df = pd.DataFrame(pd.Series(res_dict, index=res_dict.keys())).reset_index().rename(columns={'index':'csm_app_name', 0:'sexuality_score'})
    print(df)
    df.to_csv('dataframes/{}.csv'.format(APP_NAME))
    return res_dict
#%%
def get_all_app_lists():
    # replace with your folder's path
    folder_path = r'dataframes'

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
    big_df.to_csv('csm_master_df_' +NOW+'.csv')
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

