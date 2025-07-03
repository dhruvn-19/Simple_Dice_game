import random

print("*********")
print("*°*****°*")
print("*°*****°*")
print("*°*****°*")
print("*********")

while True:
    choice = input("Welcome ! , Wanna Play ? , Select Yes or No (y/n) : ").lower()
    if choice == 'y':
        die1 = random.randint(1,6)
        die2 = random.randint(1,6)
        print(f'Your Dice rolled : ({die1} , {die2})\n')
    elif choice == 'n':
        print("Thanks for Playing ! Come Again Later.")
        break
    else :
        print("Invalid Output, Try (y) or (n) to Play !\n")
            