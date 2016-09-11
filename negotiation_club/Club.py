from random import randint
from Player import player

class club() :

    def __init__ (self, name):
        self.budget = 10*randint(1,9)
        self.n_players = 11
        self.players = []
        self.bids = {}
        self.name = name
        self.clubs = []

        for i in range(0,self.n_players):
            p = player()
            self.players.append(p)

    def find_better_players(self, c):
        p = self.find_weakest_player()
        p_stats = p.get_att() + p.get_deff()
        p_possible_players = []

        for p_2 in c.get_players():
            p_2_stats = p_2.get_att() + p_2.get_deff()

            if(p_2_stats> p_stats):
                p_possible_players.append(p_2)

        return p_possible_players


    def sort_player_on_price(self, players):
        players.sort(key=lambda player:player.get_t_price(), reverse=True)
        return players



    def check_bids(self):
        for player,bid in self.bids.iteritems():
            if(bid[0] >= player.get_t_price()):
                return True, player,bid[0],bid[1]

        return False, None,None,None

    def find_weakest_player(self):
        weakest_player = None
        weakest_deff_attack = 99
        for player in self.players:
            stats = player.get_att() + player.get_deff()

            if(stats < weakest_deff_attack):
                weakest_deff_attack = stats
                weakest_player = player

        return weakest_player


    def sell_player(self, player, bid):
        self.players.remove(player)
        self.n_players -= 1
        self.budget += bid
        self.bids.pop(player)

    def buy_player(self,player,bid):
        self.players.append(player)
        self.n_players += 1
        self.budget -= bid

    def get_players(self):
        return self.players

    def get_status(self):
        return self.status

    def set_status(self, status):
        self.status = status

    def get_bids(self):
        return self.bids

    def set_bid(self, player, bid, club):
        self.bids[player] = [bid,club]

    def get_name(self):
        return self.name

    def set_clubs(self,clubs):
        self.clubs = clubs


class top_players_club(club):

    def __init__(self, name):
        club.__init__(self, name)

    def start_argument(self,comp):
        for c_2 in comp:
            if(c_2 == self):
                continue
            c_2_players = self.find_better_players(c_2)
            c_2_players = self.sort_player_on_price(c_2_players)
            i = 0

            while(self.budget>0):
                if(c_2_players[i] < self.budget):
                    c_2.set_bid(c_2_players[i], c_2_players[i].get_t_price(),self)
                    break
                i += 1

            return c_2


class balanced_club(club):
    def __init__(self, name):
        club.__init__(self, name)


    def start_argument(self,comp):
        for c_2 in comp:
            if(c_2 == self):
                continue
            c_2_players = self.find_better_players(c_2)
            c_2_players = self.sort_player_on_price(c_2_players)
            i = len(c_2_players)-1

            while (self.budget > 0):
                if (c_2_players[i] < self.budget):
                    c_2.set_bid(c_2_players[i], c_2_players[i].get_t_price(),self)
                    break
                i -= 1
            return c_2