from scraper import DojNewsScraper
from get_doj_analytics import get_all_data
from get_app_danger_analytics import get_app_rankings
def main():
    scraper = DojNewsScraper()
    #scraper.scrape()
    print('scraped')
    get_all_data()
    print('calculated data and stored plots')
    get_app_rankings(source='apple', app_name='Snapchat')
    
if __name__ == '__main__':
    main()