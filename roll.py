import random
import numpy as np

#Funtion to roll a 5 sided dice,
def rollDice(currentHand):
    # roll dice, Conditions for rolling: can only roll three times, hand cannot be filled
    rollCount = 1
    diceHeld = len(currentHand)
    rollAgain = 'y'
    while rollCount <= 3 and rollAgain != 'n' and diceHeld < 5:
        # update roll counter
        rollCount = rollCount + 1
        # The num of dice to be rolled
        diceRoll = 5 - diceHeld
        # the current roll
        roll = []
        for i in range(diceRoll):
            dice = random.randint(1, 6)
            roll.append(dice)
        roll.sort()
        print("You rolled: ", roll)
        # Ask the player which dice they want to keep
        hold = input("Would you like to keep any of your dice? (y/n) ")
        while hold != "n" and diceHeld < 5:
            keep = int(input("Which dice would you like to keep? "))
            # Create the ability to be able to hold onto certain dice
            roll = np.asarray(roll)
            # Finding where in the array the number chosen to keep is
            place = np.where(roll == keep)[0]
            # The array of just the kept dice
            nums = roll[place]
            # Converting it to a list, so it doesn't look like [array([1,2,3,4,5])]
            l = nums.tolist()
            for i in l:
                currentHand.append(i)
            # np.delete(roll, keep)
            roll = roll.tolist()
            for i in range(len(nums)):
                roll.remove(keep)
            diceHeld = len(currentHand)
            #If player already has 5 dice held leave loop else ask to keep more dice
            if diceHeld == 5:
                break
            else:
                print("Current hand: ", currentHand)
                print("Current roll: ", roll)
                hold = input('Do you want to keep any more dice? (y/n)')

    currentHand.sort()
