# -*- coding: utf-8 -*-
from ..items import LeadthreeItem
from scrapy.utils.python import to_native_str
from six.moves.urllib.parse import urljoin
import scrapy

site_ref = []
with open("/home/dduc-cc/Documents/leadthree/leadthree/leadthree/spiders/sc1", "r") as a_file:

    for row in a_file:
        try:
            site_ref.append(row.strip())
        except:
            pass


class LeadSpider(scrapy.Spider):
    # 'dont_redirect': True,
    name = 'lead'
    start_urls = site_ref

    def parse(self, response):
        items = LeadthreeItem()

        le1 = response.css(
            '#sites_tbl > tbody > tr:nth-child(1) > td.row_name > a::text').extract()
        le2 = response.css(
            '#sites_tbl > tbody > tr:nth-child(3) > td.row_name > a::text').extract()
        le3 = response.css(
            '#sites_tbl > tbody > tr:nth-child(5) > td.row_name > a::text').extract()
        le4 = response.css(
            '#sites_tbl > tbody > tr:nth-child(7) > td.row_name > a::text').extract()
        le5 = response.css(
            '#sites_tbl > tbody > tr:nth-child(9) > td.row_name > a::text').extract()
        le6 = response.css(
            '#sites_tbl > tbody > tr:nth-child(11) > td.row_name > a::text').extract()
        le7 = response.css(
            '#sites_tbl > tbody > tr:nth-child(13) > td.row_name > a::text').extract()
        le8 = response.css(
            '#sites_tbl > tbody > tr:nth-child(15) > td.row_name > a::text').extract()
        le9 = response.css(
            '#sites_tbl > tbody > tr:nth-child(17) > td.row_name > a::text').extract()
        le10 = response.css(
            '#sites_tbl > tbody > tr:nth-child(19) > td.row_name > a::text').extract()
        le11 = response.css(
            '#sites_tbl > tbody > tr:nth-child(21) > td.row_name > a::text').extract()
        le12 = response.css(
            '#sites_tbl > tbody > tr:nth-child(23) > td.row_name > a::text').extract()
        le13 = response.css(
            '#sites_tbl > tbody > tr:nth-child(25) > td.row_name > a::text').extract()
        le14 = response.css(
            '#sites_tbl > tbody > tr:nth-child(27) > td.row_name > a::text').extract()
        le15 = response.css(
            '#sites_tbl > tbody > tr:nth-child(29) > td.row_name > a::text').extract()
        le16 = response.css(
            '#sites_tbl > tbody > tr:nth-child(31) > td.row_name > a::text').extract()
        le17 = response.css(
            '#sites_tbl > tbody > tr:nth-child(33) > td.row_name > a::text').extract()
        le18 = response.css(
            '#sites_tbl > tbody > tr:nth-child(35) > td.row_name > a::text').extract()
        le19 = response.css(
            '#sites_tbl > tbody > tr:nth-child(37) > td.row_name > a::text').extract()
        le20 = response.css(
            '#sites_tbl > tbody > tr:nth-child(39) > td.row_name > a::text').extract()
        le21 = response.css(
            '#sites_tbl > tbody > tr:nth-child(41) > td.row_name > a::text').extract()
        le22 = response.css(
            '#sites_tbl > tbody > tr:nth-child(43) > td.row_name > a::text').extract()
        le23 = response.css(
            '#sites_tbl > tbody > tr:nth-child(45) > td.row_name > a::text').extract()
        le24 = response.css(
            '#sites_tbl > tbody > tr:nth-child(47) > td.row_name > a::text').extract()
        le25 = response.css(
            '#sites_tbl > tbody > tr:nth-child(49) > td.row_name > a::text').extract()
        le26 = response.css(
            '#sites_tbl > tbody > tr:nth-child(51) > td.row_name > a::text').extract()
        le27 = response.css(
            '#sites_tbl > tbody > tr:nth-child(53) > td.row_name > a::text').extract()
        le28 = response.css(
            '#sites_tbl > tbody > tr:nth-child(55) > td.row_name > a::text').extract()
        le29 = response.css(
            '#sites_tbl > tbody > tr:nth-child(57) > td.row_name > a::text').extract()
        le30 = response.css(
            '#sites_tbl > tbody > tr:nth-child(59) > td.row_name > a::text').extract()
        le31 = response.css(
            '#sites_tbl > tbody > tr:nth-child(61) > td.row_name > a::text').extract()
        le32 = response.css(
            '#sites_tbl > tbody > tr:nth-child(63) > td.row_name > a::text').extract()
        le33 = response.css(
            '#sites_tbl > tbody > tr:nth-child(65) > td.row_name > a::text').extract()
        le34 = response.css(
            '#sites_tbl > tbody > tr:nth-child(67) > td.row_name > a::text').extract()
        le35 = response.css(
            '#sites_tbl > tbody > tr:nth-child(69) > td.row_name > a::text').extract()
        le36 = response.css(
            '#sites_tbl > tbody > tr:nth-child(71) > td.row_name > a::text').extract()
        le37 = response.css(
            '#sites_tbl > tbody > tr:nth-child(73) > td.row_name > a::text').extract()
        le38 = response.css(
            '#sites_tbl > tbody > tr:nth-child(75) > td.row_name > a::text').extract()
        le39 = response.css(
            '#sites_tbl > tbody > tr:nth-child(77) > td.row_name > a::text').extract()
        le40 = response.css(
            '#sites_tbl > tbody > tr:nth-child(79) > td.row_name > a::text').extract()
        le41 = response.css(
            '#sites_tbl > tbody > tr:nth-child(81) > td.row_name > a::text').extract()
        le42 = response.css(
            '#sites_tbl > tbody > tr:nth-child(83) > td.row_name > a::text').extract()
        le43 = response.css(
            '#sites_tbl > tbody > tr:nth-child(85) > td.row_name > a::text').extract()
        le44 = response.css(
            '#sites_tbl > tbody > tr:nth-child(87) > td.row_name > a::text').extract()
        le45 = response.css(
            '#sites_tbl > tbody > tr:nth-child(89) > td.row_name > a::text').extract()
        le46 = response.css(
            '#sites_tbl > tbody > tr:nth-child(91) > td.row_name > a::text').extract()
        le47 = response.css(
            '#sites_tbl > tbody > tr:nth-child(93) > td.row_name > a::text').extract()
        le48 = response.css(
            '#sites_tbl > tbody > tr:nth-child(95) > td.row_name > a::text').extract()
        le49 = response.css(
            '#sites_tbl > tbody > tr:nth-child(97) > td.row_name > a::text').extract()
        le50 = response.css(
            '#sites_tbl > tbody > tr:nth-child(99) > td.row_name > a::text').extract()

        items['le1'] = le1
        items['le2'] = le2
        items['le3'] = le3
        items['le4'] = le4
        items['le5'] = le5
        items['le6'] = le6
        items['le7'] = le7
        items['le8'] = le8
        items['le9'] = le9
        items['le10'] = le10
        items['le11'] = le11
        items['le12'] = le12
        items['le13'] = le13
        items['le14'] = le14
        items['le15'] = le15
        items['le16'] = le16
        items['le17'] = le17
        items['le18'] = le18
        items['le19'] = le19
        items['le20'] = le20
        items['le21'] = le21
        items['le22'] = le22
        items['le23'] = le23
        items['le24'] = le24
        items['le25'] = le25
        items['le26'] = le26
        items['le27'] = le27
        items['le28'] = le28
        items['le29'] = le29
        items['le30'] = le30
        items['le31'] = le31
        items['le32'] = le32
        items['le33'] = le33
        items['le34'] = le34
        items['le35'] = le35
        items['le36'] = le36
        items['le37'] = le37
        items['le38'] = le38
        items['le39'] = le39
        items['le40'] = le40
        items['le41'] = le41
        items['le42'] = le42
        items['le43'] = le43
        items['le44'] = le44
        items['le45'] = le45
        items['le46'] = le46
        items['le47'] = le47
        items['le48'] = le48
        items['le49'] = le49
        items['le50'] = le50

        yield items
