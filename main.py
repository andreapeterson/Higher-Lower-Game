import os
def clear():  # Cross-platform clear screen
    os.system('cls' if os.name == 'nt' else 'clear')
from art import logo,vs
import random
from game_data import data





def play_game():
  random_1=random.randint(0,49)
  score=0
  should_continue=True
  print(logo)
  while should_continue:
    random_2=random.randint(0,49)
    choice1=data[random_1]
    choice2=data[random_2]
    if choice1==choice2:
      choice2=data[random.randint(0,49)]
    
    print(f"Compare A: {choice1['name']}, a {choice1['description']} from {choice1['country']}")
    print(vs)
    print(f"Compare B: {choice2['name']}, a {choice2['description']} from {choice2['country']}")
    user_input= input("Who has more followers on Instagram? Type 'A' or 'B': ").lower()
    
    if int(choice1['follower_count']) > int(choice2['follower_count']):
      correct_answer="A"
    else:
      correct_answer="B"
      
    if correct_answer=="A":
      if user_input=="a":
        score+=1
        clear()
        print(logo)
        print(f"You're right! Current score: {score}")
      else:
        print(f"Sorry, that's not right. It was {choice1['name']}. Final score = {score}")
        should_continue=False
    if correct_answer=="B":
      if user_input=="b":
        score+=1
        clear()
        print(logo)
        print(f"You're right! Current score: {score}")
      else:
         print(f"Sorry, that's not right. It was {choice2['name']}. Final score = {score}")
         should_continue=False
        
    random_1=random_2
      

play_game()


while input("If you want to play type 'Y', else type 'N': ").lower() == "y":
  clear()
  play_game()
else:
  clear()
  print("Thank you for playing! Come back soon!")