import scrapy
class wikipediaSpider(scrapy.Spider):
    name = "wikispider"
    start_urls = [
        'https://en.wikipedia.org/wiki/Information_retrieval'
    ]

# function to parse
    def parse(self,response):
        page = response.url.split('/')[-1]
        filename = 'webdoc-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)

        sel = scrapy.Selector(response)
        see_all_links = sel.xpath("//div[@class='div-col columns column-width']/ul/li/a/@href").extract()

        for link in see_all_links:
            if link is not None:
                link = response.urljoin(link)
                yield scrapy.Request(link,callback=self.parse)


