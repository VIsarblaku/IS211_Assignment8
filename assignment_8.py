# -*- coding: utf-8 -*-

# -*- coding: utf-8 -*-


import random
import time

class Game:
    def __init__(self):
        self.dice = Dice()
        players = Factory()
        self.p1 = players.p1
        self.p2 = players.p2

    def play(self):
        while (self.p1.score < 100 and self.p2.score < 100):
            self.p1.move()
            if self.p1.score < 100:
                self.p2.move()    
        if (self.p1.score > self.p2.score):
            print(f'{self.p1.name} wins!')
        else:
            print(f'{self.p2.name} wins!')


class TimedGameProxy:
    def __init__(self):
        self.dice = Dice()
        players = Factory()
        self.p1 = players.p1
        self.p2 = players.p2

    def play(self):
        starttime = time.time()
        while (self.p1.score < 100 and self.p2.score < 100):
            endtime = time.time()
            if (endtime-starttime)<60:
                self.p1.move()
                if self.p1.score < 100:
                    endtime = time.time()
                    if (endtime-starttime)<60:
                        self.p2.move()
                    else:
                        print("60 Seconds Time over")
                        break
            else:
                 print("60 Seconds Time over")
                 break
        if (self.p1.score > self.p2.score):
            print(f'{self.p1.name} wins!')
        else:
            print(f'{self.p2.name} wins!')

class Player:
    def __init__(self, title):
        self.name = title
        self.score = 0
        self.dice = Dice(6)


    def move(self):
        round_score = 0
        again = 'y'
        # establish a while loop for the player's turn
        while again == 'y':
            self.dice.roll()
            roll = self.dice.value
            if roll == 1:
                print('{} rolled a 1'.format(self.name))
                round_score = 0
                again = 'n'
            else:
                print('{} rolled a {}'.format(self.name, roll))
                round_score = round_score+roll
                print("{}'s round score is {}".format(self.name, round_score))
                again = input('roll again? (y/n)')
        self.score += round_score
        print("{}'s turn is over".format(self.name))
        print("{}'s total score is {}\n\n".format(self.name, self.score))

   

class ComputerPlayer(Player):
    
     def move(self):
        round_score = 0
        again = 'y'
        # establish a while loop for the computer's turn
        while again == 'y':
            self.dice.roll()
            roll = self.dice.value
            if roll == 1:
                print('{} rolled a 1'.format(self.name))
                round_score = 0
                again = 'n'
            else:
                print('{} rolled a {}'.format(self.name, roll))
                round_score = round_score+roll
                if round_score < (25 if 25 < (100 - self.score) else (100-self.score)) :
                    print('{} will roll again'.format(self.name))
                else:
                    again = 'n'
        self.score += round_score
        print('Turn is over')
        print("{}'s round score is {}".format(self.name, round_score))
        print("{}'s total score is {}\n\n".format(self.name, self.score))

  


class Dice:

    def __init__(self, n=6):
        self.sides = n
        self.roll()

    def roll(self):
        self.value = int(random.random()*self.sides+1)


class Factory:
    def __init__(self):
        print("Please select an option:\nSelect 1 for two human players\nSelect 2 for one human and another Computer\nSelect 3 for two Computer player (1/2/3): ")
        try:
            option = int(input())
            while option not in [1,2]:
                   print("Invlaid input")
                   print("Please select an option:\nSelect 1 for two human players\nSelect 2 for one human and another Computer\nSelect 3 for two computer players (1/2/3): ")
                   option = int(input())
            if option == 1:
                    self.p1 =  Player("Player1")
                    self.p2 =  Player("Player2")
            elif option == 2:
                self.p1 =  Player("Player")
                self.p2 =  ComputerPlayer("Computer")
            else:
                self.p1 =  ComputerPlayer("Computer1")
                self.p2 =  ComputerPlayer("Computer2")
        except:
            print("Try again, You have entered a wrong value")



if __name__ == "__main__":
    print('welcome to game of Pig!')
    game = Game()
    game.play()
    print()
    print()
    print('Bye')
