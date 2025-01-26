"""
from random import randint

print("Welcome to the game.")

pc_choice = randint(1, 50)
user_choic = int(input("Input random number."))

if user_choice == pc_choice:
    print("You won.")
elif user_choice > pc_choice:
    print("Lower.")
elif user_choice < pc_choice:
    print("Higher.")
"""


from random import randint

print("Welcome to the game.")
pc_choice = randint(1, 50)

playing = True

while playing:
  user_choice = int(input("Input random number."))
  if user_choice == pc_choice:
      print("You won.")
      playing = False
  elif user_choice > pc_choice:
      print("Lower.")
  elif user_choice < pc_choice:
      print("Higher.")
