$(document).ready(function(){
    edges_length = 0;
});


function make_clubs(competition)
{
  for (var index = 0; index != competition.length; index++) {
    var dict = {"id": index, "label": competition[index].name, 'color': 'orange'}

    data.nodes.add(dict)
  }
}

function remove_bid(playername,club2index)
{
  var player_id = check_player_graph(playername)
  for(var index = 0; index != edges_length; index ++)
  {
    if(data.edges.get(index).from == player_id && data.edges.get(index).to == club2index)
    {
        data.edges.splice(index,1);
        edges_length++;
    }
  }
}

function add_refuse(playername, club1index, bid)
{
    var player_id = check_player_graph(playername);
    dict = {"id": edges_length + 1,"from": club1index, "to": player_id, "arrows": 'to', "label": "Bid too low :" + bid.toFixed(2), 'color': 'red', 'length': 400}
    data.edges.add(dict)
    edges_length++;
    update_graph()
}

function add_sold(playername, club1index, club2index, bid)
{
    var player_id = check_player_graph(playername);
    dict = {"id" : edges_length + 1,"from": club1index, "to": player_id, "arrows": 'to', "label": "Sold with price : " + bid.toFixed(2), 'color': 'purple', 'length': 400}
    data.edges.add(dict)
    edges_length++
    dict = {"id" : edges_length + 1, "from": club2index, "to": player_id, "arrows": 'to', "label": "Buy with price :" + bid.toFixed(2), 'color': 'pink', 'length': 400}
    data.edges.add(dict)
    edges_length++
    update_graph()
}


function check_player_graph(playername)
{
  for(var index = 0; index != data.nodes.length; index++)
  {
    if(data.nodes.get(index).label == playername)
      return index
  }
  return null
}

function make_bid(player,club1_index, club2_index, bid)
{
  var player_id = null;
  if(check_player_graph(player.name) == null)
  {
    var dict = {"id": data.nodes.length,"label": player.name, 'color': 'blue'}
    player_id = data.nodes.length
    data.nodes.add(dict)
    dict = {"id" : edges_length + 1, "from": player_id, "to": club2_index, "arrows": 'to', "label": "player of", 'color': 'grey', 'length': 400}
    data.edges.add(dict)
      edges_length++
    dict = {"id" : edges_length + 1,"from": club1_index, "to": player_id, "arrows": 'to', "label": "bid :" + bid.toFixed(2), 'color': 'green', 'length': 400}
    data.edges.add(dict)
      edges_length++
  }
  else
  {
    player_id = check_player_graph(player.name);
    dict = { "id" : edges_length + 1 , "from": club1_index, "to": player_id, "arrows": 'to', "label": "bid :"+ bid.toFixed(2) , 'color': 'green', 'length': 400}
    data.edges.add(dict)
      edges_length ++
  }
  update_graph()
}

function update_graph()
{
    var container = document.getElementById('mynetwork');
       var options =
      {
      layout:
      {
          improvedLayout:false,
          hierarchical:
          {
            enabled: false,
            nodeSpacing:400,
            levelSeparation: 300,
            treeSpacing: 400,
          }
      }
  };
  var network = new vis.Network(container, data, options);
}


function make_graph(competition)
{

    data =
    {
      nodes: new vis.DataSet(),
      edges: new vis.DataSet()
    };
    make_clubs(competition);
    update_graph();
}
