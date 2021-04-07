p1_call = input("Player 1, Enter rock/paper/scissors: ")
p2_call = input("Player 2, Enter rock/paper/scissors: ")

def rock_paper_scissors(player_1, player_2):
    a_list = ["rock", "paper", "scissors"]

    while player_1 not in a_list or player_2 not in a_list:
        print ("Invalid input. Please give a valid input.")
        player_1 = input("Player 1, Enter rock/paper/scissors: ")
        player_2 = input("Player 2, Enter rock/paper/scissors: ")

    while player_1 == player_2:
        print ("Nobody wins.")
        play=input("Do you want to continue")
        if (play=="yes" or play=="YES"):
            player_1 =input("Player 1, Enter rock/paper/scissors: ")
            player_2 =input("Player 2, Enter rock/paper/scissors: ")
        else :
         break

    if player_1 == "rock" and player_2 == "paper":
        print ("Congragulations! Player 2 wins!")

    elif player_1 == "paper" and player_2 == "rock":
        print ("Congragulations! Player 1 wins!")

    elif player_1 == "rock" and player_2 == "scissors":
        print ("Congragulations! Player 1 wins!")

    elif player_1 == "scissors" and player_2 == "rock":
        print ("Congragulations! Player 2 wins")

    elif player_1 == "paper" and player_2 == "scissors":
        print ("Congragulation! Player 2 wins!")

    elif player_1 == "scissors" and player_2 == "paper":
        print ("Congragulations! Player 1 wins!")

rock_paper_scissors(p1_call, p2_call)





while Player1==Player2:
      print("There is a Tie")
      y=input(print("Do you want to continue  "))
      if y=="yes":

else:
          print("Thank you! Come back again")







Player1=input("Player 1,Enter rock/paper/scissors: ")
Player2=input("Player 2,Enter rock/paper/scissors : ")
list=['rock','paper','scissors']
while  Player1 not in list or Player2 not in list:
       print("Please enter a valid Input")
       Player1=input("Player 1, Enter rock/paper/scissors: ")
       Player2=input("Player 2, Enter rock/paper/scissors: ")