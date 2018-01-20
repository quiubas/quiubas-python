from base import base

class shortcodes( base ):
	def __init__( self, quiubas ):
		base.__init__( self, quiubas )
		self.base_name		= 'shortcodes'
		self.action_name	= 'shortcode/{id}'

	def getResponses( self, id, params = None ):
		return self.quiubas.network.get( [ self.action_name + '/responses', { 'id': id } ], params )
