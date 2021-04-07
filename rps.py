n=int(input("How many times do you want to play?"))
while(n>=1):
     n=n-1
     Player1=input("Player 1, Enter rock/paper/scissors: ")
     Player2=input("Player 2, Enter rock/paper/scissors: ")
     if Player1=="rock" and Player2=="paper":
        print("Congratulation!! Player2 wins")

     elif Player1 == "paper" and Player2 == "rock":
        print("Congragulations, Player 2 wins!")
     elif Player1=="rock" and Player2=="scissors":
        print("Congratulaion Player1")
     elif Player1 == "scissors" and Player2 == "rock":
         print ("Congragulations! Player 2 wins")
     elif Player1=="scissors" and Player2=="paper":
         print("Congratulation Player1")
     elif Player1 == "paper" and Player2 == "scissors":
        print ("Congragulation! Player 2 wins!")
     else:
         print("Inavlid Input")
      
      
     