from random import randint
from Player import player


class transfer_list():
    def __init__(self):
        self.list_length = 0
        self.transfer_players = []


    def get_best_player(self):
        for t_player in self.transfer_players:

    def show(self):
        for t_player in self.transfer_players:
            print "player price: {} att :{} def :{}".format(t_player.get_t_price(), t_player.get_att(), t_player.get_deff())

    def get_players(self):
        return self.transfer_players

    def get_player(self, index):
        return self.transfer_players[index]