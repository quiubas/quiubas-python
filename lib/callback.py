#!/usr/bin/env python
# -*- coding: utf-8 -*-

from base import base

class callback( base ):
	def __init__( self, quiubas ):
		base.__init__( self, quiubas )
		self._BASE_ = 'callback'
		self._ACTION_ = 'callback/'

	def get( self ):
		return self.getAll()

