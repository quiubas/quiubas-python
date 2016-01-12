#!/usr/bin/env python
# -*- coding: utf-8 -*-

from base import base
from sms import sms
from keywords import keywords
from callback import callback
from requests.auth import HTTPBasicAuth

class Quiubas( base ):
	def __init__( self ):
		self.sms = sms( self )
		self.keywords = keywords( self )
		self.callback = callback( self )

	def setBaseURL( self, url ):
		self.BASE_URL = url
		return self.BASE_URL

	def getBaseURL( self ):
		return self.BASE_URL

	def setAuth( self, key, private ):
		self.auth = HTTPBasicAuth( key, private )

	def getAuth( self ):
		return self.auth
