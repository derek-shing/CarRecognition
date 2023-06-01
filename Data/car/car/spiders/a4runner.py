import scrapy
import base64
import urllib

class A4runnerSpider(scrapy.Spider):
    name = '4runner'
    allowed_domains = ['www.google.com']
    start_urls = ['https://www.google.com/search?q=toyota+Prius&tbm=isch']

    def parse(self, response):
        i=1
        for img in response.xpath('//img[@class="rg_i Q4LuWd"]'):
            src = img.xpath('@data-src').get()
            if (src):
                imagefilename="image"+str(i)+".jpg"
                urllib.request.urlretrieve(src, imagefilename)
                i+=1



            '''
            if src.startswith('data:image/'):
                # Extract the base64-encoded data from the URI
                _, encoded_data = src.split(',', 1)
                # Decode the data and save it to a file
                with open('image.jpg', 'wb') as f:
                    f.write(base64.b64decode(encoded_data))
            else:
                '''
            yield {
                'image_url': src,
            }
