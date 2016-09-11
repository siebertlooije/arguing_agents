from Club import club

class competition():


    def __init__(self):
        self.clubs = []

    def add_club(self, club):
        if club in self.clubs:
            self.clubs.remove(club)

        self.clubs.append(club)


    def add_clubs(self,c_1,c_2):
        self.clubs.insert(0,c_2)
        self.clubs.insert(1,c_1)


    def get_clubs(self):
        return self.clubs


