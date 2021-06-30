import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
print("Welcome to Rock Papers and Sissors")
userinput = input('Choose between "Rock" , "Paper" and "Scissors"\n').lower()
random_output =random.randint(0,2)
rock1 =  0
paper1 = 1
scissors1 = 2
if userinput == "rock":
  print(f"{rock} \n computer's choice")
  if rock1 == random_output:
    print(f"{rock} \n DRAW")
  elif rock1 + 1 == random_output:
    print(f"{paper} \n LOOSE")
  elif rock1 + 2 == random_output:
    print(f"{scissors} \n WIN" )
elif userinput == "paper":
  print(f"{paper} \n computer's choice")  
  if paper1 == random_output:
    print(f"{paper} \n DRAW")
  elif paper1 - 1 == random_output:
    print(f"{rock} \n WIN")
  elif paper1 + 1 == random_output:
    print(f"{scissors} \n LOOSE" )
elif userinput == "scissors":
  print(f"{scissors} \n computer's choice")
  if scissors1 == random_output:
    print(f"{scissors} \n DRAW")
  elif scissors1 - 1 == random_output:
    print(f"{paper} \n WIN")
  elif scissors1 - 2 == random_output:
    print(f"{rock} \n LOOSE" )
else:
  print("WRONG INPUT")

