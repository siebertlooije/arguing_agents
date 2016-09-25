import Club;

class competition():
    def __init__(self):
        self.clubs = []
        self.opt_club = Club.club("optimal");

    def add_club(self, club):
        if club in self.clubs:
            self.clubs.remove(club)

        self.clubs.append(club)

    def get_opt_club(self):
        return self.opt_club

    def add_clubs(self,c_1,c_2):
        self.clubs.remove(c_2)
        self.clubs.remove(c_1)
        self.clubs.append(c_2)
        self.clubs.append(c_1)


    def get_clubs(self):
        return self.clubs

    def show_clubs(self):
        for club in self.clubs:
            print "Club name :" + club.get_name() + " budget :" + str(club.get_budget())
            for player in club.get_players():
                print "player value :" +  str(player.get_t_price()) + " att :" + str(player.get_att()) + " deff :" + str(player.get_deff())
            print "Total team value :" + str(club.get_team_value())

    def show_club(self, club):
        print "Club name :" + club.get_name() + " budget :" + str(club.get_budget())
        for player in club.get_players():
            print "player value :" +  str(player.get_t_price()) + " att :" + str(player.get_att()) + " deff :" + str(player.get_deff())
        print "Total team value :" + str(club.get_team_value())




    def find_optimal_team(self):
        opt_club = Club.club("optimal")
        opt_club.remove_all_players()


        for club in self.clubs:
            counter = 0;
            while (len(opt_club.get_players()) < 15):
                opt_club.get_players().append(club.get_players()[counter]);
                counter += 1;
            opt_club.find_better_players(club);
        self.opt_club = opt_club;
        self.show_club(opt_club)








