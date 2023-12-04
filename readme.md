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

As of 2018-07-28, this script has downloaded **13,087** Press Releases while the DOJ website lists **13,129**. The difference comes from some pages which exist, but do not contain any links. For example, at the time of scrape, page 311 did not contain any links, but there were links on page 310 and 312. The data spans through **January 5th, 2009**.

## Dataset
You can simply query the dataset from **BigQuery** at https://bigquery.cloud.google.com/table/jbencina-144002:doj.press_releases or download from Kaggle at https://www.kaggle.com/jbencina/department-of-justice-20092018-press-releases

You could also run the scraper, however there is a 1.5 second delay between scrape requests. That means (1.5 sec x 599 links) + (1.5 sec x 13,087 releases) = at least 5 hours, 42 minutes.

Below is an example BQ query which flattens the topics and components since they are stored as string arrays.

*Query all records*
```
#standardSQL
SELECT 
  id, 
  title, 
  contents,
  date,
  ARRAY_TO_STRING(topics,",") topics,
  ARRAY_TO_STRING(components,",") components
FROM 
  `jbencina-144002.doj.press_releases` 
```

## Contents
`scraper.py` - Main file to run which will scrape and download content

`definitions.py` - Cleaner way to store the BeautifulSoup attributes

`Example Query.ipynb` - Shows example of how to query BQ from Pandas

`Keras Classifier Model.ipynb` - Shows example of RNN model with detail here https://medium.com/jbencina/scraping-text-data-into-bigquery-and-building-a-keras-rnn-classifier-model-from-doj-press-releases-7899e520a1cf

## Scraper Instructions
1. Ensure `BeautifulSoup` and `requests` libraries are installed
2. Run `scraper.py`
