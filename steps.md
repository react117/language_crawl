# https://www.youtube.com/watch?time_continue=13&v=O_j3OTXw2_E&t=1904s
# https://towardsdatascience.com/using-scrapy-to-build-your-own-dataset-64ea2d7d4673

1. scrapy shell 'https://fundrazr.com/find?category=Health'

2. response.xpath("//h2[contains(@class, 'title headline-font')]/a[contains(@class, 'campaign-link')]//@href").extract()

3. for href in response.xpath("//h2[contains(@class, 'title headline-font')]/a[contains(@class, 'campaign-link')]//@href"):
	# add the scheme, eg http://
	url  = "https:" + href.extract() 

4. scrapy shell 'https://fundrazr.com/savemyarm'