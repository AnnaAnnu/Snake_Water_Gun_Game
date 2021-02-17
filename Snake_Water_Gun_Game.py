import random
list = ['Snake', 'Water', 'Gun']

chance = 10
no_of_chances = 0
player1 = 0
player2 = 0

print("Snake, Water, Gun Game \n")
while no_of_chances<chance:
    choose_from = input("Choose option from Snake, Water, Gun:")
    option = random.choice(list)

    if choose_from==option:
        print("TIE, Game Over \n")

    elif choose_from=='Snake' and option=='Gun':
        player1 = player1 + 1
        #use fstring
        print(f"your guess {player2} and robot's guess {player1}")
        print("Player1 wins by 1 point \n")
        print(f"player1's point is {player1} and player2's point is {player2} \n ")


    elif choose_from == "Snake" and option == "Water":
        player2 = player2 + 1
        print(f"your guess {choose_from} and computer guess is {option} \n")
        print("Human wins 1 point \n")
        print(f"computer_point is {player1} and your point is {player2} \n")

        # if user enter water
    elif choose_from == "Water" and option== "Snake":
        player1 = player1 + 1
        print(f"your guess {choose_from} and player1 guess is {option} \n")
        print("player1 wins 1 point \n")
        print(f"player1 is {player1} and your point is {player2} \n ")

    elif choose_from == "Water" and option == "Gun":
        human_point = player2 + 1
        print(f"your guess {choose_from} and amothetr's player guess is {option} \n")
        print("player2 wins by 1 point \n")
        print(f"player1 point is {player1} and your point is {player2} \n")

        # if user enter gun

    elif choose_from == "Gun" and option == "Snake":
        human_point = player2 + 1
        print(f"your guess {choose_from} and another player's guess is {option} \n")
        print("player2 wins 1 point \n")
        print(f"player1 is {player1} and your point is {player2} \n")


    elif choose_from == "Gun" and option == "Water":
        player1 = player1 + 1
        print(f"your guess {choose_from} and player1 guess is {option} \n")
        print("player1 wins 1 point \n")
        print(f"player1 is {player1} and your point is {player2} \n ")

    else:
        print("you have input wrong \n")

    no_of_chances = no_of_chances + 1
    print(f"{chance - no_of_chances} is left out of {chance} \n")

print("Game over")

if player1 == player2:
    print("Tie")

elif player1 > player2:
    print("player1 wins and you loose")

else:
    print("you win and player1 loose")

print(f"your point is {player2} and player1 point is {player1}")

