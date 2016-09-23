from random import randint, uniform
from Player import player

class club() :
    def __init__ (self, name):
        self.budget = 10*randint(1,9)
        self.n_players = 15
        self.players = []
        self.bids = {}
        self.counter_bids = {}
        self.name = name
        self.clubs = []
        self.rewards = {"Sell": 1, "Buy": 1, "Low_players" : -10, "Low_budget" : -5}
        self.states =  {"Low_players": False, "Low_budget" : False}

        for i in range(0,self.n_players):
            p = player()
            self.players.append(p)


    def update_state(self, state, key):
        self.states[key] = state;

    def get_state(self, key):
        return self.states[key];

    def update_rewards(self, reward, key):
        self.rewards[key] = reward

    def get_rewards(self):
        return self.rewards

    def get_reward(self, key):
        return self.rewards[key]

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
        if(len(self.bids) > 0):
            player_club, bid = self.bids.items()[0]
            index = player_club[0]
            club = player_club[1]
            player = club.get_players()[index]

            if (self.n_players < 14):
                print "Can't sell anymore, got too low players"
                self.update_state(True,"Low_players")
                return

            if(bid >= player.get_t_price()):
                club.buy_player(index,bid, self)
                self.sell_player(index,bid)
            else :
                print "Bid is too low"
            #else: #Counter bid
                #self.bids.pop(player,None)
                #return False, player,bid[0] * uniform(1.1,1.3), bid[1]

    def find_weakest_player(self):
        weakest_player = None
        weakest_deff_attack = 99
        for player in self.players:
            stats = player.get_att() + player.get_deff()

            if(stats < weakest_deff_attack):
                weakest_deff_attack = stats
                weakest_player = player

        return weakest_player


    def sell_player(self, index, bid):
        self.players.pop(index)
        self.n_players -= 1
        self.budget += bid
        print self.get_name() + " sold :" + str(bid)

    def buy_player(self,index, bid, club):
        self.players.append(club.get_players()[index])
        self.n_players += 1
        self.budget -= bid
        print self.get_name() + " buyed :" + str(bid)

    def get_counter_bids(self):
        return self.counter_bids

    def set_counter_bids(self, bid, player, club):
        self.counter_bids[player] = [bid, club]
        print self.name + " received bid : " + str(bid) + " from " + club.get_name()

    def get_players(self):
        return self.players

    def get_bids(self):
        return self.bids

    def set_bid(self, index, club, counter):
        bid = club.get_players()[index].get_t_price()
        if counter:
            bid = bid * uniform(1.0,1.5)
        else:
            bid = bid * uniform(0.5,1.5)
        club.get_bids()[index,self] = bid

        if(counter) :
            print self.get_name() + " did counter bid :" + str(bid) + "  to " + club.get_name()
        else :
            print self.get_name() + "  did bid :" + str(bid) + "  to   " + str(club.name)

    def get_name(self):
        return self.name

    def set_clubs(self,clubs):
        self.clubs = clubs

    def get_budget(self):
        return self.budget

    def get_n_players(self):
        return self.n_players

    def get_team_value(self):
        sum = 0
        for player in self.players:
            sum += player.get_t_price()

        return sum

    def start_argument(self, clubs):

        while(True):
            club = clubs[randint(0,len(clubs) - 1)]
            if(club == self):
                continue;

            player_index = randint(0,club.get_n_players() - 1)

            if(club.get_n_players()[player_index].get_t_price() > self.get_budget()):
                self.update_state(True,"Low_budget");
            else:
                self.set_bid(player_index,club, False);
            break;




