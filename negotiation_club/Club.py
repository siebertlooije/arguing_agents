from random import randint, uniform
from Player import player
from Graph_visualizer import graph_visualizer
from Competition import competition

class club() :
    def __init__ (self, name):
        self.budget = 10*randint(1,9)
        self.n_players = 15
        self.players = []
        self.bids = {}
        self.counter_bids = {}
        self.name = name
        self.clubs = []
        self.previous_reward = 0;

        for i in range(0,self.n_players):
            p = player()
            self.players.append(p)

    def set_previous_reward(self,prev_reward):
        self.previous_reward += prev_reward;

    def get_previous_reward(self):
        return self.previous_reward;

    def remove_all_players(self):
        self.players = [];

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


    def find_best_player(self):
        return self.sort_player_on_price(self.players)[0]

    def find_better_players(self, c):
        while(c.find_best_player().get_stats() > self.find_weakest_player().get_stats() and c.find_best_player() not in self.players) :
            self.players.remove(self.find_weakest_player())
            self.players.append(c.find_best_player())


    def sort_player_on_price(self, players):
        players.sort(key=lambda player:player.get_t_price(), reverse=True)
        return players

    def check_bids(self, comp):
        if(len(self.bids) > 0):
            player_club, bid = self.bids.items()[0]
            index = player_club[0]
            club = player_club[1]
            player = self.get_players()[index]

            if (self.n_players < 14):
                print "{} :Can't sell anymore, got too low players".format(club.get_name())
                comp.visualizer.format_arguments(self,club,player,"Have too few players", 'red')
                comp.visualizer.remove_arguments(club,self,player,"Bid")
                return

            if(bid >= player.get_t_price()):
                club.buy_player(index,bid, self)
                self.sell_player(index,bid)
                comp.visualizer.format_arguments(self,club,player,"Sell" ,'green')
            else :
                print "{} : Bid of {} is too low".format(self.get_name(),club.get_name())
                comp.visualizer.format_arguments(self,club,player,"Bid too low", 'red')
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

        print self.get_name() + " sold player "+ self.players[index].get_name() + " with price:" + str(bid)
        self.players.pop(index)
        self.n_players -= 1
        self.budget += bid

    def buy_player(self,index, bid, club):
        self.players.append(club.get_players()[index])
        self.n_players += 1
        self.budget -= bid
        print self.get_name() + " buyed player with price :" + str(bid)

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


    def player_index(self, player2):
        for index,player in enumerate(self.players):
            if player2 == player:
                return index

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

    def get_team_attributes(self):
        sum = 0
        for player in self.players:
            sum += player.get_stats()
        return sum


    def calculate_reward(self, player):
        n_players = len(self.get_players())

        alpha = float(player.get_stats() - self.get_team_attributes()/n_players)
        return (0.9*alpha + 0.1*1) if player.get_t_price() < self.budget else -50

    def start_argument(self, comp):
        clubs = comp.get_clubs()
        counter = 0;
        while(True):
            club = clubs[randint(0,len(clubs) - 1)]

            if(club == self):
                continue;

            weakest_player = self.find_weakest_player()
            comp.visualizer.format_argument(self,weakest_player,"Weakest player", "yellow")
            player = club.find_best_player()
            if (player.get_stats() <= weakest_player.get_stats()):
                print "Player : {} is not better then weakest player :{}".format(player.get_name(),weakest_player.get_name())
                return;

            transfer_player =

#            player_index = randint(0,club.get_n_players() - 1)
            #player = club.get_players()[player_index]
            player_index = club.player_index(player)

            if(player.get_t_price() < self.get_budget()):
                self.set_bid(player_index,club, False);
                comp.visualizer.format_arguments(self,club, club.get_players()[player_index], "Bid" , 'green')
                break;
            else :
                print " {} : Not have enough money to buy player of price :{}".format(self.get_name(),player.get_t_price())
                counter += 1
                if (counter == 5):
                    break;

                continue;

