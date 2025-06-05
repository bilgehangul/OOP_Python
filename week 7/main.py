from room import Room
from maze import Maze

def play(my_maze):
	#Play a game  
	while not my_maze.atExit():
		## TODO: Get direction from user
		print(my_maze.getCurrent())
		direction= input("Enter direction to move north west east south restart")


		## TODO: Based on choice do what was asked.
		if direction=="north":
			if my_maze.moveNorth():
				print("You went north")
			else:
				print("Direction invalid, try again.")
		elif direction=="south":
			if my_maze.moveSouth():
				print("You went south")
			else:
				print("Direction invalid, try again.")
		elif direction=="east":
			if my_maze.moveEast():
				print("You went east")
			else:
				print("Direction invalid, try again.")
		elif direction=="west":
			if my_maze.moveWest():
				print("You went west")
			else:
				print("Direction invalid, try again.")
		elif direction=="restart":
			my_maze.reset()
			print("You went back to the start!")
		else:
			print("Invalid Entry")
		
				
    

    	
	print("You found the exit!")


# **INTERMEDIATE_MAZE** :  This maze should be solved when the movements east and north  are applied in that order. This means you arrive at the exit when you go east room and then the north room. The description of each room doesn't matter since the correctness will be graded. The ORDER matters. 
## TODO: Create the SIMPLE_MAZE
simp_maze = []
simp_maze.append(Room("This room is the entrance."))
simp_maze.append(Room("This room has a table. Maybe a dining room?"))
simp_maze.append(Room("This room is the exit. Good Job."))

#room 1 is north of room 0.  Make sure to connect them both ways (it's not a 1-way door!)
simp_maze[0].setEast(simp_maze[1])
simp_maze[1].setWest(simp_maze[0])

#room 2 is east of room 1.  Make sure to connect them both ways (it's not a 1-way door!)
simp_maze[1].setNorth(simp_maze[2])
simp_maze[2].setSouth(simp_maze[1])
SIMPLE_MAZE = Maze(simp_maze[0],simp_maze[2])

# **INTERMEDIATE_MAZE** :  This maze should be solved when the movements are west, west, west, north, east. This means you arrive at the exit when you go west room, then west room again, then west room again, then take north and then finally the final east room. At the end of the movements, atExit should be true when it is called. The description of each room doesn't matter since the correctness will be graded. 
## TODO: Create the INTERMEDIATE_MAZE
int_maze = []
int_maze.append(Room("Room1"))
int_maze.append(Room("Room2"))
int_maze.append(Room("Room3"))
int_maze.append(Room("Room4"))
int_maze.append(Room("Room5"))
int_maze.append(Room("Room6"))

#room 1 is north of room 0.  Make sure to connect them both ways (it's not a 1-way door!)
int_maze[0].setWest(int_maze[1])
int_maze[0].getWest()
int_maze[1].setEast(int_maze[0])

#room 2 is east of room 1.  Make sure to connect them both ways (it's not a 1-way door!)
int_maze[1].setWest(int_maze[2])
int_maze[2].setEast(int_maze[1])
#room 1 is north of room 0.  Make sure to connect them both ways (it's not a 1-way door!)
int_maze[2].setWest(int_maze[3])
int_maze[3].setEast(int_maze[2])

#room 2 is east of room 1.  Make sure to connect them both ways (it's not a 1-way door!)
int_maze[3].setNorth(int_maze[4])
int_maze[4].setSouth(int_maze[3])
#room 1 is north of room 0.  Make sure to connect them both ways (it's not a 1-way door!)
int_maze[4].setEast(int_maze[5])
int_maze[5].setWest(int_maze[4])


INTERMEDIATE_MAZE = Maze(int_maze[0],int_maze[5])

if __name__=="__main__":
	
	play(INTERMEDIATE_MAZE)