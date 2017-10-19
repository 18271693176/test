# -*- coding: utf-8 -*-
from scrapy_redis.spiders import RedisSpider


class DangdangSpider(RedisSpider):
    name = 'dangdang'
    allowed_domains = ['dangdang.com']
    # start_urls = ['http://dangdang.com/']
    redis_key = 'dangdang:start_url'

    def parse(self, response):
        div_list = response.xpath("//div[@class='con flq_body']/div")[1:]
        for div in div_list:
            item = {}

