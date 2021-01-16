import random
import time

user_choice = 'yes'

while user_choice == 'yes' or user_choice == 'y':
    print("Dice is Rolling...")
    time.sleep(1)

    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)

    print('Dice1 value is :', dice1)
    print('Dice2 value is :', dice2)
    time.sleep(1)

    if dice1 == dice2:
        print('Congralution!!! You get same value')

    user_choice = input('Do you want to roll dice again? (Y/N):').lower()

print("Thank you!")