#!/usr/bin/env python
# -*- coding: utf-8 -*-

from base import base

class keywords( base ):
	def __init__( self, quiubas ):
		self.quiubas = quiubas
		self.BASE_URL = quiubas.getBaseURL() + 'keywords/'

	def get( self, id ):
		return self.gets( self.BASE_URL, id ,self.quiubas.getAuth() )

	def getAll( self ):
		return self.gets( self.BASE_URL, None, self.quiubas.getAuth() )

	def create( self, params ):
		return self.post( self.BASE_URL, params, self.quiubas.getAuth() )

	def update( self, id, params ):
		return self.put( self.BASE_URL, id, params, self.quiubas.getAuth() )

	def delete( self, id ):
		return self.remove( self.BASE_URL, id, self.quiubas.getAuth() )