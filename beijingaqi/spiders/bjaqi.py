import scrapy
from beijingaqi.items import BeijingaqiItem
import json
class beijingaqi(scrapy.Spider):
    name='aqi'
    start_urls=['http://www.86pm25.com/city/beijing.html']
    def parse(self,response):
        forcast=response.xpath('//div[@class="aqi-site"][2]/div[2]/font/text()').extract()
        yield {'tomorrow':forcast[0],
               'aftertomorrow':forcast[1]
               }
        data=[]
        rows=response.xpath('//div[@class="weilai"]/table[1]/tr')
        for row in rows:
            #yield {'address':row.xpath('td//text()').extract()[0],
            #       'AQI':row.xpath('td//text()').extract()[1],
             #      'pm24':row.xpath('td//text()').extract()[3],
             #      'pm10':row.xpath('td//text()').extract()[4]
             #   }
             item=BeijingaqiItem()
             item['address']=row.xpath('td//text()').extract()[0]
             item['AQI']=row.xpath('td//text()').extract()[1]
             item['PM25']=row.xpath('td//text()').extract()[3]
             item['PM10']=row.xpath('td//text()').extract()[4]
             data.append(item)
             yield item
        
        from scrapy.mail import MailSender
       
        mailer=MailSender(smtphost="smtp.126.com",
                          mailfrom="your email adress",
                          smtpuser="your email address",
                          smtppass="your smtppassword",
                          smtpport=25)
            #ile=open(r'/home/pi/beijingaqi/aqi.json','r')
        mailer.send(to=['wzdx1024@163.com'],subject='scrapeddata',body=str(data))
 
        


