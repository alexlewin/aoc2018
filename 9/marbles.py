#!/usr/bin/env python


import sys
from collections import defaultdict


#NUM_PLAYERS = 10
#MAX_MARBLE = 7999
NUM_PLAYERS = 9
MAX_MARBLE = 25


class Game(object):
    def __init__(self, num_players, max_marble):
        self.num_players = num_players
        self.next_player = 0
        self.scores = defaultdict(int)
        self.max_marble = max_marble
        self.board = [0]
        self.current_marble_index = 0
        self.next_marble = 1

    def turn(self):
        print('[%s]' % self.next_player, end=' ')
        for i, marble in enumerate(self.board):
            if i == self.current_marble_index:
                print('(%2s)' % marble, end='')
            else:
                print('%4s' % marble, end='')
        print()

        if self.next_marble > self.max_marble:
            self.end()

        if self.next_marble % 23 != 0:
            insert_location = (self.current_marble_index + 2) % len(self.board)
            self.board.insert(insert_location, self.next_marble)
            self.current_marble_index = insert_location
        else:
            self.scores[self.next_player] += self.next_marble
            index7 = (self.current_marble_index - 7) % len(self.board)
            self.scores[self.next_player] += self.board.pop(index7)
            self.current_marble_index = (self.current_marble_index - 7) % len(self.board)

        self.next_marble += 1
        self.next_player = (self.next_player + 1) % self.num_players

    def end(self):
        print('highest score is %s' % max(self.scores.values()))
        sys.exit()
    

game = Game(NUM_PLAYERS, MAX_MARBLE)

while True:
    game.turn()
