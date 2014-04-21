$(document).ready(function() {
  $('.change-user-status').ajaxForm({url: '/user/approval_status', type: 'post',
        success: function(data){
            var email = data.email;
            var remInput = $('input').filter(function() { return this.value == email })[0];
            $(remInput).closest('li').fadeOut(300, function() { $(this).remove(); });
            $('#user-pending-count').html(parseInt($('#user-pending-count').html())-1);
            var newPendingCount = (parseInt($("#dropdown-pending-count").text().split(' ')[2])-1).toString();
            if (parseInt(newPendingCount) == 1){
              var newPendingText = "You have 1 notification";
            }
            else{
              var newPendingText ="You have " + newPendingCount + " notifications";
            }
            $('#dropdown-pending-count').html(newPendingText);
            
    }});
}); 

function initBarChart(target) {

  // X's set the order of the bars. Y's are the value of bar.
  var data = [ { x:0, y:10 }, { x:1, y:30 }, { x:2, y:45 }, { x:3, y:25 }, { x:4, y:70 }, { x:5, y:75 }, { x:6, y:50 }, { x:7, y:80 }];

  var graph = new Rickshaw.Graph({
    element: document.querySelector(target),
    width: 400,
    renderer: 'bar',
    series: [{
      data: data,
      color: 'steelblue',
      // NAME is the label to give the y-value of the bar.
      name: 'Count'
    }]
  });
   
  graph.render();

  // Maps a bar to a label.
  var map = {0:'Bottoms', 1:'Tops', 2:'Shoes', 3:'Accessories', 4:'Jackets', 5:'Underwear', 6:'Athletic Clothes', 7:'Jewelery'};

  var hoverDetail = new Rickshaw.Graph.HoverDetail( {
    graph: graph,
    xFormatter: function(x) { return "Type: " + map[x];},
    yFormatter: function(y) { return y;}
  } );
}

function initLineChart(target) {

  var palette = new Rickshaw.Color.Palette();

  var graph = new Rickshaw.Graph( {
    element: document.querySelector("#chart"),
    width: 400,
    renderer: 'line',
    series: [
      {
        name: "Girls",
        data: [ { x:0, y:156 }, {x:1*60*60*24*5, y:153}, {x:2*60*60*24*5,y:250}, {x:3*60*60*24*5,y:603}, {x:4*60*60*24*5, y:650}, {x:5*60*60*24*5,y:642}, {x:6*60*60*24*5,y:654} ],
        color: palette.color()
      },
      {
        name: "Guys",
        data: [ { x:0, y:56 }, {x:1*60*60*24*5, y:103}, {x:2*60*60*24*5,y:257}, {x:3*60*60*24*5,y:503}, {x:4*60*60*24*5,y:642}, {x:5*60*60*24*5,y:654}, {x:6*60*60*24*5,y:630} ],
        color: palette.color()
      }
    ]
  } );

  var x_axis = new Rickshaw.Graph.Axis.Time( { graph: graph } );

  var y_axis = new Rickshaw.Graph.Axis.Y( {
    graph: graph,
    orientation: 'left',
    tickFormat: Rickshaw.Fixtures.Number.formatKMBT,
    element: document.getElementById('y_axis')
  } );

  var legend = new Rickshaw.Graph.Legend( {
    element: document.querySelector('#legend'),
    graph: graph
  } );

  var offsetForm = document.getElementById('offset_form');

  offsetForm.addEventListener('change', function(e) {
    var offsetMode = e.target.value;

    if (offsetMode == 'lines') {
      graph.setRenderer('line');
      graph.offset = 'zero';
    } else {
      graph.setRenderer('stack');
      graph.offset = offsetMode;
    }       
    graph.render();

  }, false);

  graph.render();

}

function initMultiGraph() {
  var seriesData = [ [], [], [], [], [] ];
  var random = new Rickshaw.Fixtures.RandomData(50);

  for (var i = 0; i < 75; i++) {
    random.addData(seriesData);
  }

  // SERIESDATA is basically an array of arrays, where each array stores objects
  // with an x and y value. The x value is time in epoch seconds, and the y 
  // value is the value of whatever the object and array of objects measures at 
  // time x. For example, [ [ {"x":0, "y":55.32}, ...], ...], states that at
  // time 0, the metric measured by the first array of objects had a value of 
  // 55.32.
  
  // console.log('begin0');
  // console.log(JSON.stringify(seriesData[0]));
  // console.log('begin1');
  // console.log(JSON.stringify(seriesData[1]));
  // console.log('begin2');
  // console.log(JSON.stringify(seriesData[2]));
  // console.log('begin3');
  // console.log(JSON.stringify(seriesData[3]));
  // console.log('begin4');
  // console.log(JSON.stringify(seriesData[4]));

  var graph = new Rickshaw.Graph( {
    element: document.getElementById("chart3"),
    renderer: 'multi',
    width: 900,
    height: 500,
    dotSize: 2,
    series: [
      {
        name: 'Node 1 Traffic',
        data: seriesData.shift(),
        color: 'rgba(255, 0, 0, 0.4)',
        renderer: 'stack'
      }, {
        name: 'Node 2 Traffic',
        data: seriesData.shift(),
        color: 'rgba(255, 127, 0, 0.4)',
        renderer: 'stack'
      }, {
        name: 'Visitors',
        data: seriesData.shift(),
        color: 'rgba(127, 0, 0, 0.3)',
        renderer: 'scatterplot'
      }, {
        name: 'Sales',
        data: seriesData.shift().map(function(d) { return { x: d.x, y: d.y / 4 };}),
        color: 'rgba(0, 0, 127, 0.4)',
        renderer: 'bar'
      }, {
        name: 'Inventory',
        data: seriesData.shift().map(function(d) { return { x: d.x, y: d.y };}),
        renderer: 'line',
        color: 'rgba(0, 0, 127, 0.25)'
      }
    ]
  } );

  // TODO: Fix slider.
  //var slider = new Rickshaw.Graph.RangeSlider({
  //  graph: graph,
  //  element: $('#slider3')
  //});

  graph.render();

  var detail = new Rickshaw.Graph.HoverDetail({
    graph: graph
  });
}
