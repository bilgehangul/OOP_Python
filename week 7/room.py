#Simple Maze Class
#Mark   
#Drexel University
#CS 172

class Room:
	#Constructor sets the description
	#And all four doors should be initially set to None
	def __init__(self,descr):
		self.descr = descr
		self.east = None
		self.north=	None
		self.south=	None
		self.west = None
		
	#Accessors
	#Return the correct values
	def __str__(self):
		return self.descr
	def getNorth(self):
		return self.north

	def getSouth(self):
		return self.south
	def getEast(self):
		return self.east
	def getWest(self):
		return self.west
		
	#Mutators
	#Update the values
	def setDescription(self,d):
		self.descr = d
	def setNorth(self,n):
		self.north = n
	def setSouth(self,s):
		self.south = s
	def setEast(self,e):
		self.east = e
	def setWest(self,w):
		self.west = w