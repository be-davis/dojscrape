# DOJ Website Scraper

## Overview
This Python script parses the https://www.justice.gov/news site for links to all releases which are parsed with BeautifulSoup and stored as JSON entities, and combined into a single JSON file. For each Press Release, the following is captured: 
THIS IS ADOPTED AND CHANGED FROM https://github.com/jbencina/dojreleases

1. Press Release Number (Can be missing)
2. Title
3. Contents
4. Publish Date
5. Topics (If any are given)
6. Components (Related agencies / deparments, if any)

This is updated with 2023 data and looks for articles with the tags "child" "sexual" and "abuse"

## Scraper Instructions
1. Ensure `BeautifulSoup` and `requests` libraries are installed
2. Run `scraper.py`
