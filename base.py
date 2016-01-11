#!/usr/bin/env python
# -*- coding: utf-8 -*-

from exception import Quiubas_Exception
import requests
from requests.auth import HTTPBasicAuth
import json


class base():
	def setBaseURL( self, url ):
		self.BASE_URL = url
		return self.BASE_URL

	def getBaseURL( self ):
		return self.BASE_URL

	def setAuth( self, key, private ):
		self.auth = HTTPBasicAuth( key, private )

	def getAuth( self ):
		return self.auth

	def gets( self, action, params = None, auth = None ):
		try:
			r = requests.get( action + self.get_params_validate( params ), auth=auth )
		except requests.exceptions.RequestException, e:
			raise Quiubas_Exception( 'Invalid URL' )

		return json.loads(r.text)


	def remove( self, action, id, auth = None ):
		try:
			r = requests.delete( action + id, auth=auth )
		except requests.exceptions.RequestException, e:
			raise Quiubas_Exception( 'Invalid URL' )

		return json.loads(r.text)


	def post( self, action, params, auth = None ):
		try:	
			r = requests.post( action, data=self.post_params_validate( params ), auth=auth )
		except requests.exceptions.RequestException, e:
			raise Quiubas_Exception( 'Invalid URL' )

		return json.loads(r.text)


	def put( self, action, id, params, auth = None ):
		try:
			r = requests.put( action + id, data=self.post_params_validate( params ) ,auth=auth )
		except requests.exceptions.RequestException, e:
			raise Quiubas_Exception( 'Invalid URL' )

		return json.loads(r.text)

	def get_params_validate( self, params ):
		if type(params) is list:
			return '/'.join( params )
		elif params is None:
			return ''   
		else:
			return params

	def post_params_validate( self, params ):
		if type( params ) is dict:
			if bool( params ) != False:
				return params
			else:
				raise Quiubas_Exception( 'Params can not be empty' )
		else:
			raise Quiubas_Exception('Parameters must be a dict')
			sys.exit()