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

    
    def parse_qna(self,response):
        all_data  = json.loads(response.body)
        item_data = item_data = all_data["model"]["items"]
        qna_data, itemId = self.get_qnas(item_data)

        filename = "QnA_Data/" + str(itemId) + ".json"

        #write review data 
        self.write_data(qna_data,filename)


    def get_qnas(self,item_data):
        qnas = []

        for item in item_data:
            itemId = item["itemId"]
            customerName = item["customerName"]
            question = item["question"]
            answer = item["answer"]
            a_qna = {
                "customerName" : customerName,
                "question" : question,
                "answer" : answer
            }
            qnas.append(a_qna)

        data_qna = {
            "productId": itemId,
            "qnas" : qnas
        }
        return data_qna, itemId

    
    def get_reviews(self, item_data):
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
        return data, itemId

    
    def parse(self, response):
        all_data  = json.loads(response.body)
        item_data = all_data["model"]["items"]
        
        review_data, itemId = self.get_reviews(item_data)

        filename = "Review_Data/" + str(itemId) + ".json"

        #write review data 
        self.write_data(review_data,filename)

        qna_url = "https://my.daraz.com.bd/pdp/item/getQnAList?mainSeller=%7B%22itemId%22:%22" + str(itemId) + "%22,%22sellerId%22:%221000000%22,%22skuId%22:%221054764369%22%7D&isFromMainSeller=true&pageNo=&pageSize=200"

        return scrapy.Request(qna_url,callback=self.parse_qna)