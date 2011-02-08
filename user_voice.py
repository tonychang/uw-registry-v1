#!/usr/bin/env python
# encoding: utf-8
"""
user_voice.py

Created by Nick Chen on 2011-02-07.
Copyright (c) 2011 __MyCompanyName__. All rights reserved.
"""

import urllib2
import unittest
import datetime

from django.conf import settings
from dateutil.parser import parse
try:
    import json
except:
    import simplejson as json

class UserVoice(object):
    def __init__( self, form_url=settings.USER_VOICE_FORM_URL, client_key=settings.USER_VOICE_CLIENT_KEY):
        self.form_url       = form_url
        self.client_key     = client_key
        self._suggestions   = None
    def retrieve_data( self ):
        req = urllib2.Request(url=self.form_url + '?client=' + self.client_key )
        f   = urllib2.urlopen(req)
        json_content = f.read()
        response_data = json.loads( json_content )
        self._suggestions = response_data.get('suggestions', [])
        for suggestion in self._suggestions:
            try:
                    # strptime doesn't handle %z for timezone
                    # 2010/11/22 19:42:27 +0000
                suggestion['created_at'] = parse( suggestion.get('created_at') )
            except:
                pass
            try:
                suggestion['updated_at'] = parse( suggestion.get('updated_at') )
            except:
                pass
        f.close()
        
    def suggestions( self ):
        if self._suggestions == None:
            self.retrieve_data()
        return self._suggestions

class user_voice(unittest.TestCase):
    def setUp(self):
        pass
        
    def test_init( self ):
        uservoice = UserVoice()
        for suggestion in uservoice.suggestions():
            print suggestion.get('title'), suggestion.get('vote_count'), suggestion.get('url'), suggestion.get('supporters_count'), suggestion.get('created_at')
if __name__ == '__main__':
    settings.configure(DEBUG=True, TEMPLATE_DEBUG=True, 
        USER_VOICE_CLIENT_KEY='5gfU4ZrAVacZ1HQr39Yjw', 
        USER_VOICE_FORM_URL='http://ontheroa.uservoice.com/api/v1/forums/15200/suggestions.json'
    )
    unittest.main()