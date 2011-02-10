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
        self.nickname       = nickname
        if service != None:
            if len( service.user_voice_categories.all() ) == 0:
                self.update_service_suggestions( service )
            else:
                self.category_ids = [ uvi.category_id for uvi in service.user_voice_categories.all() ]

    def update_service_suggestions( self, service ):
        category_ids    = self.lookup_category_id( nickname=service.nickname )
        for category_id in category_ids:
            try:
                uvid        = UserVoiceId()
                uvid.category_id = category_id
                uvid.service= service
                uvid.save()
                service.user_voice_categories.add( uvid )
                self.category_ids.append( category_id )
            except:
                pass

    def lookup_category_id( self, nickname=None ):
        response_data = self._request_json( '%sforums/%s/categories.json?client=%s' % ( self.api_url, self.forum_id, self.client_key ) )
        ids = []
        _search_nick = str( nickname ).lower()
        for category in response_data.get('categories', []):
            category_names = filter( lambda val: val.lower(), category.get('name', '').split(',') )
            if _search_nick in category_names:
                ids.append( int( category.get('id') ) )
        return ids

    
    def _request_json( self, request_url, data=None ):
        """
            retrieve json object from request_url and convert it to python object using python json converter.
        """
        response_data = {}
        try:
            query_data = None
            if data != None:
                query_data = urllib.urlencode( data )
                #  use opener for debugging
            opener = urllib2.build_opener(urllib2.HTTPHandler(debuglevel=0))
            req = urllib2.Request( request_url, query_data )
            f   = opener.open(req)
            json_content = f.read()
            response_data = json.loads( json_content )
            f.close()
        except:
            import traceback
            traceback.print_exc(file=sys.stderr)
            raise
        return response_data
        
    def retrieve_data_for_service( self ):
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
                    # ignore case where created_at is missing
                    pass
                try:
                    suggestion['updated_at'] = parse( suggestion.get('updated_at') )
                except:
                    # ignore case where updated_at is missing
                    pass
                self._suggestions.append( suggestion )
        return self._suggestions

    def retrieve_data_for_all( self ):
        """
            retrieve suggestions for our categories
        """
        self._suggestions   = []
        response_data       = self._request_json( '%sforums/%s/suggestions.json?client=%s' % ( self.api_url, self.forum_id, self.client_key ) )
        for suggestion in response_data.get('suggestions', []):
            try:
                    # strptime doesn't handle %z for timezone
                    # 2010/11/22 19:42:27 +0000
                suggestion['created_at'] = parse( suggestion.get('created_at') )
            except:
                # ignore case where created_at is missing
                pass
            try:
                suggestion['updated_at'] = parse( suggestion.get('updated_at') )
            except:
                # ignore case where updated_at is missing
                pass
            self._suggestions.append( suggestion )
        return self._suggestions

    def suggestions( self ):
        if self._suggestions == None:
            if self.nickname != None:
                self.retrieve_data_for_service()
            else:
                self.retrieve_data_for_all()
                # resort, since we can have multiple categories
            self._suggestions = sorted( self._suggestions, key=lambda s: int(s.get('vote_count', 0)), reverse=True)
        return self._suggestions

class user_voice(unittest.TestCase):
    def setUp(self):
        pass
        
    def test_init( self ):
        uservoice = UserVoice( )
        self.assertTrue( len( uservoice.suggestions() ) > 0 )
        self.assertTrue( len( uservoice.lookup_category_id( nickname='sws') ) > 0 )

if __name__ == '__main__':
    unittest.main()
