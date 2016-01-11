#!/usr/bin/env python
# -*- coding: utf-8 -*-


from sms import sms
from base import base
from callback import callback
from keywords import keywords

class Quiubas( base ):

	def __init__( self ):
		self.setBaseURL( 'https://quiubas.dieam.com/api/1.0/' )
		self.sms = sms( self )
		self.keywords = keywords( self )
		self.callback = callback( self )

	def setURL( self, url ):
		self.setBaseURL( url )
		self.sms = sms( self )
		self.keywords = keywords( self )

	def balance( self ) :
		return self.gets( self.getBaseURL() + 'balance', None, self.getAuth() )

quiubas = Quiubas()
quiubas.setAuth('be3c6c71e6a95fa97d897dbe464a8b2db2492f43', '48f5f0a2f69ce7f0d0c29510637a540ab0ef7c7d')

print quiubas.callback.update({ 'url': 'http://example.com'})
