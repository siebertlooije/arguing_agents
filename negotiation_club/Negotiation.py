from Balanced_club import balanced_club
from Top_players_club import top_players_club;
from Club import club
from Competition import competition

if __name__ == '__main__':
    comp = competition()
    top_clubs = ["Manchester United"]
    balanced_clubs = ["Ajax"]
#    for club in top_clubs:
#       comp.add_club(top_players_club(club))

#    for club in balanced_clubs:
#       comp.add_club(balanced_club(club))
    comp.add_club(club("ajax"));
    comp.add_club(club("manchester"));

    #comp.find_optimal_team()
    comp.show_clubs()
    for i in range(0,10):
        for club in comp.get_clubs():
            print "-------- begin {} round --------------".format(club.get_name())
            club.start_argument(comp)
            print "reward :{}".format(club.get_previous_reward())
            club.check_bids()
            print "----------end {} round -------------".format(club.get_name())

    comp.show_clubs()
    """
    for i in range(0,10):
        for club in comp.get_clubs():

            print "--------{}----------".format(club.get_name())
            club.start_argument(comp.get_clubs())
            club.check_bids()
            #club.counter_argument(comp.get_clubs())
            #bid_accepted, player, bid, c_2 = club.check_bids()
            #if bid_accepted:
            #    c_2.buy_player(player,bid)
            #    club.sell_player(player,bid)
            #    print club.get_name() + " sold :" + str(bid) + "  to " + c_2.get_name()

            #elif(bid != None):
            #    print club.get_name() + " did counter proposal :" + str(bid) + "  to " + c_2.get_name()
            #    c_2.set_counter_bids(bid, player, club)

            print "-----------------------------\n"

    """
