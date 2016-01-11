#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Quiubas_Exception( Exception ):
	def __init__(self, arg):
		# Set some exception infomation
		self.msg = arg