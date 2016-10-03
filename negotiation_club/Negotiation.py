from Club import club
from Competition import competition
from TransferList import transfer_list

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
    comp.add_club(club("feyenoord"))
    comp.init_transfer_list()
    #comp.find_optimal_team()
    comp.show_clubs()
    comp.show_transfer_list()

    for i in range(0,10):
        comp.visualizer.clean_up_arguments()
        for club in comp.get_clubs():
            raw_input("Press Enter to continue... for next club")
            print "-------- begin {} round --------------". format(club.get_name())
            club.start_argument(comp)
            print "reward :{}".format(club.get_previous_reward())
            club.check_bids(comp)
            print "----------end {} round -------------".format(club.get_name())


    comp.show_clubs()
