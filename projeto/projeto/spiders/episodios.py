# -*- coding: utf-8 -*-
import scrapy


class EpisodiosSpider(scrapy.Spider):
    name = 'episodios'
    allowed_domains = ['https://pt.wikipedia.org/wiki/Lista_de_episódios_de_Breaking_Bad']
    start_urls = ['http://pt.wikipedia.org/wiki/Lista_de_episódios_de_Breaking_Bad']

    def parse(self, response):
        if response.status == 200:
            titulos = response.xpath('//table//td[@class="summary"]//text()').extract()
            for titulo in titulos:
                yield {'titulo':titulo}
        else:
            print("Não 200")

'''
class PrefsctbaSpider(scrapy.Spider):
    name = 'prefsctba'
    allowed_domains = ['http://www.curitiba.pr.gov.br/']
    start_urls = ['http://www.curitiba.pr.gov.br/']

    def parse(self, response):
        for data in response.xpath("//div[@id='divBoxUltimasNoticias']//li"):
            titulo_noticia = data.xpath("a/text()[last()]").extract_first()
            data_noticia = data.xpath("div[@class='quadro']/text()[1]").extract_first()
            hora_noticia = data.xpath("div[@class='quadro']/text()[2]").extract_first()
            link_noticia = data.xpath("a/@href").extract_first()
            noticia = PrefsItem(titulo_noticia=titulo_noticia,data_noticia=data_noticia,hora_noticia=hora_noticia,link_noticia=link_noticia)
            yield noticia
'''