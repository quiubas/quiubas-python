#!/usr/bin/env python
# -*- coding: utf-8 -*-

from base import base

class sms(base):
	def __init__( self, quiubas ):
		base.__init__( self, quiubas )
		self._BASE_ = 'sms'
		self._ACTION_ = 'sms/'

	def send( self, params ):
		return self.action( params )

	def getResponses( self, id ):
		return self.network.get( self._ACTION_, [ id, 'responses' ] )