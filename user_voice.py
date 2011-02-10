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
from uwregistry.models import UserVoiceId

from dateutil.parser import parse
try:
    import json
except:
    import simplejson as json

class UserVoice(object):
    def __init__( self, nickname=None, service=None, api_url=settings.USER_VOICE_API_URL, client_key=settings.USER_VOICE_CLIENT_KEY, forum_id=settings.USER_VOICE_FORUM_ID):
        self.api_url        = api_url
        self.client_key     = client_key
        self.forum_id       = forum_id
        self._suggestions   = None
        self.category_ids   = []
        if service != None:
            if len( service.user_voice_categories.all() ) == 0:
                category_ids    = self.lookup_category_id( nickname=nickname )
                for category_id in category_ids:
                    uvid        = UserVoiceId()
                    uvid.category_id = category_id
                    uvid.service= service
                    uvid.save()
                    service.user_voice_categories.add( uvid )
                    self.category_ids.append( category_id )
            else:
                for uvid in service.user_voice_categories.all():
                    self.category_ids.append( uvid.category_id )
            

    def lookup_category_id( self, nickname=None ):
        response_data = self._request_json( '%sforums/%s/categories.json?client=%s' % ( self.api_url, self.forum_id, self.client_key ) )
        ids = []
        for category in response_data.get('categories', []):
            category_names = category.get('name', '').split(',')
            if nickname in category_names:
                ids.append( int( category.get('id') ) )
        return ids

    
    def _request_json( self, request_url ):
        """
            retrieve json object from request_url and convert it to python object using python json converter.
        """
        response_data = {}
        try:
            req = urllib2.Request( url=request_url )
            f   = urllib2.urlopen(req)
            json_content = f.read()
            response_data = json.loads( json_content )
            f.close()
        except:
            import traceback
            traceback.print_exc(file=sys.stderr)
        finally:
            return response_data
        
    def retrieve_data( self ):
        """
            retrieve suggestions for our categories
        """
        self._suggestions   = []
        for category_id in self.category_ids:
            response_data       = self._request_json( '%sforums/%s/suggestions.json?client=%s&category=%s' % ( self.api_url, self.forum_id, self.client_key, category_id ) )
            for suggestion in response_data.get('suggestions', []):
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
                self._suggestions.append( suggestion )

    def suggestions( self ):
        if self._suggestions == None:
            self.retrieve_data()
                # resort, since we can have multiple categories
            self._suggestions = sorted( self._suggestions, key=lambda s: int(s.get('vote_count', 0)), reverse=True)
        return self._suggestions

class user_voice(unittest.TestCase):
    def setUp(self):
        pass
        
    def test_init( self ):
        uservoice = UserVoice( )
        print uservoice.lookup_category_id( nickname='sws')
if __name__ == '__main__':
    unittest.main()
