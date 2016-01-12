#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import json
from exception import Quiubas_Exception

class Network:
	def __init__( self, quiubas ):
		self.quiubas = quiubas
		self.version = '1.0'
		self.BASE_URL = 'https://quiubas.dieam.com/api/'+ self.version +'/'

	def get ( self, path, params = None ):
		return self.request( path, None, params, 'GET' )

	def post ( self, path, params = None ):
		return self.request( path, None, params, 'POST' )

	def delete( self, path, id, params = None ):
		return self.request( path, id, params, 'DELETE' )

	def put( self, path, id, params = None ):
		return self.request( path, id, params, 'PUT' )

	def request( self, path, id, params, method ):
		url = self.formatURL( path )
		auth = self.quiubas.getAuth()

		if method == 'GET':
			try:
				r = requests.get( url + self.get_params_validate( params ), auth=auth )
			except requests.exceptions.RequestException, e:
				self.error_connection()
		elif method == 'POST':
			try:	
				r = requests.post( url, data=self.post_params_validate( params ), auth=auth )
			except requests.exceptions.RequestException, e:
				self.error_connection()

		elif method == 'PUT':
			try:
				r = requests.put( url + id, data=self.post_params_validate( params ) ,auth=auth )
			except requests.exceptions.RequestException, e:
				self.error_connection()

		elif method == 'DELETE':
			try:
				r = requests.delete( url + id, data=self.post_params_validate( params ) ,auth=auth )
			except requests.exceptions.RequestException, e:
				self.error_connection()


		return json.loads(r.text)



	def error_connection( self  ):
		raise Quiubas_Exception( 'Invalid URL' )

	def setBaseURL( self, url ):
		self.BASE_URL = url
		return self.BASE_URL

	def getBaseURL( self ):
		return self.BASE_URL

	def formatURL( self, path ):
		return self.getBaseURL()  + path

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
		elif params == None:
			return params
		else:
			raise Quiubas_Exception('Parameters must be a dict')
			sys.exit()