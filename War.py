#Mike Wenzel
#War
#This program simulates the classic card game War.


import random

def tie(hands, p1, p2, down):   #MAKE THIS WORK FOR A NUMBER OF PLAYERS, NOT JUST 2 BC THERE CAN BE A 3 WAY TIE
    print("TIE")

    print(len(hands[p1]))

    down.append(hands[p1].pop(0))
    down.append(hands[p1].pop(0))
    num1 = down[-1]     # Grabbing the last element of down as deciding card

    down.append(hands[p2].pop(0))
    down.append(hands[p2].pop(0))
    num2 = down[-1]     # Grabbing the last element of down as deciding card

    if num1 > num2:     # Deciding winner
        winner = p1
    elif num2 > num1:
        winner = p2
    else:
        winner = tie(hands, p1, p2, down)   # Recursive call if there is another tie

    return winner

def play(hands):
    down = []
    index = 0
    for i in hands:
        down.append(hands[index].pop(0))    # Placing down a card for each player
        index = index + 1

    player = 0
    max = 0
    for i in range(len(down)):  # Finding max value of placed cards
        if down[i] > max:
            max = down[i]
            player = i
        elif down[i] == max:
            player = tie(hands, player, i, down)

    for i in range(len(down)):      # Giving winner his/her cards
        hands[player].append(down[i])
    print("Player", player, " wins this round")
    print(hands)


def createHands(players):
    hands = [[] for j in range(players)]

    print(hands)

    deck = [2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 9, 10, 10, 10,
            10, 11, 11, 11, 11, 12, 12, 12, 12, 13, 13, 13, 13, 14, 14, 14, 14]
    # 11 = Jack
    # 12 = Queen
    # 13 = King
    # 14 = Ace

    curHand = 0
    for i in range(52):
        randint = random.randint(0, len(deck) - 1)  # Shuffle and hand out cards to players
        hands[curHand].append(deck[randint])
        deck.remove(deck[randint])
        curHand = curHand + 1
        if curHand >= players:
            curHand = 0

    print(hands)

    return hands


if __name__ == '__main__':
    print('How many players?')
    players = input()
    players = int(players)
    hands = createHands(players)

    # test = hands[0].pop(0)
    # print(hands)
    # print(test)
    # hands[0].append(test)
    # print(hands)

    end = False
    while end == False:
        #end = play(hands)
        play(hands)
        play(hands)
        play(hands)
        play(hands)
        play(hands)
        play(hands)
        end = True