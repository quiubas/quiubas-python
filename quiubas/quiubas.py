import re
import urllib
from network import network
from sms import sms
from keywords import keywords
from callback import callback

class Quiubas:
	def __init__( self ):
		self.lib_version		= '1.0.1'
		self.api_key			= None
		self.api_private		= None
		self.base_url			= 'https://rest.quiubas.com'
		self.version			= '1.0'

		self.network = network( self )
		self.sms = sms( self )
		self.keywords = keywords( self )
		self.callback = callback( self )

	def setBaseURL( self, url ):
		self.BASE_URL = url
		return self.BASE_URL

	def getBaseURL( self ):
		return self.BASE_URL

	def setAuth( self, api_key, api_private ):
		self.api_key = api_key
		self.api_private = api_private

	def getAuth( self ):
		return {
			'api_key': self.api_key,
			'api_private': self.api_private
		}

	def format(self, path, vars = None):
		if not vars:
			vars = dict()

		parsed_vars = dict()

		for k in vars:
			if vars[k] is not None:
				parsed_vars['{' + k + '}'] = urllib.urlencode( vars[k] )

		regex = re.compile("(%s)" % "|".join(map(re.escape, parsed_vars.keys())))
		if len(parsed_vars) != 0:
			return regex.sub(lambda mo: str(parsed_vars[mo.string[mo.start():mo.end()]]), path)
		else:
			return path
