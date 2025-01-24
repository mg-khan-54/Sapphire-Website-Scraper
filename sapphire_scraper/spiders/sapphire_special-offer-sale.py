import scrapy

class SapphireSpider(scrapy.Spider):
    name = "sapphire_special-offer-sale"
    allowed_domains = ["pk.sapphireonline.pk"]
    start_urls = [
        # "https://pk.sapphireonline.pk/collections/man",
        "https://pk.sapphireonline.pk/collections/man-uns-fall-winter-24/products/usm-2p24v4-16-1"
    ]

    check = True
    counter = 1
    def parse(self, response):
        while self.check:
            hello = "https://pk.sapphireonline.pk/collections/special-offer-sale?page=" + str(self.counter)
            yield scrapy.Request(url=hello, callback=self.funct)
    def funct(self, response):
        response_check = response.xpath('//h3[@class= "t4s-product-title"]/child::a/text()').get()
        if response_check is not None:
            self.counter += 1
        else:
            self.check = False
        for item in response.xpath('//h3[@class= "t4s-product-title"]'):
            link = item.xpath("./child::a/@href").getall()
            yield from response.follow_all(link, self.scrape)

    def scrape(self, response):
        title = response.xpath('//h1[contains(@class,"t4s-product")]/text()').get()

        actual_price = response.xpath('//div[@class="t4s-product-price"]/descendant::span[@class="money"][1]/text()').get()
        offer_price = response.xpath('//div[@class="t4s-product-price"]/descendant::span[@class="money"][2]/text()').get()
        SKU = response.xpath('//h3[contains(@class,"t4s-sku-value")]/text()').get()
        details = response.xpath('//section[@id="content1"]').getall()
        image_links = []
        link_list = response.xpath('//img[contains(@data-master,"//pk")]/@data-master').getall()

        for links in link_list:
            complete_link = response.urljoin(links)
            image_links.append(complete_link)

        yield {
            'title': title,
            'actual_price': actual_price,
            "offer_price": offer_price,
            'SKU': SKU,
            'details': details,
            # 'image_urls': image_links
        }
