class TrackableObject:
	def __init__(self, objectID, centroid):
		#armazene o ID do objeto e inicialize uma lista de centróides
		# usando o centroide atual
		self.objectID = objectID
		self.centroids = [centroid]

		# inicializa um booleano usado para indicar se o objeto tem
		# já foi contado ou não
		self.counted = False