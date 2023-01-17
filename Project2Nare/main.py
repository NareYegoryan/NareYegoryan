from random import randint
from sys import breakpointhook


class Game():
    def __init__(self):
        self.fDice = randint(1, 6)
        self.sDice = randint(1, 6)
        self.goal = 0
        self.start(self.fDice, self.sDice, goal=0)

    def start(self, fDice, sDice, goal=0):
        num = fDice + sDice
        while True:
            if goal == 0:
                if num in [7, 11]:
                    print('You win')
                    break
                elif num in [2, 3, 12]:
                    print('Casino Wins')
                    break
                elif num in [4, 5, 6, 8, 9, 10]:
                    goal = num
                    print(f'Your goal number is {goal}')
                    self.start(fDice=randint(1, 6), sDice=randint(1, 6), goal=goal)
                    break
            else:
                if num == goal:
                    print(f"The sum of dice is {fDice} + {sDice} = {num}")
                    print('You win')
                    break
                elif num == 7:
                    print(f"The sum of dice is {fDice} + {sDice} = {num}")
                    print('Casino Wins')
                    break
                else:
                    print(f"The sum of dice is {fDice} + {sDice} = {num}")
                    self.start(randint(1, 6), randint(1, 6), goal)
                    break


if __name__ == '__main__':
    Game()
