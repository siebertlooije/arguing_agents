import requests
import json

class graph_visualizer():

    def __init__(self, ):
        self.players = []
        self.clubs = []

    def dump_json(self, data, file = '../javascript/arguments'):
        with open(file, 'w+') as outfile:
            json.dump(data, outfile)

    def send_json(self, arguments):
        data = {}
        nodes = []
        for index, argument in enumerate(arguments):
            dict = {"id": index, "label": argument};
            nodes.append(dict)
        data['nodes'] = nodes
        return data

    def visualize_clubs(self, clubs):
        data = {}
        nodes = []
        self.clubs = clubs;
        for index, club in enumerate(clubs):
            dict = {"id" : index, "label" : club.get_name()}
            nodes.append(dict)
        data['nodes'] = nodes
        self.dump_json(data)


    def get_player_id(self, player):
        return (self.players.index(player) + len(self.clubs) + 1)

    def load_arguments(self):
        with open('../javascript/arguments') as data_file:
            data = json.load(data_file)
        return data;


    def remove_arguments(self, club1, club2,player, argument_label):
        data = self.load_arguments()
        if argument_label == "Bid":
           for edge in data['edges']:
               if edge['from'] == self.clubs.index(club1) \
                       and edge['to'] == self.get_player_id(player) \
                       and edge['label'] == argument_label:
                    data['edges'].remove(edge)
        self.dump_json(data)

    def clean_up_arguments(self):
        data = self.load_arguments()
        rem_playes = []
        if 'edges' in data:
            for edge in data['edges']:
                if edge['label'] == "Buy" or edge['label'] == "Sell":
                    data['edges'].remove(edge)
                    rem_playes.append(edge['to'])

            for node in data['nodes']:
                if node['id'] in rem_playes:
                    self.players.remove(self.players[node['id'] - len(self.clubs)])
                    data['nodes'].remove(node)
        self.dump_json(data)

    def check_nodes(self,node, nodes):
        return True if node in nodes else False



    def format_arguments(self, club1, club2, player, argument_label):
        data = self.load_arguments()

        nodes = data['nodes']
        edges = data['edges'] if 'edges' in data else []

        c_id1 = self.clubs.index(club1)
        c_id2 = self.clubs.index(club2)

        if player not in self.players:
            id = len(self.clubs) + len(self.players) + 1
            dict = {"id" : id, "label" : "player_" + str((len(self.players) + 1))}
            nodes.append(dict)
            data['nodes'] = nodes
            self.players.append(player)
            dict = {"from" : id, "to" : c_id2, "arrows" : 'to' , "label" : "Player of " + club2.get_name()}
            edges.append(dict)
        else:
            id = self.players.index(player) + len(self.clubs) + 1

        dict = {"from": c_id1, "to": id , "arrows": 'to', "label": argument_label}
        edges.append(dict)
        data['edges'] = edges
        self.dump_json(data, '../javascript/arguments')

    def make_data(self, node_size):
        data = {}
        nodes = []
        for i in range(0,node_size):
            dict = {"id" : i, "label" : "argument_" + str(i)};
            nodes.append(dict);
        data['nodes'] = nodes;

        edges = []
        for i in range(0, node_size):
            for j in range(0, node_size):
                if i == j:
                    continue;
                dict = {"from" : i, "to" : j, "arrows" : 'to', "label" : "R_"+ str(i) + "_" + str(j)}
                edges.append(dict)
        data['edges'] = edges;
        return data;



