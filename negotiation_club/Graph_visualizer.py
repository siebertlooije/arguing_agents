import requests
import json


class graph_visualizer():

    def __init__(self, ):
        self.players = {}
        self.clubs = []

    def dump_json(self, data, file = '../javascript/arguments'):
        with open(file, 'w+') as outfile:
            json.dump(data, outfile)

    def visualize_clubs(self, clubs):
        data = {}
        nodes = []
        self.clubs = clubs;
        for index, club in enumerate(clubs): #For the clubs
            dict = {"id" : index, "label" : club.get_name(), 'color' : 'orange'}
            nodes.append(dict)

        dict = {"id" : len(clubs), "label" : "Transfer lijst" , 'color' : 'pink'} #For the transfer lijst
        nodes.append(dict)
        data['nodes'] = nodes
        self.dump_json(data)

    def load_arguments(self):
        with open('../javascript/arguments') as data_file:
            data = json.load(data_file)
        return data

    def remove_arguments(self, club1, club2,player, argument_label):
        data = self.load_arguments()
        if argument_label == "Bid":
           for edge in data['edges']:
               if edge['from'] == self.clubs.index(club1) \
                       and edge['to'] == self.get_key(self.players,player) \
                       and edge['label'] == argument_label:
                    data['edges'].remove(edge)
        self.dump_json(data)

    def clean_up_arguments(self):
        data = self.load_arguments()
        rem_players = []
        if 'edges' in data:
            for edge in data['edges']:
                if  edge['label'] == "Sell":
                    data['edges'].remove(edge)
                    rem_players.append(edge['to'])

            for node in data['nodes']:
                if node['id'] in rem_players:
                    data['nodes'].remove(node)
                    self.players.pop(node['id'])

        self.dump_json(data)

    def check_nodes(self,node, nodes):
        return True if node in nodes else False

    def format_arguments(self, club1, club2, player, argument_label, color):
        data = self.load_arguments()

        nodes = data['nodes']
        edges = data['edges'] if 'edges' in data else []

        c_id1 = self.clubs.index(club1)
        c_id2 = self.clubs.index(club2)
        player_id = self.get_key(self.players,player)
        if  player_id not in self.players:
            id = len(self.clubs) + len(self.players) + 1
            dict = {"id" : id, "label" : "player :" + player.get_name() , 'color' : 'blue'}
            nodes.append(dict)
            data['nodes'] = nodes
            self.players[id] = player
            dict = {"from" : id, "to" : c_id2, "arrows" : 'to' , "label" : "Player of " + club2.get_name(),'color' : 'grey' , 'length':250 , 'physics' : 'false'}
            edges.append(dict)
        else:
            id = player_id

        dict = {"from": c_id1, "to": id , "arrows": 'to', "label": argument_label, 'color' : color, 'length' :250, 'physics' : 'false'}
        edges.append(dict)
        data['edges'] = edges
        self.dump_json(data, '../javascript/arguments')


    def get_key(self, dict, player):
        for id, p in dict.iteritems():
            if player == p:
                return id



