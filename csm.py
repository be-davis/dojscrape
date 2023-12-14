#%%
from bs4 import BeautifulSoup
import requests
import re
def get_possible_apps():
    app_name = input('What app are you looking for?  ')
    link = 'https://www.commonsensemedia.org/search/category/app/' + app_name
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
page_data = BeautifulSoup(requests.get('https://www.commonsensemedia.org/app-reviews').content, 'lxml')
page_data.find_all('a',{'href':re.compile('/app-reviews/')})
# %%
import sys
import time

def spinning_cursor():
    while True:
        for cursor in '|/-\\':
            yield cursor


def main():
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
        #print(app_key,get_sexuality_score(base_link + app_link))
    print(res_dict)
    return res_dict
    
if __name__ == '__main__':
    main()

# %%
"""
app rating: done
sexuality rating: done
get meta content where name="description": TODO

"""