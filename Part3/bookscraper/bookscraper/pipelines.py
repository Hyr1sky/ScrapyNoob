# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

import scrapy
from scrapy.pipelines.images import ImagesPipeline
from scrapy.exceptions import DropItem
from scrapy.utils.project import get_project_settings
import os

class BookscraperPipeline:

    def process_item(self, item, spider):
        adapter = ItemAdapter(item)

        ## Strip all whitespaces from strings
        field_names = adapter.field_names()
        for field_name in field_names:
            if field_name != 'description':
                value = adapter.get(field_name)
                adapter[field_name] = value.strip()

        ## Category & Product Type --> switch to lowercase
        lowercase_keys = ['category', 'product_type']
        for lowercase_key in lowercase_keys:
            value = adapter.get(lowercase_key)
            adapter[lowercase_key] = value.lower()

        ## Price --> convert to float
        price_keys = ['price', 'price_excl_tax', 'price_incl_tax', 'tax']
        for price_key in price_keys:
            value = adapter.get(price_key)
            value = value.replace('£', '')
            adapter[price_key] = float(value)

        ## Availability --> extract number of books in stock
        availability_string = adapter.get('availability')
        split_string_array = availability_string.split('(')
        if len(split_string_array) < 2:
            adapter['availability'] = 0
        else:
            availability_array = split_string_array[1].split(' ')
            adapter['availability'] = int(availability_array[0])

        ## Reviews --> convert string to number
        num_reviews_string = adapter.get('num_reviews')
        adapter['num_reviews'] = int(num_reviews_string)
        
        ## Stars --> convert text to number
        stars_string = adapter.get('stars')
        split_stars_array = stars_string.split(' ')
        stars_text_value = split_stars_array[1].lower()
        if stars_text_value == "zero":
            adapter['stars'] = 0
        elif stars_text_value == "one":
            adapter['stars'] = 1
        elif stars_text_value == "two":
            adapter['stars'] = 2
        elif stars_text_value == "three":
            adapter['stars'] = 3
        elif stars_text_value == "four":
            adapter['stars'] = 4
        elif stars_text_value == "five":
            adapter['stars'] = 5

        return item
    

# class BookImagePipeline(ImagesPipeline):

#     def file_path(self, request, response=None, info=None, *, item=None):
#         # 生成文件名
#         image_guid = request.url.split('/')[-1]
#         return 'full/%s' % (image_guid)

#     def get_media_requests(self, item, info):
#         # 遍历项目项中的图像 URL，并为每个 URL 创建一个下载请求
#         for image_url in item.get('image_urls', []):
#             yield scrapy.Request(image_url, meta={'item': item})

#     def item_completed(self, results, item, info):
#         # 处理下载完成后的结果
#         image_paths = [x['path'] for ok, x in results if ok]
#         if not image_paths:
#             raise DropItem("Image download failed")
#         return item

#     def process_item(self, item, spider):
#         # 在项目项中添加图像保存路径
#         settings = get_project_settings()
#         image_store = settings.get('IMAGES_STORE')
#         image_paths = [x['path'] for ok, x in item.get('image_urls', []) if ok]
#         if image_paths:
#             item['image_paths'] = [os.path.join(image_store, p) for p in image_paths]
#         return item
