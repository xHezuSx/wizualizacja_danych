# Wymagania wersja Level 4:
# - dodajemy 1 skałę na planszy oznaczone jako R (ang. Rock)
# - jak Player próbuje wejść na pole R to nie pozwalamy mu na to i stoi w miejscu

import numpy as np
import random
class Player:
    def __init__(self, curr_x, curr_y):
        self.curr_x = curr_x
        self.curr_y = curr_y

    def moving(self, board, player_input):
        if player_input == "A":
            if self.curr_x == 0:
                print("invalid value")
            else:
                self.curr_x = self.curr_x-1
        elif player_input == "S":
            if self.curr_y == board.h-1:
                print("invalid value")
            else:
                self.curr_y = self.curr_y+1
        elif player_input == "D":
            if self.curr_x == board.w-1:
                print("invalid value")
            else:
                self.curr_x = self.curr_x+1
        elif player_input == "W":
            if self.curr_y == 0:
                print("invalid value")
            else:
                self.curr_y = self.curr_y-1

class Board:
    def __init__(self, w, h):
        self.w = w
        self.h = h
        self.end_x = w
        self.end_y = h
        self.start_x = None
        self.start_y = None
        self.board = np.full((h, w), ' ', str)

    def setEnd(self, w, h):
        self.end_y = h
        self.end_x = w
        self.board[self.end_y][self.end_x] = "O"

    def setStart(self, w, h):
        self.start_y = h
        self.start_x = w
        self.board[self.start_y][self.start_x] = "P"

    def update_map(self, user):
        self.board[user.curr_y][user.curr_x] = " "

    def new_position(self, user):
        self.board[user.curr_y][user.curr_x] = "P"

    def __str__(self):
        return str(self.board)

while True:
    try:
        n = int(input("ile lvl gramy? "))
        h = int(input("Podaj wysokosc planszy: "))
        w = int(input("Podaj szerokosc planszy: "))
        break
    except:
        print("invalid value")

trials = 0

for i in range(n):
    print("Level: ", i+1)
    w += i
    h += i
    board = Board(w, h)
    start_w = random.randint(0, w-1)
    start_h = random.randint(0, h-1)
    end_w = random.randint(0, w-1)
    end_h = random.randint(0, h-1)

    while start_h == end_h and start_w == end_w:
        start_w = random.randint(0, w - 1)
        start_h = random.randint(0, h - 1)
        end_w = random.randint(0, w - 1)
        end_h = random.randint(0, h - 1)

    board.setEnd(end_w, end_h)
    board.setStart(start_w, start_h)
    andrew = Player(board.start_x, board.start_y)
    while andrew.curr_x != board.end_x or andrew.curr_y != board.end_y:
        print(board)
        sign = input("gdzie idziemy? ")
        board.update_map(andrew)
        andrew.moving(board, sign.upper())
        board.new_position(andrew)
        trials += 1
        print("-----------------")

    print(board)
    print("liczba ruchów: ", str(trials))
    if i < n-1:
        trials = 0
        print("Brawo! Czas na nastepny poziom!")
print("Gratulacje! Gra skonczona")


