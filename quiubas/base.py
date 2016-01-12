

class base:
	def __init__( self, quiubas ):
		self.quiubas = quiubas;

	def action( self, params = None ):
		return self.quiubas.network.post( self.base_name, params )

	def get( self, id = None, params = None ):
		return self.quiubas.network.get( [ self.action_name, { 'id': id } ], params )

	def delete( self, id = None, params = None ):
		return self.quiubas.network.delete( [ self.action_name, { 'id': id } ], params )

	def update( self, id = None, params = None ):
		return self.quiubas.network.put( [ self.action_name, { 'id': id } ], params )

	def getAll( self, params ):
		return self.quiubas.network.get( self.base_name, params )
