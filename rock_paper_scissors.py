#!/usr/bin/env python3
import random

"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""

moves = ['rock', 'paper', 'scissors']

"""The Player class is the parent class for all of the Players
in this game"""


class Player:
    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        pass



def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


class RandomPlayer(Player):
    def move(self):
        return random.choice(moves)
    
    def count(self):
        self.countp1 = 0
        self.countp2 = 0

class HumanPlayer(Player):
    def move(self):
        return input("")

class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.countp1 = 0
        self.countp2 = 0

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"Player 1: {move1}  Player 2: {move2}")
        if move1 == move2:
            print("*** TIE ***")
            print(self.countp1)
            print(self.countp2)
            # Nobody wins return same count
        elif beats(move1, move2) == True:
            print("*** PLAYER ONE WINS ***")
            # Count p1 +1
            self.countp1 +=1
            print(self.countp1)
            print(self.countp2)
        else:
            print("*** PLAYER TWO WINS ***")
            #Count p2 +1
            self.countp2 +=1
            print(self.countp1)
            print(self.countp2)
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

    def play_game(self):
        print("Let's play some Rock, Paper or Scissors, go!\n"
        "Game start!")
        for round in range(3):
            print(f"Round {round}:")
            self.play_round()
            #print(f"The score is")
        print("Game over!")


if __name__ == '__main__':
    game = Game(RandomPlayer(), RandomPlayer())
    game.play_game()