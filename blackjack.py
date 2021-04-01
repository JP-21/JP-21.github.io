import random #This will give the user the ability to choose a random number from a variable
#declare var to assign card values in a simple black jack game.
card_values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
#the way we stop the application is through setting the while loop to false. 
#declare a variable to keep track the sum of what the players have
sum = 0
#using this variable to store the value of of whether the user wants to keep going 
turn = "hit"
#start while loop to loop through the list assigned in card_values 


while card_values:
    #This will add the value of sum and a random number from the list containing the blackjack values 
    sum += random.choice(card_values)
    print("You currently have " + str(sum))
    
    #declaring condition for when the player has a number less the 21
    if sum < 21:
        turn = input("What do you want to do? (hit or stop)")
    #setting condition if the number goes over 21 than print LOSER!
    elif sum > 21:
        print("You went over! GAME OVER! You ended at " + str(sum) + ".")
        break
    elif sum == 21:
        print("BLACK JACK! You got " + str(sum) + "!")
        break
    if turn == "stop":
        print("You stopped at " + str(sum))
        break


