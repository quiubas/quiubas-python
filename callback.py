#!/usr/bin/env python
# -*- coding: utf-8 -*-

from base import base

class callback( base ):
	def __init__( self, quiubas ):
		self.quiubas = quiubas
		self.BASE_URL = quiubas.getBaseURL() + 'callback/'

	def get( self ):
		return self.gets( self.BASE_URL, None, self.quiubas.getAuth() )

	def update( self, params ):
		return self.put( self.BASE_URL, '', params, self.quiubas.getAuth() )