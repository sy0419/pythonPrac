from random import randint

print("Welcome to the game.")

user_choic = int(input("Input random number."))
pc_choic = randint(1, 50)

if user_choic == pc_choic:
    print("You won.")
elif user_choic < pc_choic:
    print("Lower.")
elif user_choic > pc_choic:
    print("Higher.")