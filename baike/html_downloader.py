# -*- coding: UTF-8 -*-
import urllib2

__author__ = 'nidayu'


class HtmlDownloader(object):


    def download(self, url):
        if url is None:
            return None

        response = urllib2.urlopen(url)
        if response.getcode() != 200:
            return None

        return  response.read()