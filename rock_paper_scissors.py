#!/usr/bin/env python3
import random


moves = ['rock', 'paper', 'scissors']
raw_number_rounds = list(range(1, 101))
number_rounds = [str(g) for g in raw_number_rounds]
play_again = ["yes", "no"]


def valid_input(message, options):
    while True:
        response = input(message).lower()
        if response in options:
            return response
        else:
            print(f"Try again, '{response}' is an invalid option.\n")


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
    def move(self):
        return valid_input("Rock, paper or scissors? -> ", moves)

    def count(self):
        self.countp1 = 0


class RandomPlayer(Player):
    def move(self):
        return random.choice(moves)

    def count(self):
        self.countp2 = 0


class ReflectPlayer(Player):
    def move(self):
        if self.my_move is not None:
            return self.their_move
        else:
            return random.choice(moves)

    def count(self):
        self.countp2 = 0


class CyclePlayer(Player):
    def move(self):
        if self.my_move is not None:
            if self.my_move == "rock":
                return "paper"
            elif self.my_move == "paper":
                return "scissors"
            else:
                return "rock"
        else:
            return random.choice(moves)

    def count(self):
        self.countp2 = 0


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.countp1 = 0
        self.countp2 = 0

    def number_rounds(self):
        x = valid_input("How many rounds do you want to play?\n"
                        "from 1 to 100 -> ", number_rounds)
        return x

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"Player 1: {move1}  Player 2: {move2}")
        if move1 == move2:
            print("*** TIE ***")
            print(f"Score: Player One: {self.countp1},"
                  f" Player Two: {self.countp2}\n")
        elif beats(move1, move2):
            print("*** PLAYER ONE WINS THE ROUND ***")
            self.countp1 += 1
            print(f"Score: Player One: {self.countp1},"
                  f" Player Two: {self.countp2}\n")
        else:
            print("*** PLAYER TWO WINS THE ROUND ***")
            self.countp2 += 1
            print(f"Score: Player One: {self.countp1},"
                  f" Player Two: {self.countp2}\n")
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

    def get_winner(self, countp1, countp2):
        if countp1 == countp2:
            print("*** IT'S A TIE ***")
            print("*** FINAL SCORE ***")
            print(f"PLYAER ONE: {countp1}, PLAYER TWO: {countp2}")
        elif countp1 > countp2:
            print("*** PLAYER ONE WINS THE GAME ***")
            print("*** FINAL SCORE ***")
            print(f"PLYAER ONE: {countp1}, PLAYER TWO: {countp2}")
        else:
            print("*** PLAYER TWO WINS THE GAME ***")
            print("*** FINAL SCORE ***")
            print(f"PLYAER ONE: {countp1}, PLAYER TWO: {countp2}")

# def play_again(self):
# print("Do you want to play another game?")
# return valid_input("Yes or no? -> ", play_again)

    def play_game(self):
        print("Let's play some Rock, Paper or Scissors, go!\n"
              "Game start!\n")
        x = self.number_rounds()
        for round in range(1, int(x)+1):
            print(f"Round {round}:")
            self.play_round()
        self.get_winner(self.countp1, self.countp2)
        print("Game over!")


players = (ReflectPlayer(), RandomPlayer(), CyclePlayer())
random_players = random.choice(players)

if __name__ == '__main__':
    game = Game(HumanPlayer(), RandomPlayer())
    game.play_game()
