from collections import Counter

"""
Select function: allows players to select points option 
"""

def select(card, hand):
    x = card.keys()
    y = 1
    print("===== Points option's =====")
    for i in card:
        print("Option", y, ":", i)
        y += 1
    option = input("Select points option: ")
    match option:
        case "1":
            p = calOnes(hand)
            inputPoint(card, p, "Ones")
            print("Total point: ", p)
        case "2":
            p = calTwos(hand)
            inputPoint(card, p, "Twos")
            print("Total point: ", p)


        case "3":
            p = calThrees(hand)
            inputPoint(card, p, "Threes")
            print("Total point: ", p)


        case "4":
            p = calFours(hand)
            inputPoint(card, p, "Fours")
            print("Total point: ", p)


        case "5":
            p = calFives(hand)
            inputPoint(card, p, "Fives")
            print("Total point: ", p)


        case "6":
            p = calSixes(hand)
            inputPoint(card, p, "Sixes")
            print("Total point: ", p)


        case "7":
            p = cal3OK(hand)
            inputPoint(card, p, "3 of a Kind")
            print("Total point: ", p)


        case "8":
            p = cal4OK(hand)
            inputPoint(card, p, "4 of a Kind")
            print("Total point: ", p)


        case "9":
            p = calFull(hand)
            inputPoint(card, p, "Full House")
            print("Total point: ", p)


        case "10":
            p = calSmall(hand)
            inputPoint(card, p, "Small Straight")
            print("Total point: ", p)


        case "11":
            p = calLarge(hand)
            inputPoint(card, p, "Large Straight")
            print("Total point: ", p)


        case "12":
            p = calYahtzee(hand)
            inputPoint(card, p, "Yahtzee")
            print("Total point: ", p)


        case "13":
            p = calChance(hand)
            inputPoint(card, p, "Chance")
            print("Total point: ", p)



    return

#Calculate the amount of 1's in a hand
def calOnes(hand):
    print("You picked Ones")
    points = 0
    for i in range(len(hand)):
        if hand[i] == 1:
            points = points + 1
    return points

#Calculate the amount of 2's in a hand
def calTwos(hand):
    print("You picked Twos")
    points = 0
    for i in range(len(hand)):
        if hand[i] == 2:
            points = points + 2
    return points

#Calculate the amount of 3's in a hand
def calThrees(hand):
    print("You picked Threes")
    points = 0
    for i in range(len(hand)):
        if hand[i] == 3:
            points = points + 3
    return points

#Calculate the amount of 4's in a hand
def calFours(hand):
    print("You picked Fours")
    points = 0
    for i in range(len(hand)):
        if hand[i] == 4:
            points = points + 4
    return points

#Calculate the amount of 5's in a hand
def calFives(hand):
    print("You picked Fives")
    points = 0
    for i in range(len(hand)):
        if hand[i] == 5:
            points = points + 5
    return points

#Calculate the amount of 6's in a hand
def calSixes(hand):
    print("You picked Sixes")
    points = 0
    for i in range(len(hand)):
        if hand[i] == 6:
            points = points + 6
    return points

#Calculate if the hand has a 3 of a kind
def cal3OK(hand):
    print("You picked 3 of a Kind")
    # Optimal solution

    count = Counter(hand)
    for points, amount in count.items():
        if amount >= 3:
            return points * 3

    return 0

#Calculate if the hand has a 4 of a kind
def cal4OK(hand):
    print("You picked 4 of a Kind")
    for x in range(len(hand)):
        count = 0
        for y in range(len(hand)):
            if hand[x] == hand[y]:
                count += 1
                if count >= 4:
                    return hand[x] * 4
    return 0

#Calculate if the hand is a full house
def calFull(hand):
    print("You picked Full House")
    newHand = []
    for x in range(len(hand)):
        count3 = 0
        for y in range(len(hand)):
            if hand[x] == hand[y]:
                count3 += 1
                if count3 >= 3:
                    newHand = [value for value in hand if value != hand[x]]
                    if newHand[0] == newHand[1]:
                        return 25
                    else:
                        return 0
    return 0

#Calculate if the hand is a small straight
def calSmall(hand):
    print("You picked Small Straight")
    hand.sort()
    option = hand[0]
    match option:
        case 1:
            count = 1
            for x in range((len(hand) - 1)):
                if hand[x + 1] == (hand[x] + 1):
                    count += 1
            if count >= 4:
                return 30
            else:
                return 0
        case 2:
            count = 1
            for x in range((len(hand) - 1)):
                if hand[x + 1] == (hand[x] + 1):
                    count += 1
            if count >= 4:
                return 30
            else:
                return 0
        case 3:
            count = 1
            for x in range((len(hand) - 1)):
                if hand[x + 1] == (hand[x] + 1):
                    count += 1
            if count >= 4:
                return 30
            else:
                return 0
        case _:
            return 0

#Calculate if the hand is a large straight
def calLarge(hand):
    print("You picked Large Straight")
    hand.sort()
    option = hand[0]
    match option:
        case 1:
            count = 1
            for x in range((len(hand) - 1)):
                if hand[x + 1] == (hand[x] + 1):
                    count += 1
            if count >= 5:
                return 30
            else:
                return 0
        case 2:
            count = 1
            for x in range((len(hand) - 1)):
                if hand[x + 1] == (hand[x] + 1):
                    count += 1
            if count >= 5:
                return 30
            else:
                return 0
        case _:
            return 0

#Calculate if the hand is a yahtzee
def calYahtzee(hand):
    print("You picked Yahtzee")
    option = hand[0]
    count = 0
    for x in range(len(hand)):
        if hand[x] == option:
            count += 1

    if count >= 5:
        return 50
    else:
        return 0

#Calculate the total sum
def calChance(hand):
    print("You picked Chance")
    return sum(hand)

#Input the calculated point into the score card
def inputPoint(scoreCard, points, option):
    scoreCard[option] = points

