from random import randint,uniform

class player():

    def __init__(self):
        self.name = ""
        self.att = randint(1,9)
        self.deff = randint(1,9)
        self.t_price = (self.att+self.deff)*uniform(0.9,1.1)

    def get_att(self):
        return self.att

    def get_deff(self):
        return self.deff

    def get_t_price(self):
        return self.t_price

