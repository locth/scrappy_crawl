# -*- coding: utf-8 -*-
import scrapy
from tut.items import CrawlItem
from scrapy_splash import SplashRequest
import esprima
import urllib.request

VIDEO_XNXX = "https://www.xnxx.com/video-vmyi95d/gorgeous_young_girl_sucks_dick_like_a_pornstar_-_natalissa"

class VideoSpider(scrapy.Spider):

    name = "vid"
    allowed_domains = ['xnxx.com']
    start_urls = [VIDEO_XNXX]

    def start_requests(self):
        for url in self.start_urls:
            yield SplashRequest(url, endpoint="render.html", callback=self.parse,
            args={
                'wait': 0.5,
                'User-Agent':"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.106 Safari/537.36",
            },
            )

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = 'video-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
        jsscript = response.xpath("//script[contains(.,' html5player.setVideoHLS')]").get()
        link = jsscript[jsscript.find("setVideoUrlLow(")+16:jsscript.find("html5player.setVideoUrlHigh")-9]
        print("==== LINK ====")
        print(link)
        urllib.request.urlretrieve(link, 'video-%s.mp4' % page) 
        print("==============")
        self.log('Saved file %s' % filename)

    script = """
        function main(splash)
            splash.plugins_enabled = true
            splash.html5_media_enabled = true
            splash.media_source_enabled = true
        end
    """