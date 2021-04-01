# in this game, I will create a simple black jack game that will give the player a choice to either hit or stop at their number

#import random to use random package to recieve random values
import random

#declare var that holds the values of blackjack
card_values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
#players score tracker
sum = 0

#will be used to determine to add another card 
turn = "hit"




#create loop to start game play
#each condition will determine what the player will be able to do. 
while card_values:
    sum += random.choice(card_values)
    #this condition will determine whether the player wants to stop or not
    #the loop will keep going unless something tells it to stop 
    #in this case, any sum less than 21 will use the following code 
    if sum < 21:
        print("You currently have " + str(sum))
        turn = input("What do you want to do? Type one of the following: (hit or stop)")
    #change the condition for when sum is greater than 21.
    #stop game and tell them they lost
    elif sum > 21:
        print("You went over! You have " + str(sum) + ".")
        break
    #condition to when player gets 21
    #tell user thay got blackjack and stop while loop
    elif sum == 21:
        print("BLACKJACK! You have 21!")
        break
    #if the player chooses to stop the game, it will print out the number they stopped at as well as stopping the loop
    if turn != "hit":
        print("You stopped at " + str(sum))
        break

    