#Griffin Georgiadis
#CS21, Assignment 6, part 2
#Make a game where the user plays the computer in a game of 21 with dice
import random

Min=21


def main():
    rollDice()
    rollDice2()
    get_response()





def rollDice():
    value1 = random.randint(1, 6)
    value2 = random.randint(1, 6)
    value_user = value1 + value2
    
    value_total= value_user + value_total
    
def rollDice2():
    valueone = random.randint(1, 6)
    valuetwo = random.randint(1, 6)
    value_comp = valueone + valuetwo
    
    value = value_comp + value
    
    


def get_response():
       user = input("Do you want to roll? ")
       while user == 'y':
           print("Points: ",value_total)
       while user == 'n':
           print("Users Points: ", value_total)
           print("Computers Points: ", value)
       if value > value_total:
            print("Computer Wins")
       else:
            print("User Wins")
           


main()
