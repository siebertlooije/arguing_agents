from Club import club;

class balanced_club(club):
    def __init__(self, name):
        club.__init__(self, name)


    def start_argument(self, clubs):
        best_player = None;
        value_best_player = 0;
        best_club = None;
        for c_2 in clubs:
            if(c_2 == self):
                continue
            c_2_players = self.find_better_players(c_2)
            c_2_players = self.sort_player_on_price(c_2_players)

            if(len(c_2_players)==0):
                continue;

            i = len(c_2_players) - 1

            while (i != 0):
                if (c_2_players[i].get_t_price() < self.budget and c_2_players[i].get_t_price() > value_best_player):
                    best_player = c_2_players[i]
                    value_best_player = c_2_players[i].get_t_price()
                    best_club = c_2;
                    break;
                i -= 1
        if(best_player != None):
            self.set_bid(best_player, value_best_player, best_club, False)

    def counter_argument(self, clubs):
        if(len(self.get_counter_bids()) == 0):
            return

        item = self.get_counter_bids().items()[0]

        player = item[0]
        bid = item[1][0]
        club = item[1][1]

        best_player = None
        value_best_player = 0
        best_club = None
        for c_2 in clubs:
            if (c_2 == self):
                continue
            c_2_players = self.find_better_players(c_2)
            c_2_players = self.sort_player_on_price(c_2_players)

            if (len(c_2_players) == 0):
                continue;

            i = len(c_2_players) - 1
            while (i !=0 ):
                if c_2_players[i].get_sum_all_attribute() >= player.get_sum_all_attribute() and c_2_players[i].get_t_price() < bid:
                    if (c_2_players[i].get_t_price() < self.budget and c_2_players[i].get_t_price() > value_best_player):
                        best_player = c_2_players[i]
                        value_best_player = c_2_players[i].get_t_price()
                        best_club = c_2;
                        break;
                i -= 1
        if (best_player != None):
            print "Set bid on other player by " + str(self.get_name())
            self.set_bid(best_player, value_best_player, best_club, False)
        else:
            self.buy_player(player, bid)
            club.sell_player(player, bid)
        self.counter_bids.pop(player,None)


