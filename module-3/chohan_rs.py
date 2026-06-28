"""
chohan_rs.py
Author: Rakesh Shrestha
Course: CSD-325 Advanced Python
Assignment: Module 3.2 - Brownfield + Flowchart
Date: June 2026

Description:
    Brownfield modification of the Cho-Han dice game originally written
    by Al Sweigart. In this traditional Japanese dice game, players bet
    whether the total of two dice will be even (CHO) or odd (HAN).

Changes made from the original chohan.py:
    1. Changed the input prompt from '> ' to 'rs: ' to match my initials.
    2. Changed the house fee from 10 percent to 12 percent.
    3. Added a notice in the program introduction that rolls totaling 2 or 7
       earn a 10 mon bonus.
    4. Added logic that announces the 10 mon bonus and adds it to the purse
       when the dice total is 2 or 7.

Original source:
    Al Sweigart, The Big Book of Small Python Projects (Cho-Han game).
"""

import random
import sys


JAPANESE_NUMBERS = {
    1: 'ICHI',
    2: 'NI',
    3: 'SAN',
    4: 'SHI',
    5: 'GO',
    6: 'ROKU'
}


# CHANGE 3: Added the 10 mon bonus notice for rolls totaling 2 or 7.
print('''Cho-Han, by Al Sweigart al@inventwithpython.com

In this traditional Japanese dice game, two dice are rolled in a bamboo
cup by the dealer sitting on the floor. The player must guess if the
dice total is even (CHO) or odd (HAN).

BONUS NOTICE: If the dice total is 2 or 7, you receive a 10 mon bonus!
''')

purse = 5000

while True:  # Main game loop.
    # Place a bet.
    print('You have', purse, 'mon. How much do you bet? (or QUIT)')
    while True:
        # CHANGE 1: Changed the input prompt from '> ' to 'rs: '.
        pot = input('rs: ')
        if pot.upper() == 'QUIT':
            print('Thanks for playing!')
            sys.exit()
        elif not pot.isdecimal():
            print('Please enter a whole number.')
        elif int(pot) > purse:
            print('You do not have enough to make that bet.')
        else:
            # This is a valid bet.
            pot = int(pot)
            break  # Exit the loop once a valid bet is placed.

    # Roll the dice.
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)

    print('The dealer swirls the cup and you hear the rattle of dice.')
    print('The dealer slams the cup on the floor, still covering the')
    print('dice and asks for your bet.')
    print()
    print('    CHO (even) or HAN (odd)?')

    # Let the player choose CHO or HAN.
    while True:
        # CHANGE 1: Changed the input prompt from '> ' to 'rs: '.
        bet = input('rs: ').upper()
        if bet != 'CHO' and bet != 'HAN':
            print('Please enter either "CHO" or "HAN".')
            continue
        break

    # Reveal the dice results.
    print('The dealer lifts the cup to reveal:')
    print('  ', JAPANESE_NUMBERS[dice1], '-', JAPANESE_NUMBERS[dice2])
    print('    ', dice1, '-', dice2)

    # CHANGE 4: Award a bonus when the total of the dice is 2 or 7.
    roll_total = dice1 + dice2
    if roll_total == 2 or roll_total == 7:
        print('The total roll was', roll_total,
              '- Lucky roll! You get a 10 mon bonus!')
        purse = purse + 10

    # Determine whether the player won.
    roll_is_even = roll_total % 2 == 0
    if roll_is_even:
        correct_bet = 'CHO'
    else:
        correct_bet = 'HAN'

    player_won = bet == correct_bet

    # Display the bet results.
    if player_won:
        print('You won! You take', pot, 'mon.')
        purse = purse + pot

        # CHANGE 2: Changed the house fee from 10 percent to 12 percent.
        house_fee = pot * 12 // 100
        print('The house collects a', house_fee, 'mon fee.')
        purse = purse - house_fee
    else:
        purse = purse - pot
        print('You lost!')

    # Check whether the player has run out of money.
    if purse == 0:
        print('You have run out of money!')
        print('Thanks for playing!')
        sys.exit()
