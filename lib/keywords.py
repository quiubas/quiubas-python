#!/usr/bin/env python
# -*- coding: utf-8 -*-

from base import base

class keywords( base ):
	def __init__( self, quiubas ):
		base.__init__( self, quiubas )
		self._BASE_ = 'keywords'
		self._ACTION_ = 'keywords/'

	def create ( self, params ):
		return self.action( params )