import requests
import json

class set_json():

    def dump_json(self, data):

        with open('../javascript/state', 'w') as outfile:
            json.dump(data, outfile)

    def make_data(self, node_size):
        data = {};
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

if __name__ == '__main__':
    sj = set_json()
    node_size = 4
    data = sj.make_data(node_size);
    sj.dump_json(data);


