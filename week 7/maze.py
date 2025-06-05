#Mark Boady
#CS 172 - Maze Game
#Drexel University 2018
from room import Room


class Maze:
	#Inputs: Pointer to start room and exit room
	#Sets current to be start room
	def __init__(self,st=None,ex=None):
		self.start = st
		self.exit = ex
		self.current = st
		
	#Return the room the player is in (current)
	def getCurrent(self):
		return self.current

	#The next four all have the same idea
	#See if there is a room in the direction
	#If the direction is None, then it is impossible to go that way
	#in this case return false
	#If the direction is not None, then it is possible to go this way
	#Update current to the new move (move the player)
	#then return true so the main program knows it worked.
	def moveNorth(self):
		if self.current.getNorth() == None:
			return False
		else:
			self.current = self.current.getNorth()
			return True
	def moveSouth(self):
		if self.current.getSouth() == None:
			return False
		else:
			self.current = self.current.getSouth()
			return True
	def moveEast(self):
		if self.current.getEast() == None:
			return False
		else:
			self.current = self.current.getEast()
			return True
	def moveWest(self):
		if self.current.getWest() == None:
			print(self.current.getWest())
			return False
		else:
			self.current = self.current.getWest()
			return True
	#If the current room is the exit,
	#then the player won! return true
	#otherwise return false
	def atExit(self):
		if self.current == self.exit:
			return True
		else:
			return False

	#If you get stuck in the maze, you should be able to go
	#back to the start
	#This sets current to be the start_room
	def reset(self):
		self.current = self.start


