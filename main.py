#Rene Walcott-Taylor

import roll
import scorecard

def main():

    print("Welcome to Yahtzee")

    #store the amount of players
    playerNames = []
    playerTags = []

    #Nested dictionary to store all the players score cards
    scoreCards = {}

    playerAmount = int(input("How many players: "))

    #save names of players
    print("Enter name of players")
    for x in range(playerAmount):
        playerNames.append(input(""))
    prefixTag = "Player"
    i = 1
    for x in range(playerAmount):
        playerTags.append(prefixTag+str(i))
        i += 1

    #Add player names and default score cards values
    for x in range(len(playerNames)):
        scoreCards[str(playerNames[x])] = {'Ones': None, 'Twos': None, 'Threes': None, 'Fours': None, 'Fives': None, 'Sixes': None, '3 of a Kind': None, '4 of a Kind': None, 'Full House': None, 'Small Straight': None, 'Large Straight': None, 'Yahtzee': None, 'Chance': None}

    print(scoreCards)
    #print(playerTags)
    play(playerAmount, playerNames, scoreCards)

    #calculate final scores
    totalScores = []
    for x in range(len(playerNames)):
        # The current player
        currentPlayer = playerNames[x]
        totalScore = calScore(scoreCards[currentPlayer])
        totalScores.append(totalScore)
        print(currentPlayer, ': your final score is', totalScore)

    calWinner(totalScores, playerNames)

def play(playerAmount, playerNames, scoreCards):
    rounds = 13
    for x in range(rounds):
        for y in range(playerAmount):
            currentHand = []
            currentPlayer = playerNames[y]
            print(currentPlayer, ": It's your turn ")
            roll.rollDice(currentHand)
            print(currentPlayer, "your hand: ", currentHand)
            print(currentPlayer, ": ", scoreCards[currentPlayer])
            scorecard.select(scoreCards[currentPlayer], currentHand)
            print(currentPlayer, ": ", scoreCards[currentPlayer])


def calScore(scoreCard):
    score = 0
    for x in scoreCard.values():
        #scores.append(scoreCard[x])
        score += int(0 if x is None else x)
    #finalScore = sum(scores)

    #print(finalScore)
    return score

def calWinner(totalScores, playerNames):
    # Finding the maximum score
    max = 0
    for i in range(len(totalScores)):
        if totalScores[i] > max:
            max = totalScores[i]
    # Finding the winner/s
    winners = []
    for k in range(len(totalScores)):
        if totalScores[k] == max:
            winners.append(playerNames[k])

    # Displaying the winner
    # Check if there's a tie
    if len(winners) > 1:
        # Displaying the winner if there are multiple winners
        print('The winners are: ')
        for j in range(len(winners)):
            print(winners[j])
    else:
        # Displaying the winner when there is one winner
        print('The winner is: ', winners[0])


'''
scoreCard = {'Ones': None, 'Twos': None, 'Threes': None, 'Fours': None, 'Fives': None, 'Sixes': None,
              '3 of a Kind': None, '4 of a Kind': None, 'Full House': 25, 'Small Straight': None,
              'Large Straight': None, 'Yahtzee': 50, 'Chance': 25}
'''
main()




