#Mark Boady and Matthew Burlick
#Drexel University 2020
#CS 172


import random
import time

## TODO: import CustomMonster class here 
from monster import CustomMonster

def driver():
	## TODO: Get first monster's name, health, description, basicAttackDamange, specialAttackDamage, defenseDamage, defenseName here.
    name1 = input("Enter monster 1 name:\n")
    health1 = int(input("Enter a number for monster 1 health:\n"))
    description1 = input("Enter monster 1 description:\n")
    basicattackdmg1 = int(input("Enter a number for monster 1 basic attack damage:\n"))
    specattackdmg1 = int(input("Enter a number for monster 1 special attack damage:\n"))
    defdamage1 = int(input("Enter a number for monster 1 defense damage:\n"))
    basicname1 = input("Enter monster 1 basic attack name:\n")
    specname1 = input("Enter monster 1 special attack name:\n")
    defname1= input("Enter monster 1 defense name:\n")
    
    monster1 = CustomMonster(name1, health1,description1,basicattackdmg1,specattackdmg1,defdamage1,basicname1,specname1,defname1)
	
	
    name2 = input("Enter monster 2 name:\n")
    health2 = int(input("Enter a number for monster 2 health:\n"))
    description2 = input("Enter monster 2 description:\n")
    basicattackdmg2 = int(input("Enter a number for monster 2 basic attack damage:\n"))
    specattackdmg2 = int(input("Enter a number for monster 2 special attack damage:\n"))
    defdamage2 = int(input("Enter a number for monster 2 defense damage:\n"))
    basicname2 = input("Enter monster 2 basic attack name:\n")
    specname2 = input("Enter monster 2 special attack name:\n")
    defname2= input("Enter monster 2 defense name:\n")
    
    monster2 = CustomMonster(name2, health2,description2,basicattackdmg2,specattackdmg2,defdamage2,basicname2,specname2,defname2)
	
		
    winner = monster_battle(monster1,monster2)


#This function has two monsters fight and returns the winner
def monster_battle(m1, m2):

	#first reset everyone's health!
	#####TODO######
    m1.resetHealth()
    m2.resetHealth()

	#next print out who is battling
    print("Starting Battle Between")
    print(m1.getName()+": "+m1.getDescription())
    print(m2.getName()+": "+m2.getDescription())
	
    if random.randint(0,1) == 0:
        attacker = m1
        defender = m2
    else:
        attacker = m2
        defender = m1
	#Whose turn is it?
     
	
	#Select Randomly whether m1 or m2 is the initial attacker
	#to other is the initial definder
	######TODO######
	
	
	
    print(attacker.getName()+" goes first.")
	#Loop until either monster is unconscious (health < 1) or choose to stop.
    while( m1.getHealth() > 0 and m2.getHealth() > 0):
        #Ask the user a move among special attack, basic attack, defense or the stop.
        move = input('Pick one of these (s)pecial attack, (b)asic attack, (d)efense or sto(p):')

		#It will be nice for output to record the damage done
        before_health=defender.getHealth()
		
		#for each of the options above, apply the appropriate attack and 
		#print out who did what attack on whom
		#basic attack
        if( move.lower() == "b"):
			# Attacker uses basic attack on defender 
			# and print results by calling print_results function
			######TODO######
            defender.doDamage(attacker.getBasicAttackDamage())
            print_results(attacker,defender,attacker.getBasicName(),attacker.getBasicAttackDamage())
			
		#defense attack
        elif move.lower() == "d":
			# Defend! and print results by calling print_results function
			######TODO######
            attacker.defenseAttack(defender)
            print_results(attacker,defender,attacker.getDefenseName(),attacker.getDefenseAttackDamage())
			
		#special attack
        elif move.lower() == "s":
			# Special Attack! and print results by calling print_results function
			######TODO######
            attacker.specialAttack(defender)
            print_results(attacker,defender,attacker.getSpecialName(),attacker.getSpecialAttackDamage())
			
        elif move.lower() == 'p':
            break
		
		
		#Print the names and healths after this round
		######TODO######
        print(attacker.getName(),"at",attacker.getHealth())
        print(defender.getName(),"at",defender.getHealth())
		
		#Swap attacker and defender
		######TODO######
		
        swap = attacker
        attacker = defender
        defender = swap
		
	
		
            
    print("\nBattle is over. let's see who has won...")
	
    if attacker.getHealth() > defender.getHealth():
        print(attacker.getName(),"is victorious!")
        return attacker
    else:
        print(defender.getName(),"is victorious!")
        return defender
	# Print out who won.
    # Return who won
	


#Print status updates
####TODO####
def print_results(attacker,defender,attack,hchange):
	####TODO####
	# Get the name of the attacker and the defender.
	# then give status updates based on the the attack. For more
	# info refer to the example trace.
	
    res= attacker.getName()+" "+"used"+" "+attack+" "+"on"+" "+defender.getName()
    print(res)
    print("The attack did %d damage."%(hchange))

#----------------------------------------------------
if __name__=="__main__":
	#Ideally ever battle will be different
	#But for reproducability, we'll seed the random number generator as 0
	
    random.seed(0)
    driver()