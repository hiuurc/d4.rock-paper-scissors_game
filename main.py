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

#Write your code below this line 👇
import random
hand = [rock, paper, scissors]

player_choice = int(input("What do you choose? Type 1 for Rock, 2 for Paper or 3 for Scissors."))
computer_choice = random.randint(1,3)

print(hand[player_choice - 1])
print("Computer choose:\n", computer_choice)
print(hand[computer_choice-1])

if player_choice == 1:
  if computer_choice == 2:
    print ("Computer win!")
  elif computer_choice == 3:
    print ("You win!")
  else:
    print ("Draw")
elif player_choice == 2:
  if computer_choice == 1:
    print ("You win!")
  elif computer_choice == 3:
    print ("Computer win!")
  else:
    print ("Draw")
elif player_choice == 3:
  if computer_choice == 1:
    print ("Computer win!")
  elif computer_choice == 2:
    print("You win!")
  else:
    print ("Draw")  






