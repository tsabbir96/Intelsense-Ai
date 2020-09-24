# Daraz-scrapper

1. open cmd and install scrapy using pip
   "pip install scrapy"

2. Go to Daraz Scrapper\daraz_scrapper\daraz_scrapper\spiders\jack_da_scrapper.py

3. Open the file (you have to include the urls you need to scrap)

4. Under "Class jack_da_scrapper" you will find "start_urls". The URLs included are the links that you need to scrap

5. Observe the URL structure : 
   https://my.daraz.com.bd/pdp/review/getReviewList?itemId=133166583&pageSize=200&filter=0&sort=0&pageNo=   
   You need to pass the itemId in the link. 

6. Now go to a product link in daraz you want to scrape. Example:
   "https://www.daraz.com.bd/products/samsung-galaxy-note-20-ultra-69-1440x3088-pixels-108mp-
   camera-12gb-ram-exynos-990-4500-mah-battery-i134710726-s1056614066.html?spm=a2a0e.searchlistcategory.list.3.648f585erDIRQQ&search=1"
   you can get the itemId from this link. The item id is situated between "-i" and "-s" in the link. Now copy the itemId. 
   For this example above, the item id is 134710726
   
7. Now go back to "start_urls" in jack_da_scrapper.py

8. replace the itemId with the newly copied itemId.

9. You can add 10 links by completing the steps above once again. 

10. After adding the links navigate to the folder that has "scrapy.cfg"

11. open cmd -> Write this command:
    scrapy crawl jack
    press Enter
    
12. All the links will be scrapped and stored in the "Review_Data" flolder
   
   
THings daraz crapper wil scrap :
Item Name
buyerName
rating
review content
replies
