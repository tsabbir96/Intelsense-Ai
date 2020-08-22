import scrapy
import json
class jack_da_scrapper(scrapy.Spider):
    name = "jack"
    start_urls = [
        "https://my.daraz.com.bd/pdp/review/getReviewList?itemId=133166583&pageSize=200&filter=0&sort=0&pageNo=",
        "https://my.daraz.com.bd/pdp/review/getReviewList?itemId=133210201&pageSize=200&filter=0&sort=0&pageNo=",
        "https://my.daraz.com.bd/pdp/review/getReviewList?itemId=131778652&pageSize=200&filter=0&sort=0&pageNo="
    ]

    def write_data(self, raw_data, filename):
        with open(filename, 'w', encoding='utf-8') as file:
            json.dump(raw_data, file, ensure_ascii=False)
        print('Data have saved in JSON format...')

    def parse(self, response):
        all_data  = json.loads(response.body)
        item_data = all_data["model"]["items"]
        review = []

        for item in item_data:
            itemId = item["itemId"]
            itemTitle = item["itemTitle"]
            buyerName = item["buyerName"]
            rating = item["rating"]
            reviewContent = item["reviewContent"]
            replies = item["replies"]
            a_review = {
                "buyerName" :  buyerName,
                "rating" : rating,
                "reviewContent" : reviewContent,
                "replies" : replies,
            }
            review.append(a_review)

        data = {
            "productId": itemId,
            "product_name" : itemTitle,
            "reviews" : review
        }

        filename = "Review_Data/" + str(itemId) + ".json"

        #write review data 
        self.write_data(data,filename)

        