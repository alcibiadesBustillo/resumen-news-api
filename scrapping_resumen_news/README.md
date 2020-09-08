# Scraping Resumen News

# News web scrapper
> Scrapping newspaper sites using python.

In this project help us to practice how to make a web scraper to extract information of any website some html elements of it.
In our example we select websites of newspapers identifying the title and body tags.

![](header.png)

## Dependencies
Python 3

## Usage
```shell
python3 -m venv .env
source .env/bin/activate
pip install -r requirements.txt
```
To scrape the newspage site first you must configure the config.yaml file in the [extract]() folder 

```yaml
news_sites:
  newyorktimes:
    url: https://www.nytimes.com/es/
    url2: https://www.nytimes.com
    queries:
      homepage_article_links: 'article h2 a'
      article_body: '#article-summary'
      article_title: 'header div h1'
```

and then run the following command

```sh
python3 pipeline.py
```

## License
[This project is under MIT License](https://opensource.org/licenses/MIT)

