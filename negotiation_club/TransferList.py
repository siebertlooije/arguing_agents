from random import randint
from Player import player


class transfer_list():

    def __init__(self):
        self.list_length = randint(25,50)
        self.transfer_players = []
        for i in range(0,self.list_length):
            p = player()
            self.transfer_players.append(p)

    def show(self):
        for t_player in self.transfer_players:
            print "player price: {} att :{} def :{}".format(t_player.get_t_price(), t_player.get_att(), t_player.get_deff())

