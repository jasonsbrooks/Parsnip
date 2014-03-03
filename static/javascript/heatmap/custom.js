$(document).ready(function () {
	 // heatmap configuration
    var config = {
        element: document.getElementById("heatmapArea"),
        radius: 10,
        opacity: 50,
        legend: {
            position: 'br',
            title: 'foot traffic in store'
        }   
    };
    
    var obj = {}    // Store the foot traffic data.
    // obj = {1:[x, y, time], 2: ...}

    var i = 0;      // Number of data points in obj

    //creates and initializes the heatmap
    var heatmap = h337.create(config);
    
    heatmap.store.setDataSet({ max: 10, data: []});

    var startTime;  // Time of first click.

    var active = false, // true when mouse is clicked.
        firstClick = true;  // to set startTime
    
    

    $('#heatmapArea').mousedown(function() {
        console.log("mouse down");
        active = true;
        if (firstClick) {
            firstClick = false;
            startTime = new Date();
        }
    });

    $('#heatmapArea').mouseup(function() {
            console.log("mouse UP");
            active = false;
    });

    setInterval(function(){       
        if (active === true) {
            console.log("active")
        }
    }, 100);

    $('#heatmapArea').mousemove(function(event) {
        
        
        x = event.clientX,
        y = event.clientY
        

        if (active) {
            var dTime = (new Date() - startTime) / 1000
            $('#data-table').append(x + ", " + y + ", " + dTime + "<br>");
            heatmap.store.addDataPoint(x, y, 3);
            obj[i++] = [x, y, dTime]
        }
    });
    
   

    $('#replay').click(function() {
        console.log('REPLAY');
        $('#heatmapArea').html("");
        heatmap = h337.create(config)
        console.log(obj);
    });


});