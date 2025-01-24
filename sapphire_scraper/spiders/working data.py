
# import scrapy

#
#
# class SapphireSpider(scrapy.Spider):
#     name = "sapphire"
#     allowed_domains = ["pk.sapphireonline.pk"]
#     start_urls = ["https://pk.sapphireonline.pk/collections/man"]
#
#     def parse(self, response):
#         sections = response.xpath("//ul[@class='cstm-ul-m']/descendant::a/@href").getall()
#         yield from response.follow_all(sections, self.scraper)
#
#     def scraper(self, response):
#         for item in response.xpath("//ul[@class='cstm-ul-m']/descendant::h4"):
#             list = item.xpath("./text()").getall()
#             yield {
#                 "title": list,
#             }





# """ This code is perect for xtracting all mens item data in single go"""
# import scrapy
# class SapphireSpider(scrapy.Spider):
#     name = "sapphire"
#     allowed_domains = ["pk.sapphireonline.pk"]
#     start_urls = [
#         # "https://pk.sapphireonline.pk/collections/man",
#         "https://pk.sapphireonline.pk/collections/man-uns-fall-winter-24/products/usm-2p24v4-16-1"
#     ]
#
#     def parse(self, response):
#
#
#         product_name = response.xpath('//div[@class= "t4s-col-md-5 t4s-col-12 t4s-col-item t4s-product__info-wrapper t4s-pr"]/descendant::h1[@class="t4s-product__title"]/text()').get()
#         product_price = response.xpath('//div[@class= "t4s-col-md-5 t4s-col-12 t4s-col-item t4s-product__info-wrapper t4s-pr"]/descendant::span[@class="money"]/text()').get()
#         details = response.xpath('//section[@id="content1"]').get()
#         product_id = response.xpath('//h3[contains(@class,"t4s-sku-value")]/text()').get()
#         yield {
#             "product_name": product_name,
#             "product_price": product_price,
#             "product_id": product_id,
#             "details": details
#         }
#
#         next = response.xpath('//button[text() = "Next"]/parent::a/@href').get()
#         if next is not None:
#             yield response.follow(next,self.parse)



"""images downloader"""
# img_src = response.xpath('//img[contains(@data-master,"//pk")]/@data-master').get()
# complete_link = response.urljoin(img_src)
#
# yield {
#     # 'title': title,
#     # 'price': price,
#     # 'SKU': SKU,
#     # 'details': details,
#     'img_src': images_downloader(response)






