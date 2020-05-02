"""
ASENCI, ALJOHN
Group06
Code for Project 6 with the class Die and Player
"""


from random import randint

class Die:

    def __init__(self):
        self.value = 1

    def roll(self):
        self.value = randint(1, 6)

    def getValue(self):
        return self.value

    def __str__(self):
        return str(self.getValue())


class Player(object):

    def __init__(self):
        self.die1 = Die()
        self.die2 = Die()
        self.roll = ""
        self.rollsCount = 0
        self.atStartup = True
        self.winner = self.loser = False

    def __str__(self):
        return self.roll

    def getRollsCount(self):
        return self.rollsCount

    def rollDice(self):
        self.rollsCount += 1
        self.die1.roll()
        self.die2.roll()
        (v1, v2) = (self.die1.getValue(),
                    self.die2.getValue())
        self.roll = str((v1, v2)) + " total = " + str(v1 + v2)
        if self.atStartup:
            self.initialSum = v1 + v2
            self.atStartup = False
            if self.initialSum in (2, 3, 12):
                self.loser = True
            elif self.initialSum in (7, 11):
                self.winner = True
        else:
            laterSum = v1 + v2
            if laterSum == 7:
                self.loser = True
            elif laterSum == self.initialSum:
                self.winner = True
        return (v1, v2)


    def isWinner(self):
        return self.winner

    def isLoser(self):
        return self.loser

    def play(self):
        while not self.isWinner() and not self.isLoser():
            self.rollDice()
        return self.isWinner()


def playOneGame():
    player = Player()
    while not player.isWinner() and not player.isLoser():
        player.rollDice()
        print(player)
    if player.isWinner():
        print("You win!")
    else:
        print("You lose!")


def playManyGames(number):
    wins = 0
    losses = 0
    winRolls = 0
    lossRolls = 0
    for count in range(number):
        player = Player()
        hasWon = player.play()
        rolls = player.getRollsCount()
        if hasWon:
            wins += 1
            winRolls += rolls
        else:
            losses += 1
            lossRolls += rolls
    print("The total number of wins is", wins)
    print("The total number of losses is", losses)
    print("The average number of rolls per win is %0.2f" % \
          (winRolls / wins))
    print("The average number of rolls per loss is %0.2f" % \
          (lossRolls / losses))
    print("The winning percentage is %0.3f" % (wins / number))


def main():
    playOneGame()
    number = int(input("Enter the number of games: "))
    playManyGames(number)


if __name__ == "__main__":
    main()
