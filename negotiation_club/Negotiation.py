from Club import top_players_club,balanced_club
from Competition import competition

if __name__ == '__main__':
    comp = competition()
    top_clubs = ["Manchester United","Barcelona"]
    balanced_clubs = ["Ajax", "PSV"]
    for club in top_clubs:
        comp.add_club(top_players_club(club))

    for club in balanced_clubs:
        comp.add_club(balanced_club(club))

    for i in range(0,5):
        for club in comp.get_clubs():
            bid_accepted, player, bid, c_2 = club.check_bids()
            if bid_accepted:
                c_2.buy_player(player,bid)
                club.sell_player(player,bid)
                print club.get_name() + " sold :" + str(player.get_t_price()) + "  to " + c_2.get_name()
            elif(bid != None) :
                c_2.set_bid(player,bid,club)
            club.start_argument(comp.get_clubs())

    comp.show_clubs()

