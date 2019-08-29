### Synopsis

This custom routine scrapes a single link. I have scrapped story title, story date, and the main story from https://www.anandabazar.com/sport/bwf-world-championships-final-pv-sindhu-vs-nozomi-okuhara-dgtl-1.1036258. Right now in order to scrap urls with this tool, user need to have a bit of scripting knowledge, because you need to identify the story title body segments
. Will try to make the tool more flexible and human intervension should be as less as possible.

### How to replicate my result

1. Install Scrapy. https://docs.scrapy.org/en/latest/intro/install.html

2. Clone the repo.

3. The file you are looking for is `global_scrape.py` inside `language_crawl/language_crawl/spiders/`. Please go through the file. It should be straight forward.

4. You can see my scrapped result data in `abp_scrap.csv`.

5. To replicate my results, please open your terminal, go to the `language_crawl/language_crawl` directory and run `scrapy crawl my_global_scraper -o abp_scrap.csv`. But before that please go through the article once.

### Referance
* https://www.youtube.com/watch?time_continue=13&v=O_j3OTXw2_E&t=1904s
* https://towardsdatascience.com/using-scrapy-to-build-your-own-dataset-64ea2d7d4673
