function update_arguments()
{
     var request = new XMLHttpRequest();
  request.open('GET', '/arguments', true);
  request.onreadystatechange = function()
  {
    if (request.readyState == 4)
    {
        var json = JSON.parse(request.responseText);
        make_graph(json['nodes'], json['edges']);
    }
  };
  request.send();
}

function make_graph(nodes, edges)
{
  var container = document.getElementById('mynetwork');

    var data =
    {
      nodes: new vis.DataSet(nodes),
      edges: new vis.DataSet(edges)
    };

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
