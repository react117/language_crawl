import scrapy
from language_crawl.items import LangCrawlItem
from datetime import datetime
import re


class GlobalLangCrawl(scrapy.Spider):
	name = "my_global_scraper"

	# First Start Url
	start_urls = ["https://fundrazr.com/find?category=Health"]

	npages = 2

	# This mimics getting the pages using the next button. 
	for i in range(2, npages + 2):
		start_urls.append("https://fundrazr.com/find?category=Health&page="+str(i)+"")
	
	def parse(self, response):
		url  = "https://www.anandabazar.com/sport/bwf-world-championships-final-pv-sindhu-vs-nozomi-okuhara-dgtl-1.1036258" 
		yield scrapy.Request(url, callback=self.parse_dir_contents)	
					
	def parse_dir_contents(self, response):
		item = LangCrawlItem()

		# Getting Story Title
		item['storyTitle'] = response.xpath("//div[contains(@id, 'story_container')]/div[contains(@class, 'storypage_cover_story')]/div[contains(@class, 'columns')]/h1/descendant::text()").extract()[0].strip()

		# Story Date
		item['storyDate'] = response.xpath("//div[contains(@id, 'story_container')]//div[contains(@class, 'abp-story-date-div')]/descendant::text()").extract()[0].strip()

		# Getting Story
		story_list = response.xpath("//div[contains(@id, 'story_container')]//div[contains(@class, 'articleBody')]/div[contains(@id, 'textbody')]//p/descendant::text()").extract()
		story_list = [x.strip() for x in story_list if len(x.strip()) > 0]
		item['storyDetails']  = " ".join(story_list)

		yield item

