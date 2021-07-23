#!/usr/bin/env python3
import random

"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""

moves = ['rock', 'paper', 'scissors']

"""The Player class is the parent class for all of the Players
in this game"""


class Player:
    my_move = None
    their_move = None
    
    def move(self):
        return

    def learn(self, my_move, their_move):
        self.my_move = my_move
        self.their_move = their_move
        

def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))

class HumanPlayer(Player):

    def valid_input(self):
        while True:
            response = input().lower()   
            if response in moves:
                break
            else:
                print("Try again, this is an invalid option.\n")    

    def move(self):
        valid_input(self)
        return

    def count(self):
        self.countp1 = 0

class RandomPlayer(Player):
    def move(self):
        return random.choice(moves)
    
    def count(self):
        self.countp2 = 0

class ReflectPlayer(Player):
    def move(self):
        if self.my_move == None:
            return random.choice(moves)
        else:
            return self.their_move

    def count(self):
        self.countp2 = 0

class CyclePlayer(Player):
    def move(self):
        if self.my_move == None:
            return random.choice(moves)
        if self.my_move == "rock":
            return "paper"
        elif self.my_move == "paper":
            return "scissors"
        else:
            return "rock"

    def count(self):
        self.countp2 = 0

class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.countp1 = 0
        self.countp2 = 0

    def play_round(self):
        # move1 = valid_input(self.p1.move(), moves)
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"Player 1: {move1}  Player 2: {move2}")
        if move1 == move2:
            print("*** TIE ***")
            print(f"Score: Player One: {self.countp1}, Player Two: {self.countp2}\n")
        elif beats(move1, move2) == True:
            print("*** PLAYER ONE WINS ***")
            self.countp1 +=1
            print(f"Score: Player One: {self.countp1}, Player Two: {self.countp2}\n")
        else:
            print("*** PLAYER TWO WINS ***")
            self.countp2 +=1
            print(f"Score: Player One: {self.countp1}, Player Two: {self.countp2}\n")
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

    def play_game(self):
        print("Let's play some Rock, Paper or Scissors, go!\n"
        "Game start!\n")
        for round in range(4):
            # Try to make the first round, round 1 not round 0
            print(f"Round {round}:")
            self.play_round()
        print("Game over!")


# Use this after to play a random player in all we created   
# players = (ReflectPlayer(), RandomPlayer(), CyclePlayer())
# random_players = random.choice(players)


if __name__ == '__main__':
    game = Game(HumanPlayer(), CyclePlayer())
    game.play_game()