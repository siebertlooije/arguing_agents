import Club;
from Graph_visualizer import graph_visualizer
import csv

class competition():
    def __init__(self):
        self.clubs = []
        self.opt_club = Club.club("optimal");
        self.visualizer = graph_visualizer()
        self.player_names = self.read_in_names()

    def add_club(self, club):
        if club in self.clubs:
            self.clubs.remove(club)
        player_cnt = 0

        for index in range(len(self.clubs) * (club.n_players),(len(self.clubs) + 1) * (club.n_players)):
            if index > 100: #length of player name list
                break
            club.get_players()[player_cnt].set_name(self.player_names[index])
            player_cnt += 1

        self.clubs.append(club)


    def read_in_names(self):
        player_names = []
        with open('../footballers.csv') as csvfile:
            reader = csv.reader(csvfile)
            next(reader, None) #skip header
            for row in reader:
                player_names.append(row[1])
        return player_names



    def get_opt_club(self):
        return self.opt_club

    def add_clubs(self,c_1,c_2):
        self.clubs.remove(c_2)
        self.clubs.remove(c_1)
        self.clubs.append(c_2)
        self.clubs.append(c_1)

    def get_index_club(self, club):
        return self.clubs.index(club)

    def get_clubs(self):
        return self.clubs

    def show_clubs(self):
        for club in self.clubs:
            print "Club name :" + club.get_name() + " budget :" + str(club.get_budget())
            for player in club.get_players():
                print "player name : " + str(player.get_name()) + "  player value :" +  str(player.get_t_price()) + " att :" + str(player.get_att()) + " deff :" + str(player.get_deff())
            print "Total team value :" + str(club.get_team_value())
            self.visualizer.visualize_clubs(self.clubs)

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








