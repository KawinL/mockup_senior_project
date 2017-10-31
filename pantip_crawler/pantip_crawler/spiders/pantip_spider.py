import scrapy
# from scrapy.contrib.spiders import CrawlSpider
from scrapy import Spider
from pantip_crawler.items import PantipCrawlerItem
import re
import json

def clean_sentences(sentence):
    sentence = re.sub("(\r|\n|\t)", "", sentence)
    sentence = re.sub(r"(<a.+/a>)", "", sentence)  # <a.+\/a>
    sentence = re.sub(r"(<.+/>)", "", sentence)  # <br /> and <image><image/>
    sentence = re.sub(r"(&.+;)", "", sentence)  # &quot;
    return sentence

##### Post Tag #####
# <div class="display-post-tag-wrapper">
#     <a href="/tag/สูตรอาหาร" target="_blank" class="tag-item">สูตรอาหาร</a>
#     <a href="/tag/ทำอาหาร" target="_blank" class="tag-item">ทำอาหาร</a>
#     <a href="/tag/อาหารเจ" target="_blank" class="tag-item">อาหารเจ</a>
#   </div>
##### Post Datetime #####
# <span class="display-post-timestamp" style="display:block">
# <abbr title="24 ตุลาคม 2560 เวลา  16:48:22 น." data-utime = "10/24/2017 16:48:22"
# class="timeago"></abbr>
##### CommentDatetime #####
# response['data_utime'] = "10/24/2017 16:48:22"



class PantipSpider(Spider):

    name = 'pantip'
    start_urls = ['https://pantip.com/tag/จุฬาลงกรณ์มหาวิทยาลัย']
    request_url = "https://pantip.com/forum/topic/render_comments?tid={}&param=page{}"

    def parse(self, response):
        response_url = response.url
        # print(response_url)
        next_page = response.xpath(
            "//div[@class = 'loadmore-bar indexlist']/a[@rel='next']/@href").extract()[0]
        list_urls = response.xpath(
            "//div[@class='post-item-title']/a/@href").extract()
        for thread_url in list_urls:
            url = "https://pantip.com" + thread_url
            title = response.xpath("//a[@href='{}']/text()".format(thread_url)).extract()[0]
            item = PantipCrawlerItem()
            item['thread_id'] = thread_url.replace("/topic/", "")
            item['url'] = url
            item['title'] = clean_sentences(title)
            request = scrapy.Request(url, callback=self.parse_thread)
            request.meta['item'] = item
            yield request

        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse, meta={'item': item})

    def parse_thread(self, response):
        item = response.meta['item']
        topic = response.xpath("//div[@class = 'display-post-story']//text()").extract()[0]
        item['topic'] = clean_sentences(topic)
        item['tags'] = response.xpath("//div[@class='display-post-tag-wrapper']/a[@class='tag-item']//text()").extract()
        item['datetime'] = response.xpath("//span[@class='display-post-timestamp']/abbr/@data-utime").extract()[0]
        # item['comments'] = []
        item['comments'] = parse_comment(item['url'], item['thread_id'])
        headers = {
            "referer": item['url'],
            "user-agent": """Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko)
                            Chrome/61.0.3163.100 Safari/537.36
                        """,
            "x-requested-with": "XMLHttpRequest"
        }
        yield item
    #     request = scrapy.Request(self.request_url.format(item['thread_id'], 1), callback=self.parse_comment
    #                              , headers=headers, meta={'page': 1})
    #     request.meta['item'] = item
    #     yield request
    #
    # def parse_comment(self, response):
    #     item = response.meta['item']
    #     res = json.loads(response.body_as_unicode())
    #     current_page = response.meta.get('page')
    #     response_page = res['paging']['page']
    #     if current_page > response_page:
    #         yield item
    #     # limit number of comment to avoid large file
    #     limit_size = 10
    #     if len(item['comments']) > limit_size:
    #         yield item
    #
    #     try:
    #         comments = res["comments"]
    #     except KeyError:
    #         pass
    #     else:
    #         for idx, response in enumerate(comments):
    #             try:
    #                 is_del = response["admin_comment_del"]
    #             except KeyError:
    #                 is_del = ""
    #             if not is_del:
    #                 main_comment = response['message']
    #                 date = response['data_utime']
    #                 item['comments'].append({'comment': clean_sentences(main_comment), 'datetime': date})
    #                 for reply in response['replies']:
    #                     item['comments'].append({'comment': clean_sentences(reply['message']),
    #                                              'datetime': reply['data_utime']})
    #     headers = {
    #         "referer": item['url'],
    #         "user-agent": """Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko)
    #                         Chrome/61.0.3163.100 Safari/537.36
    #                     """,
    #         "x-requested-with": "XMLHttpRequest"
    #     }
    #     request = scrapy.Request(self.request_url.format(item['thread_id'], current_page+1), callback=self.parse_comment
    #                              , headers=headers, meta={'page': current_page+1})
    #     request.meta['item'] = item
    #     yield request

from urllib.request import Request, urlopen

def parse_comment(url, thread_id):
    all_comments = []
    headers = {
        "referer": url,
        "user-agent": """Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko)
                        Chrome/61.0.3163.100 Safari/537.36
                    """,
        "x-requested-with": "XMLHttpRequest"
    }
    request_url = "https://pantip.com/forum/topic/render_comments?tid={}&param=page{}"
    current_page = 1
    response_page = 1
    while True:
        req = Request(request_url.format(thread_id, current_page), headers=headers)
        res = urlopen(req)
        response_string = res.read().decode('utf-8')  # Convert bytes to string type and string type to dict
        json_obj = json.loads(response_string)
        response_page = json_obj['paging']['page']
        if response_page < current_page:
            break
        try:
            comments = json_obj["comments"]
        except KeyError:
            pass
        else:
            for idx, response in enumerate(comments):
                try:
                    is_del = response["admin_comment_del"]
                except KeyError:
                    is_del = ""
                if not is_del:
                    main_comment = response['message']
                    all_comments.append(clean_sentences(main_comment))
                    for reply in response['replies']:
                        all_comments.append(clean_sentences(reply['message']))
        current_page += 1
    return all_comments
