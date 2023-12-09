from scraper import DojNewsScraper
from get_analytics import get_all_data
def main():
    scraper = DojNewsScraper()
    scraper.scrape()
    print('scraped')
    get_all_data()
if __name__ == '__main__':
    main()