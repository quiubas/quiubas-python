from base import base

class mnp( base ):
	def __init__( self, quiubas ):
		base.__init__( self, quiubas )
		self.base_name		= 'mnp'
		self.action_name	= 'mnp/{number}'

	def getData( self, number, params = None ):
		return self.quiubas.network.get( [ self.action_name, { 'number': number } ], params )

