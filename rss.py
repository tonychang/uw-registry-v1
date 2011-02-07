#!/usr/bin/env python
# encoding: utf-8
"""
rss.py

Created by Nick Chen on 2011-02-07.
Copyright (c) 2011 __MyCompanyName__. All rights reserved.
"""

import unittest
import feedparser
import datetime
import time

from django.conf import settings
try:
    settings.configure(DEBUG=True, TEMPLATE_DEBUG=True, BLOG_RSS_FEED = 'http://depts.washington.edu/ontheroa/?feed=rss2')
except:
    pass

class RSS(object):
    def __init__(self, feed_url=settings.BLOG_RSS_FEED):
        self.feed_url   = feed_url
        self.feed       = None
    def parse( self ):
        self.feed = feedparser.parse( self.feed_url )
        for entry in self.feed['entries']:
            entry['updated_parsed'] = RSS.time_tuple_to_datetime( entry['updated_parsed'] )

    def entries( self ):
        if self.feed == None:
            self.parse()
        print "HERE"
        try:
            return self.feed['entries']
        except:
            print "failed"
    @staticmethod
    def time_tuple_to_datetime( timetuple ):
        return datetime.datetime.fromtimestamp(time.mktime(timetuple))

class rss(unittest.TestCase):
    def setUp(self):
        pass
    def test_rss( self ):
        r = RSS()
        for entry in r.entries():
            print entry.updated_parsed

    
if __name__ == '__main__':
    unittest.main()