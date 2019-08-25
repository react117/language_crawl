# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class LangCrawlItem(scrapy.Item):
	storyDetails = scrapy.Field()
	storyDate = scrapy.Field()
	storyTitle = scrapy.Field()
	# amountRaised = scrapy.Field()
	# goal = scrapy.Field()
	# currencyType = scrapy.Field()
	# numberContributors = scrapy.Field()
	# url = scrapy.Field()