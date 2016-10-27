$(function(){ // on dom ready

$('#cy').cytoscape({
  layout: {
    name: 'cose',
    padding: 10,
    randomize: true
  },
  
  style: cytoscape.stylesheet()
    .selector('node')
      .css({
        'shape': 'data(faveShape)',
        'width': 'mapData(weight, 40, 80, 20, 60)',
        'content': 'data(name)',
        'text-valign': 'center',
        'text-outline-width': 2,
        'text-outline-color': 'data(faveColor)',
        'background-color': 'data(faveColor)',
        'color': '#fff'
      })
    .selector(':selected')
      .css({
        'border-width': 3,
        'border-color': '#333'
      })
    .selector('edge')
      .css({
        'curve-style': 'bezier',
        'opacity': 0.666,
        'width': 'mapData(strength, 70, 100, 2, 6)',
        'target-arrow-shape': 'triangle',
        'source-arrow-shape': 'circle',
        'line-color': 'data(faveColor)',
        'source-arrow-color': 'data(faveColor)',
        'target-arrow-color': 'data(faveColor)'
      })
    .selector('edge.questionable')
      .css({
        'line-style': 'dotted',
        'target-arrow-shape': 'diamond'
      })
    .selector('.faded')
      .css({
        'opacity': 0.25,
        'text-opacity': 0
      }),
  
  elements: {
    nodes: [
      { data: { id: 'President', name: 'President', weight: 70, faveColor: '#6FB1FC', faveShape: 'triangle' } },
      { data: { id: 'CEO', name: 'CEO', weight: 70, faveColor: '#EDA1ED', faveShape: 'ellipse' } },
      { data: { id: 'Trainer', name: 'Trainer', weight: 70, faveColor: '#86B342', faveShape: 'octagon' } },
      { data: { id: 'Captain', name: 'Captain', weight: 70, faveColor: '#F5A45D', faveShape: 'rectangle' } },
      { data: { id: 'Supporters', name: 'Supporters', weight: 70, faveColor: '#939393', faveShape: 'diamond' } }
    ],
    edges: [
      { data: { source: 'President', target: 'CEO', faveColor: '#6FB1FC', strength: 80 } },
      { data: { source: 'President', target: 'Trainer', faveColor: '#6FB1FC', strength: 80 } },
      
      { data: { source: 'Trainer', target: 'President', faveColor: '#86B342', strength: 80 } },
      { data: { source: 'Trainer', target: 'CEO', faveColor: '#86B342', strength: 80 } },
      
      { data: { source: 'CEO', target: 'President', faveColor: '#EDA1ED', strength: 80 } },
      { data: { source: 'CEO', target: 'Trainer', faveColor: '#EDA1ED', strength: 80 } },
      
      { data: { source: 'Supporters', target: 'Supporters', faveColor: '#939393', strength: 80 } },
      
      { data: { source: 'Captain', target: 'Captain', faveColor: '#F5A45D', strength: 80 } },
      
    ]
  },
  
  ready: function(){
    window.cy = this;
    
    // giddy up
  }
});

}); // on dom ready