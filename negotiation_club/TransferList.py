from random import randint
from Player import player


class transfer_list():

    def __init__(self):
        self.list_length = randint(25,50)
        self.t_players = []
        for i in range(0,self.list_length):
            p = player()
            self.t_players.append(p)
