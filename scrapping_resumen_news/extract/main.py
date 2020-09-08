import argparse
import logging
import re
logging.basicConfig(level=logging.INFO)

from common import config        # import configuration
logger = logging.getLogger(__name__) 

import news_page_objects as news

from requests.exceptions import HTTPError
from urllib3.exceptions import MaxRetryError

# Regular expressions for check the url 
is_well_formded_link = re.compile(r'^https?://.+/.+$')  # Example: https://example.com/hay
is_root_path = re.compile(r'^/.+$')  # Example: some text

import datetime
import csv

def _news_scraper(news_site_uid):
    print(news_site_uid)
    host_url = config()['news_sites'][news_site_uid]['url']
    host_url2 = config()['news_sites'][news_site_uid]['url2']     

    logger.info(f'\tBegginig scraper for {host_url}')

    # 1. Go to main page and get all the tech link articles
    homepage = news.HomePage(news_site_uid, host_url)
    
    articles = []  # list for save tech articles    
    for link in homepage.article_links:
        #print(link)
        article = _fetch_article(news_site_uid, host_url2, link)
        if article:
            logger.info('Article fetched!')        
            articles.append(article)
    
    _save_article(news_site_uid, articles)

def _save_article(news_site_uid, articles):
    now = datetime.datetime.now().strftime('%y_%m_%d')
    out_file_name = '{}_{}_articles.csv'.format(news_site_uid, now)
    csv_headers = list(filter(lambda property: not property.startswith('_'), dir(articles[0])))
    
    with open(out_file_name, mode='w+') as f:
        writer = csv.writer(f)
        writer.writerow(csv_headers)

        for article in articles:
            row = [str(getattr(article, prop)) for prop in csv_headers]
            print(row)
            writer.writerow(row)

    

def _fetch_article(news_site_uid, host_url, link):
    logger.info("Start fetching article at {}".format(link))

    articles = None
    print(_build_link(host_url, link))
    try:
        article =  news.ArticlePage(news_site_uid, _build_link(host_url, link))
    except (HTTPError, MaxRetryError) as e:
        logger.warning('Error fetching the article', exc_info=False)
    
    if article and not article.body:
        logger.warning('Invalid article. There is no body')
        return None
    
    #print(article.title)
    #print('\n')
    #print(article.body)
    return article
        
    
        

def _build_link(host_url, link):
    if is_well_formded_link.match(link):
        return link
    elif is_root_path.match(link):
        return '{}{}'.format(host_url, link)
    else:
        return '{}/{}'.format(host_url, link)



if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    news_sites_choices = list(config()['news_sites'].keys())
    parser.add_argument(
        'news_sites',
        help='The news sites that you want to scrape the tech section',
        type=str,
        choices=news_sites_choices
    )
    args = parser.parse_args()
    _news_scraper(args.news_sites)

