#!/usr/bin/env python
# -*- coding: utf-8 -*-

from base import base
from exception import Quiubas_Exception

class sms(base):
	def __init__( self, quiubas ):
		self.quiubas = quiubas
		self.BASE_URL = quiubas.getBaseURL() + 'sms/'

	def get( self, id = None ):
		if id != None:
			return self.gets( self.BASE_URL, id, self.quiubas.getAuth() )
		else:
			raise Quiubas_Exception( 'ID required' )
	
	def getAll( self ):
		return self.gets( self.BASE_URL, None, self.quiubas.getAuth() )

	def send( self, params ):
		return self.post( self.BASE_URL, params, self.quiubas.getAuth())

	def getResponses( self, id ):
		return self.gets( self.BASE_URL, [ id, 'responses' ], self.quiubas.getAuth() )