from Club import top_players_club,balanced_club
from Competition import competition

if __name__ == '__main__':
    comp = competition()

    c_1 = top_players_club("Manchester United")
    c_2 = balanced_club("Barcelona")
    comp.add_club(c_1)
    comp.add_club(c_2)

    for i in range(0,5):
        for club in comp.get_clubs():
            print club.get_name()
            bid_accepted, player, bid, c_2 = club.check_bids()
            if bid_accepted:
                c_2.buy_player(player,bid)
                club.sell_player(player,bid)

            c_2 = club.start_argument(comp.get_clubs())
            comp.add_clubs(club,c_2)

