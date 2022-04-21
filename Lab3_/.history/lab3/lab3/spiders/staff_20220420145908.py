import scrapy
from lab3.items import FacultyItem, DepartmentItem

class StaffSpider(scrapy.Spider):
    name = "staff"
    BASE_URL = "http://www.univ.kiev.ua"
    start_urls = ["http://www.univ.kiev.ua/ua/departments"]

    def parse(self, response):
        for a in response.css(".b-references__holder li a"):
            url =f"{self.BASE_URL}{a.css('::attr(href)').get()}"
            res = FacultyItem(
                url=url,
                name=a.css("a::text").get()
            )
            yield res
            yield scrapy.Request(
                url=url,
                callback=self.parse_dep,
                meta={
                    "faculty": res["name"]
                }
            )

    def parse_dep(self, response):
        for a in response.css(".b-body__holder ol li a"):
            url =f"{self.BASE_URL}{a.css('::attr(href)').get()}"
            res = DepartmentItem(
                url=url,
                name=a.css("a::text").get(),
                faculty=response.meta["faculty"]
            )
            yield res