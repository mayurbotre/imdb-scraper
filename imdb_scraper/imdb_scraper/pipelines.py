# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class ImdbScraperPipeline:
    def process_item(self, item, spider):
        return item


# imdb_scraper/pipelines.py

# class MyPipeline:
#     def __init__(self):
#         self.items = []

#     def process_item(self, item, spider):
#         self.items.append(dict(item))
#         return item

#     def get_items(self):
#         return self.items

class MyPipeline:
    def open_spider(self, spider):
        self.items = []

    def close_spider(self, spider):
        for item in self.items:
            print(item)

    def process_item(self, item, spider):
        self.items.append(item)
        return item
