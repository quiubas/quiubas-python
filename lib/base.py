#!/usr/bin/env python
# -*- coding: utf-8 -*-

from exception import Quiubas_Exception
from network import Network

class base:
	def __init__( self, quiubas ):
		self.network = Network( quiubas )

	def action( self, params = None ):
		return self.network.post( self._BASE_, params )

	def get( self, id ):
		return self.network.get( self._ACTION_, id )

	def delete( self, id ):
		return self.network.delete( self._ACTION_, id )

	def update( self, id, params = None ):
		if params != None:
			return self.network.put( self._ACTION_, id, params )
		else :
			return Quiubas_Exception( 'Updated required params.' )

	def getAll( self ):
		return self.network.get( self._BASE_ )

