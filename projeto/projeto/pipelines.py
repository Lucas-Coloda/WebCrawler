# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class ProjetoPipeline(object):
    def process_item(self, item, spider):
        if item['titulo']:
            texto = item['titulo'].strip()
            texto = texto.replace('"', '')
            texto = texto.replace("'", '')
            texto = texto.upper()
            item['titulo'] = texto
        if item['titulo']:
            return item


class SaveDataPipeline(object):
    def open_spider(self, spider):
        self.arquivo = open('titulos.txt', 'a')

    def process_item(self, item, spider):
        self.arquivo.write(item['titulo']+'\n') 
        return item

    def close_spider(self, spider):
        self.arquivo.close()
