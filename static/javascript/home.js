$(document).ready(function(){
	

    $.fn.fullpage({
            anchors: ['home', 'analytics', 'interface'],
            onLeave: function(index, direction){
	            //after leaving section 2
	            if(index == '1' && direction =='down'){
	                // $('#header').animate({'height': '50px'}, 100);
	            }

	            else if(index == '2' && direction == 'up'){
	                // alert("Going to section 1!");
	            }
	        }
            // navigation: true,
            // navigationPosition: 'right',
            // navigationTooltips: ['Home', 'Video', 'White Paper', 'MAC Address Lookup'],
            // resize: true,
            // easing: 'linear',
            // scrollingSpeed: 400,
            // autoScrolling: false
    });
});

